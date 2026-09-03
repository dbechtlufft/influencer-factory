# Teste de vídeo faceless no TikTok — brief e fatos de monetização
**Origem:** balcão, sessão de 2026-09-03

## Decisões / Respostas

- Receita de anúncio não é o jogo: Creator Rewards do TikTok paga US$0,01–0,04/mil views, só vídeo ≥60s, exige 10k seguidores + 100k views/30d. YouTube: regra "conteúdo inautêntico" (jul/2025) derrubou milhares de canais faceless em 2026; IA como ferramenta segue permitida com edição/ponto de vista humano.
- Afiliado do TikTok Shop BR exige ~2.000 seguidores (piloto abaixo disso; sinais de cair pra 1.000). Conta nova não monetiza no vídeo 1 pelo Shop. Conta business libera link na bio no dia 1 → afiliado externo enquanto o Shop não destrava.
- Decisões do teste: TikTok, conta nova business; monetização-alvo TikTok Shop afiliado; postagem manual pelo celular (API de postagem trava app não auditado em privado); som trending adicionado no app cobre a ausência de BGM.
- Fora de escopo agora: persona/LoRA, API de postagem, migração pro cli.py do MPT.

## O que já existe no influencer-factory (fase 0, validado 2026-08-25)

- MoneyPrinterTurbo vendorado, pinado em 68ce652. Esteira: roteiro pronto → edge-tts
  (pt-BR-FranciscaNeural) → legendas (timing edge) → montagem moviepy. 1080×1920, 44s, sem API key.
- Runner: `run_e2e.py` — 1 roteiro hardcoded, material local (NASA, domínio público), BGM off.
- Sem chave Pexels. Sem trilha CC0. Publicação por API é "futura" (YouTube API + IG Graph).

## Lacunas para o teste (o que construir nas próximas horas)

1. **Runner em lote:** `run_batch.py` lendo `batch/<nicho>/NN.md` (roteiro + legenda/hashtags no
   frontmatter) → N `final.mp4` + `NN.caption.txt`. Reusa o esqueleto do `run_e2e.py`.
2. **Material do nicho:** NASA não serve pra produto. Opções em ordem de custo:
   (a) chave Pexels grátis + `video_source="pexels"` (MPT já suporta);
   (b) imagens do próprio produto/afiliado com ken burns (MPT aceita imagens em `local_videos`).
   Pré-cortar pra 9:16 (MPT letterboxa 16:9).
3. **Roteiros:** 10 roteiros escritos na sessão pelo Claude (sem LLM no pipeline — decisão do
   repo). Estrutura: hook em 2s, 3 pontos, CTA "segue pra parte 2". 45–60s.
4. **Postagem manual** do celular (API do TikTok trava app não auditado em privado). Adicionar
   som trending no app na hora de postar — cobre a ausência de BGM e ajuda alcance.
5. **NÃO fazer agora:** persona/LoRA, API de postagem, migração pro cli.py do MPT.

## Decisões pendentes (Diego)

- **Nicho/produto.** Critério: produto de TikTok Shop com comissão ≥15%, explicável em 45s sem
  mostrar rosto, com footage acessível (Pexels ou fotos do produto). Ideia no ar: nicho feminino
  40+ (tweet do Bruno Faggion: apps pra mulheres rendem 2×). Decidir no início da sessão.
- **Conta:** TikTok nova, tipo business (libera link na bio dia 1 → afiliado externo enquanto o
  Shop não destrava).

## Desenho do teste e critério de morte

- 10 vídeos em 5 dias (2/dia), mesmo nicho, mesma hora. Métricas: views médias, retenção 3s,
  seguidores ganhos, cliques no link da bio.
- **Mata:** <500 views médias após 10 vídeos OU 0 clique no link. **Continua:** curva subindo
  ou ≥1 clique → mais 10 vídeos rumo aos 1.000 seguidores.
- Registrar resultado diário num `experiments/2026-09-tiktok-<nicho>.md` no influencer-factory.

## Prompt pra abrir a sessão no influencer-factory

```
Lê knowledge/do-balcao/2026-09-03-teste-tiktok-faceless.md — é o brief de hoje.
Objetivo das próximas horas: sair com 10 vídeos faceless prontos (mp4 + caption) pra eu postar
manualmente numa conta nova de TikTok. Nicho/produto: <PREENCHER>. Constrói o run_batch.py
reusando o run_e2e.py, resolve o material do nicho (Pexels se eu passar a chave, senão imagens
do produto com ken burns), escreve os 10 roteiros e gera tudo. Não mexe em persona, API de
postagem nem migração pro cli.py. Ao final, cria experiments/2026-09-tiktok-<nicho>.md com o
critério de morte do brief e a tabela diária vazia.
```

## Referências

- Benchmark externo: @jonhodev, 2026-09-02 — 25 vídeos no TikTok Shop = R$24, promete atualização diária: https://x.com/jonhodev/status/2095187547022324000
- Requisitos TikTok Shop BR: https://zibshop.com.br/ativar-tiktok-shop/requisitos-tiktok-shop · sinal de 1.000 seguidores: https://www.tiktok.com/@lucaskalango/video/7580159632656715026
- YouTube inauthentic content: https://arwriterai.com/en/blog/youtube-inauthentic-content-policy-ai-creators-2026/ · onda de suspensões: https://milx.app/en/news/why-youtube-just-suspended-thousands-of-ai-channels-and-how-to-protect-yours
- Creator Rewards: https://kineclip.com/blog/tiktok-creator-rewards-program-guide/

## Pendências

- Decidir nicho/produto (critério na seção "Decisões pendentes").
- Chave Pexels (grátis) ou fotos do produto como material do nicho.
