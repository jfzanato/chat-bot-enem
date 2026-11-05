# SARESP 2026 · Manual de Orientação

Chatbot interativo com o mascote da Unidade Regional de Ensino de Jaú, baseado nos documentos fornecidos **FAQ do Manual de Orientação do SARESP 2026 (1).docx** e **FAQ_SARESP Digital.docx**.

Construído em HTML, CSS e JavaScript puros, sem compilação ou IA generativa. A base contém 55 perguntas: 26 originais preservadas e 29 adicionais do FAQ SARESP Digital. As perguntas e respostas foram conferidas com os documentos enviados. A importação preserva o texto e as quebras entre parágrafos, sem reproduzir a formatação do Word. Não houve complementação ou validação por pesquisa externa.

## Abrir localmente

Na pasta do projeto, execute:

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Acesse [http://127.0.0.1:8080](http://127.0.0.1:8080).

## Como o chat funciona

- **Temas e categorias:** os botões levam às perguntas do documento. Cada resposta é apresentada na íntegra e identifica sua origem: P1 a P26 no FAQ original ou a linha da tabela do FAQ digital.
- **Busca por palavra-chave:** o campo de busca normaliza acentos e procura termos nas perguntas e nas palavras-chave cadastradas no JSON.
- **Mascote interativo animado:** usa GIF com transparência nativa e mantém apenas a animação do arquivo, sem efeitos adicionais de salto. Ao clicar, o balão apresenta uma mensagem de incentivo.
- **Acessibilidade e segurança:** todo o conteúdo é inserido de maneira segura como texto, respeitando acessibilidade (`prefers-reduced-motion`) e validações de integridade.

## Conteúdo e seções cobertas (55 perguntas)

1. Visão Geral e Apresentação do SARESP 2026 (P1 a P3)
2. Diretrizes de Aplicação e Regras de Regência (P4 a P6)
3. Atendimento Especializado e Nome Social (P7 e P8)
4. Cronograma, Horários e Duração das Provas (P9 a P11)
5. Estrutura dos Cadernos de Prova e Componentes Curriculares (P12 a P14)
6. Instrumentos de Orientação e Controle Administrativo (P15 e P16)
7. Atribuições das Equipes - Central, Regional e Local (P17 a P20)
8. Logística, Segurança e Devolução dos Materiais (P21 a P23)
9. Processamento dos Resultados, Divulgação e Ajuda de Custo (P24 e P25)
10. Canais de Suporte e Comunicação (P26)
11. SARESP digital (29 perguntas adicionais, IDs digital-01 a digital-29)

## Fonte e atualização

Cópias dos documentos recebidos estão em `data/fontes/faq-saresp-2026.docx` e `data/fontes/faq-saresp-digital.docx`, disponíveis para download em “Ver fontes” e nas respostas. Os links gerais da SEDUC/SP e da VUNESP não são usados como evidência das respostas.

A base está em `data/perguntas.json`. Cada pergunta tem `sourceItem` (número no FAQ) e `sourceSection` (seção de origem). O FAQ original foi importado em 04/11/2026, e o FAQ digital foi acrescentado em 05/11/2026. A diferença de escopo do público-alvo entre os documentos foi confirmada pelo responsável pelo conteúdo. A validade técnica configurada até 31/12/2027 é um bloqueio de manutenção, não uma garantia de que prazos e orientações permanecerão atualizados.

O item P13 do documento declara 48 itens no primeiro dia, mas a discriminação apresentada (18 + 6 + 18, para a 3ª série) soma 42. Essa divergência foi preservada; corrigir a resposta exige uma fonte corrigida ou orientação explícita do responsável pelo conteúdo.

O backup original do Enem permanece em `backups/original-20261104-113933/perguntas.json`. Uma segunda cópia, anterior à importação deste documento, preserva a adaptação do SARESP que já existia no projeto em `backups/antes-importacao-documento-20261104-114157/`.

Para hospedar, mantenha `index.html`, `styles.css`, `app.js`, `assets/` e `data/` juntos em uma hospedagem estática. O documento-fonte também ficará disponível aos visitantes. Não envie a pasta `backups/`, que contém versões antigas. A página completa está publicada na Vercel e o código está no GitHub. O pacote `saresp-cloudflare.zip` e a pasta `deploy-cloudflare/` são exportações locais anteriores à inclusão das perguntas digitais; devem ser gerados novamente antes de uma futura publicação no Cloudflare.
