# How-to — o que só o Diego faz antes da sessão de execução (2026-09-04)

Complementa `do-balcao/2026-09-03-teste-tiktok-faceless.md`. Passos verificados em 04/09 contra
as fontes oficiais listadas no fim; nomes de menu podem variar com versão do app — quando não
achar, use a busca dentro de Configurações.

## Por que é você, e não o agente

| Motivo | Itens |
|---|---|
| Identidade (CPF, telefone, documento, aceite de termos, dados bancários) | Shopee Afiliados, Hotmart, criar contas TikTok, verificação do TikTok Shop |
| App logado no celular (sessão do Claude não tem browser) | tela do TikTok Shop, comissão real na Shopee, espionagem no For You |
| Comportamento humano (automatizar é exatamente o que o TikTok pune) | aquecer as contas |

Tudo que não está nesta lista o agente faz: shortlist de SKUs, BGM CC0, roteiros, `run_batch.py`,
pré-corte 9:16, experimentos. Fotos dos produtos: mande os links, o agente tenta baixar.

## Ordem e tempo

| Quando | Bloco | Tempo |
|---|---|---|
| Hoje | 1 e-mails · 2 contas TikTok · 3 tela do Shop · 4 Shopee · 5 Hotmart | ~60 min |
| Todo dia até a sessão | 6 aquecer + espionar (é a mesma atividade) | 10–15 min por conta |
| Quando a Shopee aprovar (2–5 dias úteis) | 7 SKUs · 8 links · 9 devolutiva | ~30 min |

---

## 1. Dois e-mails novos (5 min)

- Crie 2 Gmails, um por nicho. Sugestão de padrão: `<nome-da-conta>.tiktok@gmail.com`.
- Não use o número de telefone no cadastro do TikTok; entre por e-mail. O TikTok só aceita um
  telefone por conta e você vai querer o número livre para a verificação do Shop.
- Guarde login e senha no gerenciador de senhas. Duas contas no mesmo celular ficam vinculadas
  entre si (aceito no brief), mas não podem compartilhar e-mail.

## 2. Duas contas TikTok business (15 min)

Repita para cada nicho:

1. App TikTok → **Cadastrar** → **Usar e-mail** → o Gmail do nicho. Data de nascimento real
   (precisa de 18+ para o Shop e para afiliados).
2. Nome de usuário: sem "IA", sem "oficial", sem nome de marca. Curto e do nicho
   (ex.: nicho A algo com "40+", "pele", "rotina"; nicho B algo com "casa", "organiza").
3. **Perfil → ☰ (canto superior direito) → Configurações e privacidade → Conta → Mudar para
   Conta Business**. Escolha a categoria (A: Beleza/Cuidados pessoais; B: Casa/Decoração).
   É reversível pelo mesmo caminho.
4. **Perfil → Editar perfil**: foto (imagem do nicho, não rosto seu), bio de 1 linha com a
   promessa do nicho. O campo **Website** aparece na conta business sem mínimo de seguidores;
   deixe vazio por enquanto (entra o link da Shopee quando aprovar).
5. Não poste nada ainda.

Regra de saúde da conta (podcast, relato): 5 contas por CPF no Shop; violação derruba score.
Não crie mais que essas 2.

## 3. Tela do TikTok Shop para criadores (5 min, decide o desenho do teste)

Em cada conta: **Perfil → ☰ → Ferramentas do criador** (em algumas versões: **TikTok Studio**)
**→ TikTok Shop para criadores**.

Anote o que a tela mostra. Só existem três resultados:

| A tela mostra | O que fazer |
|---|---|
| Botão **Solicitar/Inscrever-se** disponível com 0 seguidores | Solicite. Verificação de identidade: RG ou CNH, foto com boa luz. Se aprovar, o link do produto vai no vídeo, não na bio → o agente revisita "conta business vs pessoal" (brief, "Decisões a revisitar"). |
| "Você precisa de **N** seguidores" | Anote N. É o piso real desta conta (o brief diz que aparece 1.000 ou 5.000). O teste mede quantos vídeos até N. |
| Opção não aparece | Atualize o app. Se seguir sem aparecer, tire print e mande. |

Tire print da tela em cada conta. Isso vira dado no `experiments/`.

## 4. Shopee Afiliados (10 min + espera de 2–5 dias úteis)

Precisa: conta de comprador na Shopee, CPF, telefone, e um canal público **com conteúdo**.
**Não cadastre as contas TikTok novas** — perfil vazio é o motivo nº 1 de rejeição. Use o seu
canal existente que tenha posts (Instagram, YouTube ou outro); depois de aprovado dá para
adicionar canais.

1. Navegador: **affiliate.shopee.com.br** (ou app Shopee → **Eu → Programa de Afiliados**).
2. Preencha nome, e-mail, telefone, CPF, canais de divulgação (link do canal com conteúdo).
3. Chega um código por e-mail: **digite na hora**, expira rápido.
4. Aguarde o e-mail de aprovação. Fontes divergem: 24–48h a 3–5 dias úteis.
5. Pagamento: mínimo R$30 acumulado, PF recebe via ShopeePay até o dia 10. Comissão só sobre o
   produto (sem frete), paga após entrega.

## 5. Hotmart (10 min, link sai no mesmo dia)

1. **app.hotmart.com** → criar conta → escolha **"Quero vender como Afiliado"**.
2. Complete: CPF, dados bancários (para receber), foto de perfil.
3. Menu lateral **Produtos → Afiliar-se a um produto**. Filtre categoria Saúde/Beleza.
   Procure 1–2 produtos para o nicho 40+ (menopausa, sono, pele, colágeno) com selo de
   **afiliação automática** → botão **"Afilie-se agora"** (aprova na hora).
   Evite os de **"Solicitar afiliação"** (moderada, o produtor analisa).
4. Depois de afiliar, copie o **link de divulgação (Hotlink)**. Status das solicitações fica em
   **Produtos → Meus produtos → Sou Afiliado(a) → Solicitadas**.
5. Anote nome, preço, comissão e link de cada produto para a devolutiva (item 9).

Lembrete do brief: Hotmart só via link na bio, o TikTok Shop proíbe produto digital.

## 6. Aquecer e espionar ao mesmo tempo (10–15 min/dia por conta, todo dia até a sessão)

Faça como pessoa, não como script: no celular, pelo app, em horários normais. Não faça 100
ações em 2 minutos.

**Aquecimento (cada conta, só no próprio nicho):**

- Busque 2–3 termos do nicho (A: "sérum retinol", "colágeno 40 anos", "pele madura";
  B: "organização de casa", "satisfying organização", "garrafa térmica").
- Assista 10–15 vídeos **até o fim**. Curta os bons. Salve 3–5. Siga 5–10 contas do nicho.
  Comente em 1–2 (comentário real, uma frase).
- Não poste. Não siga fora do nicho. O For You da conta precisa "aprender" o nicho.

**Espionagem (mesma sessão, quando aparecer vídeo do produto/nicho com >100k views):**

1. Toque em **Compartilhar → Copiar link**.
2. Anote no bloco de notas do celular, um bloco por vídeo:

```
link:
views:
produto:
hook (primeiras 2–3 s, transcrito literal):
estrutura (o que acontece em ordem, 1 linha por bloco):
formato (mãos+produto / foto / texto na tela / voz):
por que segurou (1 frase):
```

3. Meta: **2–3 vídeos por nicho**. Melhor 3 hooks bons que 10 links sem hook.
4. Bônus: na busca do TikTok, digite **Creator Search Insights** → mostra buscas em alta por
   tópico. Anote 2–3 termos do nicho que estão em alta.

Ao final, mande o texto (ou cole em `batch/<nicho>/espionagem.md` no repo). O agente modela os
roteiros em cima disso.

## 7. SKUs com comissão confirmada (quando a Shopee aprovar, 15 min)

O agente entrega uma shortlist de candidatos por nicho. Sua parte é confirmar a comissão real:

1. Painel **affiliate.shopee.com.br** → busque o produto (ou aba **Ofertas** / campanhas com
   comissão extra).
2. Confira a **taxa de comissão** exibida. Critério do brief: **≥15%** em 1 SKU por nicho.
   Segundo SKU pode ser o de impulso (R$30–60, comissão baixa, muitos vendidos) para testar a
   tese do volume.
3. Confira no produto: loja com reputação, estoque, número de vendidos, avaliações, fotos
   oficiais nítidas em fundo limpo.
4. Nicho A: nada de emagrecedor, detox, "trata ou cura". Suplemento comum é categoria aberta.

Anote por SKU: nome, link da página do produto, preço, comissão %, loja.

## 8. Links de afiliado e bio (5 min)

1. No painel de afiliados, gere o **link** do SKU principal de cada nicho.
2. TikTok: **Perfil → Editar perfil → Website** → cole o link. Uma bio comporta um link:
   coloque o SKU principal; Hotmart entra depois se o nicho A sobreviver.
3. Teste o link do próprio celular antes de postar.

## 9. Devolutiva para o agente (o que colar de volta na sessão)

```
TikTok Shop — conta A: [print/resultado]   conta B: [print/resultado]
Shopee: aprovado em __/__ (ou pendente)
Hotmart: produto(s) + link(s)
SKUs nicho A: nome | link | preço | comissão | loja   (1–2)
SKUs nicho B: nome | link | preço | comissão | loja   (1–2)
Espionagem: blocos do item 6 (2–3 por nicho)
Creator Search Insights: termos em alta por nicho
Bio: link colado? sim/não
```

Com isso na mão a sessão de execução sai com os 10 vídeos + captions + experimentos.

## Fontes (verificadas 04/09/2026)

- Termos Shopee Afiliados: https://help.shopee.com.br/portal/10/article/124094
- Comissão e pagamento Shopee: https://shopee.com.br/blog/afiliado-shopee-comissao-pagamentos/
- Cadastro Shopee (terceiros, 2026): https://jefersonsouza.com.br/afiliados/como-ser-afiliado-shopee-em-2026-passo-a-passo-para-comecar/
- Hotmart afiliar-se: https://help.hotmart.com/pt-br/article/215829028/como-me-afiliar-a-um-produto-na-hotmart-
- TikTok Shop BR piloto: https://seller-br.tiktok.com/university/essay?knowledge_id=2918995033900817
- Business = Commercial Music Library: https://ads.tiktok.com/help/article/how-to-use-the-commercial-music-library
- Caminho "Ferramentas do criador → TikTok Shop para criadores" (terceiros): https://rendagold.com.br/como-se-cadastrar-como-criador-afiliado-no-tiktok-shop-em-2026-transactional-criador-afiliado-tiktokshop-youtube/
- Link na bio em conta business (terceiros): https://stan.store/blog/tiktok-link-bio-requirements-2026-guide/
