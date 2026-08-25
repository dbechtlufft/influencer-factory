# influencer-factory

Fábrica de influencer sintético: esteira faceless (roteiro → TTS → legendas → montagem)
primeiro, persona (LoRA + lip-sync) depois. Relatório-mãe:
https://claude.ai/code/artifact/96cf77cf-98c5-493a-8146-00af38062da1

## Stack

- Python 3.12 local (upstream pinna 3.11 em `.python-version`; e2e validado em 3.12).
- `MoneyPrinterTurbo/` = clone vendorado (MIT, gitignorado) de
  https://github.com/harry0703/MoneyPrinterTurbo, pinado em `68ce652` pelo `setup.ps1`.
  Chamamos `app.services.task.start()` direto em Python; não usamos webui/API server.
- ffmpeg vem do `imageio-ffmpeg` (pip); não há ffmpeg no sistema.

## Comandos

- Setup (máquina limpa): `.\setup.ps1` — clona MPT pinado, venv+pip, baixa materiais
  do `materials.json` (NASA, domínio público, sem API key).
- E2E (short pt-BR sem LLM/sem stock API): `.venv\Scripts\python run_e2e.py`

## Decisões que valem

- Roteiro: `video_script` pronto nos params → pipeline não chama LLM nenhum.
- Material: `video_source="local"`; proveniência versionada em `materials.json`
  (Pexels precisa de key que ainda não temos).
- Legendas: timing do edge-tts. O knob real é `subtitle_provider` no config.toml do
  MPT (gitignorado, reescrito pela WebUI) — por isso o `run_e2e.py` enforça via
  `config.app["subtitle_provider"] = "edge"` e FALHA se o vídeo sair sem legenda.
- BGM: as músicas bundled do MPT são ripadas de YouTube (README-en.md:405) —
  proibidas para publicação; `bgm_type=""` até termos trilha CC0 própria (`bgm_file`).
- Publicação futura: YouTube API + IG Graph, NÃO o Upload-Post do MPT.

## Gotchas

- `video_concat_mode="sequential"` usa só os primeiros `video_clip_duration`s de CADA
  clipe e loopa (video.py:612) — usar `random` (default) para aproveitar o footage.
- Fonte 16:9 vira letterbox no 9:16 (MPT não cropa) — pré-cortar material pra vertical
  quando a estética importar.
- A montagem é moviepy/CPU; a 3060 só entra na fase persona.

## Pendente (entrevista creating-claude-md)

- Gotchas/out-of-scope/gates de aprovação — entrevistar Diego quando o repo crescer.
- Chave Pexels (ou decisão de ficar em local/CC0) para material de stock real.
- Migrar o runner para o `cli.py`/`docs/skill/mpt_agent.py` do MPT (driver testado
  upstream, contrato JSON) em vez do `task.start()` manual — decisão de escopo.
- Fase 1+: persona (LoRA, EchoMimicV3/InfiniteTalk, MuseTalk), clone de voz
  (Chatterbox via `travisvn/chatterbox-tts-api`; referência registra no servidor).
