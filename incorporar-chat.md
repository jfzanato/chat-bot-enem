# Incorporar o chat em um editor WYSIWYG

O arquivo `chat-saresp.html` contém somente o chat. Imagem, estilos, JavaScript, as 26 perguntas e respostas e o documento-fonte estão incorporados no mesmo HTML. Funciona por duplo clique, sem servidor, API, bibliotecas externas ou leitura de JSON por rede. É uma cópia independente da base atual: futuras alterações no JSON do site não aparecem automaticamente neste arquivo.

## Opção recomendada com iframe

Hospede o arquivo HTML em um endereço HTTPS e use o modo HTML ou bloco de incorporação do editor para inserir:

```html
<iframe
  src="https://SEU-DOMINIO/chat-saresp.html"
  title="Chat de dúvidas do SARESP 2026"
  width="100%"
  height="780"
  style="display:block;max-width:700px;border:0;margin:0 auto"
  loading="lazy">
</iframe>
```

Substitua o endereço pelo local real de hospedagem. O endereço `127.0.0.1` serve apenas para testes neste computador. O editor precisa permitir iframe, e a hospedagem precisa permitir a incorporação na página de destino. O HTML tem de ser servido como página, não como anexo para download. Uma política CSP que proíba scripts inline também impedirá o funcionamento.

Se a plataforma exigir `sandbox`, habilite `allow-scripts allow-downloads` para permitir a conversa e o download do documento. Não é necessário habilitar `allow-same-origin` para este chat. O botão de download depende também das permissões do navegador e da plataforma.

## Inserção direta do código

Se o editor permitir `<style>` e `<script>`, copie o bloco `<div id="saresp-chat">...</div>` completo, incluindo o script interno, para o modo de código HTML. Os estilos e os seletores JavaScript estão limitados ao componente para reduzir conflitos com a página de destino. Estilos globais da página ainda podem afetar elementos; iframe oferece isolamento mais completo.

Alguns editores removem scripts ao salvar, ou inserem HTML sem executar scripts. Nesses casos, colar o código diretamente não basta. Use o iframe ou um bloco próprio de código autorizado pela plataforma. Confira o funcionamento na página publicada, pois a prévia de edição pode bloquear scripts.

## Atualizar o arquivo independente

Após revisar `data/perguntas.json`, gere novamente o HTML:

```powershell
python scripts/build-chat-standalone.py
```

O site principal não é alterado pelo gerador. A validade da base e as referências P1–P26 são preservadas. O documento-fonte está incluído para download; o conteúdo dele ficará disponível a quem receber o HTML. As respostas reproduzem o documento fornecido, incluindo a divergência numérica já identificada no P13.
