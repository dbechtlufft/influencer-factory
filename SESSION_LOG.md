# SESSION_LOG — influencer-factory

## 2026-09-04 — Brief do teste TikTok atualizado (decisões fechadas)

Cópia do brief em knowledge/do-balcao substituída pela versão com decisões de 04/09 (Shopee+Hotmart, nichos mulher 40+ e casa, 2 contas business, vídeos 20–30s, checklist pré-sessão e aprendizados do podcast Sidney Giorni). Sessão de execução (run_batch.py + 10 vídeos) começa após o checklist do Diego.


## 2026-08-25 — Bootstrap do repo + MPT e2e validado (fase 0)

Repo criado no padrão (a casca "Nova pasta" ficou para o Diego apagar — rename trava com a
sessão aberta) e MoneyPrinterTurbo validado e2e na 3060: short faceless pt-BR de 44s
(1080×1920, voz Francisca/edge-tts, legendas edge, material NASA domínio público), sem
nenhuma API key — roteiro pronto via `video_script`, `video_source=local`. Review de 7
finders: 11 achados, 10 aplicados (destaques: BGM bundled do MPT é ripado de YouTube →
desligado; setup reprodutível com `setup.ps1` + `materials.json` pinando MPT em 68ce652);
migração pro `cli.py` upstream ficou como pendência de escopo. Vídeo final:
`MoneyPrinterTurbo/storage/tasks/e2e-20260825-015904/final-1.mp4`. Remote GitHub pendente de
confirmação (`gh repo create influencer-factory --private --source . --push`).
