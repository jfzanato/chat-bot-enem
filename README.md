# Enem com você

Protótipo de chatbot com o mascote da Unidade Regional de Ensino de Jaú. HTML, CSS e JavaScript puros, sem compilação, backend ou API de IA. A imagem fornecida foi preservada em `assets/ajudante.jpg`.

## Abrir localmente

Na pasta do projeto, execute:

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Acesse http://127.0.0.1:8080. Para encerrar, pressione Ctrl+C no terminal. Abrir o HTML por duplo clique não é suficiente: o navegador costuma bloquear a leitura do JSON pelo protocolo `file://`.

## Publicar

Envie `index.html`, `styles.css`, `app.js`, `assets/` e `data/` para uma hospedagem estática HTTPS, preservando a estrutura. Não precisa de banco de dados nem servidor de aplicação. Nenhum serviço de hospedagem foi configurado por este protótipo. As fontes tipográficas usam Google Fonts; se não houver internet, a interface usa Arial.

## Como o chat funciona

- Assuntos levam a perguntas fechadas. Cada botão exibe literalmente a resposta cadastrada no JSON.
- O campo de busca normaliza acentos e procura palavras nas perguntas e palavras-chave. Ele sempre pede que o estudante selecione uma pergunta; não interpreta uma pergunta livre como uma autorização para responder automaticamente.
- Perguntas sem correspondência recebem uma mensagem fixa de ausência de conteúdo. Uma sugestão de busca não significa que a pergunta do estudante tenha sido compreendida.
- Não há geração de texto, consulta automática à web, cadastro de estudantes ou persistência da conversa. A pesquisa digitada não sai do navegador. Links oficiais e Google Fonts fazem suas próprias requisições quando acessados/carregados.
- Conteúdo é inserido como texto, sem executar HTML vindo da busca ou da base.
- A base falha de forma fechada se faltar, estiver inválida ou ultrapassar a validade. A validade é conferida no fuso de São Paulo, usando a data do dispositivo; não substitui manutenção editorial.

## Conteúdo e manutenção

As 26 perguntas cobrem datas, horários, documentos, caneta, lanche, celular, saída, provas, redação, inscrição, atendimento e usos da nota. Pesquisa em fontes públicas do Inep realizada em **04/11/2026**. As respostas são resumos, não transcrições integrais nem atendimento individual. O edital e suas retificações prevalecem. O chat não é um canal oficial do Inep.

Edite `data/perguntas.json` para atualizar o conteúdo. Cada pergunta tem `id` único, `category`, `question`, `answer`, `keywords` e `source` correspondente ao catálogo `sources`. Todas as falas do ajudante relacionadas à consulta ficam nesse arquivo; mensagens operacionais de erro ficam no JavaScript.

Antes de outra edição, confira cada fonte, atualize perguntas, prazos, `edition`, `reviewedAt` e `validUntil`, além das referências visuais a 2026 no HTML. A validade atual termina em 31/12/2026; não a prorrogue sem revisar o conteúdo. Dúvidas não cobertas devem receber uma nova resposta editorial com fonte antes de entrarem no chat.

## Fontes consultadas

- [Cronograma 2026](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem/orientacoes/cronograma)
- [Horários, estrutura e documentos](https://www.gov.br/inep/pt-br/centrais-de-conteudo/noticias/enem/enem-2026-falta-um-mes-para-o-primeiro-dia-de-provas)
- [Obrigações do participante](https://www.gov.br/inep/pt-br/acesso-a-informacao/perguntas-frequentes/exame-nacional-do-ensino-medio-enem/no-dia-do-exame-orientacoes/obrigacoes-do-participante-do-enem)
- [Redação 2026](https://www.gov.br/inep/pt-br/centrais-de-conteudo/noticias/enem/enem-2026-cartilha-da-redacao-esta-disponivel)
- [Perguntas frequentes](https://www.gov.br/inep/pt-br/acesso-a-informacao/perguntas-frequentes/exame-nacional-do-ensino-medio-enem/)
- [Apresentação do exame](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem/)
