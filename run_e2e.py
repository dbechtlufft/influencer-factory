# -*- coding: utf-8 -*-
"""E2E fase 0: short faceless pt-BR via MoneyPrinterTurbo, sem LLM e sem stock API.

Roteiro pronto em video_script (nenhuma chamada de LLM) + video_source=local
(clipes de dominio publico da NASA em MoneyPrinterTurbo/storage/local_videos/).
Saida em MoneyPrinterTurbo/storage/tasks/<task_id>/final-1.mp4.
"""

import os
import sys
import time

MPT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MoneyPrinterTurbo")
sys.path.insert(0, MPT_ROOT)
os.chdir(MPT_ROOT)

from app.models.schema import MaterialInfo, VideoParams  # noqa: E402
from app.services import task  # noqa: E402

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

LOCAL_VIDEOS_DIR = os.path.join(MPT_ROOT, "storage", "local_videos")


def main() -> int:
    materials = [
        MaterialInfo(provider="local", url=name)
        for name in sorted(os.listdir(LOCAL_VIDEOS_DIR))
        if name.lower().endswith(".mp4")
    ]
    if not materials:
        print(f"ERRO: nenhum clipe em {LOCAL_VIDEOS_DIR}")
        return 1
    print(f"materiais locais: {[m.url for m in materials]}")

    params = VideoParams(
        video_subject="3 curiosidades sobre o espaço",
        video_script=SCRIPT,
        video_source="local",
        video_materials=materials,
        video_aspect="9:16",
        video_concat_mode="sequential",
        video_clip_duration=5,
        video_count=1,
        voice_name="pt-BR-FranciscaNeural-Female",
        voice_rate=1.0,
        bgm_type="random",
        bgm_volume=0.2,
        subtitle_enabled=True,
        subtitle_position="bottom",
        font_name="BeVietnamPro-Bold.ttf",
        font_size=56,
        text_fore_color="#FFFFFF",
        stroke_color="#000000",
        stroke_width=1.5,
        n_threads=4,
    )

    task_id = time.strftime("e2e-%Y%m%d-%H%M%S")
    print(f"task_id: {task_id}")
    result = task.start(task_id, params, stop_at="video")

    videos = (result or {}).get("videos") or []
    if videos:
        print("\nOK — video final:")
        for v in videos:
            print(f"  {v}")
        return 0
    print(f"\nFALHOU — resultado: {result}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
