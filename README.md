# SARESP 2026 · Manual de Orientação

Chatbot interativo com o mascote da Unidade Regional de Ensino de Jaú, adaptado para as diretrizes do **Manual de Orientação do SARESP 2026** (28ª edição), elaborado pela **Secretaria da Educação do Estado de São Paulo (SEDUC/SP)** em parceria com a **Fundação VUNESP**.

Construído em HTML, CSS e JavaScript puros, sem compilação, sem backend complexo e sem IA generativa: todas as respostas são fiéis ao documento oficial.

## Abrir localmente

Na pasta do projeto, execute:

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Acesse [http://127.0.0.1:8080](http://127.0.0.1:8080).

## Como o chat funciona

- **Temas e categorias:** os botões levam diretamente às perguntas do Manual. Cada resposta é apresentada na íntegra de acordo com o FAQ oficial.
- **Busca por palavra-chave:** o campo de busca normaliza acentos e procura termos nas perguntas e nas palavras-chave cadastradas no JSON.
- **Mascote interativo animado:** possui animação contínua de flutuação e reage com incentivos e comemoração ao clique.
- **Acessibilidade e segurança:** todo o conteúdo é inserido de maneira segura como texto, respeitando acessibilidade (`prefers-reduced-motion`) e validações de integridade.

## Conteúdo e seções cobertas (26 perguntas do FAQ)

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

## Fontes Oficiais

- [SEDUC/SP - Secretaria da Educação do Estado de São Paulo](https://www.educacao.sp.gov.br)
- [Fundação VUNESP](https://www.vunesp.com.br)
