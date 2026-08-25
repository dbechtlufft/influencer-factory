# -*- coding: utf-8 -*-
"""E2E fase 0: short faceless pt-BR via MoneyPrinterTurbo, sem LLM e sem stock API.

Roteiro pronto em video_script (nenhuma chamada de LLM) + video_source=local
(clipes de dominio publico da NASA — proveniencia em materials.json, download
via setup.ps1). Saida em MoneyPrinterTurbo/storage/tasks/<task_id>/final-1.mp4.
"""

import os
import sys
import time

MPT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MoneyPrinterTurbo")

SCRIPT = (
    "Você sabia que o espaço esconde segredos incríveis? Aqui vão três curiosidades "
    "que vão mudar a forma como você vê o céu. Primeira: a Estação Espacial "
    "Internacional dá uma volta completa na Terra a cada noventa minutos. Os "
    "astronautas lá em cima veem dezesseis nasceres do sol por dia. Segunda: a Lua "
    "está se afastando da Terra quase quatro centímetros por ano. Num futuro "
    "distante, os eclipses totais do Sol vão simplesmente deixar de existir. "
    "Terceira: uma única erupção solar pode liberar mais energia do que milhões de "
    "bombas atômicas juntas. E o mais impressionante: tudo isso está acontecendo "
    "agora, bem acima da sua cabeça. Se você curtiu, guarda esse vídeo e compartilha "
    "com alguém que ama o espaço."
)


def main() -> int:
    if not os.path.isdir(MPT_ROOT):
        print("ERRO: MoneyPrinterTurbo/ não existe — rode .\\setup.ps1 primeiro.")
        return 1
    sys.path.append(MPT_ROOT)

    from app.config import config
    from app.models import const
    from app.models.schema import MaterialInfo, VideoParams
    from app.services import task
    from app.utils import utils

    # Decisão do projeto (CLAUDE.md): legendas com timing do edge-tts. O knob
    # real vive no config.toml do MPT (gitignorado e reescrito pela WebUI),
    # então a decisão é enforçada aqui, em código versionado.
    config.app["subtitle_provider"] = "edge"

    local_videos_dir = utils.storage_dir("local_videos", create=True)
    extensions = tuple(f".{e}" for e in const.FILE_TYPE_VIDEOS + const.FILE_TYPE_IMAGES)
    materials = [
        MaterialInfo(url=name)
        for name in sorted(os.listdir(local_videos_dir))
        if name.lower().endswith(extensions)
    ]
    if not materials:
        print(f"ERRO: nenhum material em {local_videos_dir} — rode .\\setup.ps1.")
        return 1
    print(f"materiais locais: {[m.url for m in materials]}")

    params = VideoParams(
        # Obrigatório no schema, mas inerte com video_source=local e sem
        # publicação: nada consome video_subject neste modo.
        video_subject="3 curiosidades sobre o espaço",
        video_script=SCRIPT,
        video_source="local",
        video_materials=materials,
        # As músicas bundled do MPT vêm de vídeos do YouTube (README-en.md:405,
        # copyright incerto) — BGM só com bgm_file próprio CC0.
        bgm_type="",
        voice_name="pt-BR-FranciscaNeural-Female",
        font_name="BeVietnamPro-Bold.ttf",
        font_size=56,
        n_threads=4,
    )

    task_id = time.strftime("e2e-%Y%m%d-%H%M%S")
    print(f"task_id: {task_id}")
    result = task.start(task_id, params, stop_at="video") or {}

    for warning in result.get("warnings") or []:
        print(f"AVISO do pipeline: {warning}")

    videos = result.get("videos") or []
    if not videos:
        print(f"\nFALHOU — stage: {result.get('failed_stage')}, erro: {result.get('error')}")
        return 1
    # Legenda é parte do critério do e2e; o pipeline a degrada sem falhar.
    if not result.get("subtitle_path"):
        print("\nFALHOU — vídeo gerado SEM legendas (degradação silenciosa do edge):")
        for v in videos:
            print(f"  {v}")
        return 1

    print("\nOK — video final:")
    for v in videos:
        print(f"  {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
