# influencer-factory

Fábrica de influencer sintético: esteira faceless (roteiro → TTS → legendas → montagem)
primeiro, persona (LoRA + lip-sync) depois. Relatório-mãe:
https://claude.ai/code/artifact/96cf77cf-98c5-493a-8146-00af38062da1

## Stack

- Python 3.12 + venv em `.venv/` (raiz do repo).
- `MoneyPrinterTurbo/` = clone vendorado (MIT, gitignorado) — a esteira de montagem.
  Chamamos `app.services.task.start()` direto em Python; não usamos webui/API server.
- ffmpeg vem do `imageio-ffmpeg` (pip); não há ffmpeg no sistema.

## Comandos

- Setup: `python -m venv .venv && .venv\Scripts\pip install -r MoneyPrinterTurbo\requirements.txt`
- E2E (short pt-BR sem LLM/sem stock API): `.venv\Scripts\python run_e2e.py`

## Decisões que valem

- Roteiro: `video_script` pronto nos params → pipeline não chama LLM nenhum.
- Material: `video_source="local"` + clipes em `MoneyPrinterTurbo/storage/local_videos/`
  (domínio público/CC0; Pexels precisa de key que ainda não temos).
- Legendas: `subtitle_provider="edge"` (timing do edge-tts; whisper só se precisar).
- Publicação futura: YouTube API + IG Graph, NÃO o Upload-Post do MPT.

## Pendente (entrevista creating-claude-md)

- Gotchas/out-of-scope/gates de aprovação — entrevistar Diego quando o repo crescer.
- Chave Pexels (ou decisão de ficar em local/CC0) para material de stock real.
- Fase 1+: persona (LoRA, EchoMimicV3/InfiniteTalk, MuseTalk), clone de voz (Chatterbox).
