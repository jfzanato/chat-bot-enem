"""Gera o chat independente a partir da base local, sem alterar o site principal."""
import base64
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'data/perguntas.json').read_text(encoding='utf-8'))
image = base64.b64encode((ROOT / 'assets/ajudante.jpg').read_bytes()).decode('ascii')
data['documentBase64'] = base64.b64encode((ROOT / 'data/fontes/faq-saresp-2026.docx').read_bytes()).decode('ascii')
payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')

template = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chat SARESP 2026</title>
</head>
<body>
<!-- Para editores que permitem scripts, copie o bloco abaixo até seu fechamento. -->
<section data-saresp-chat aria-label="Chat de dúvidas do SARESP 2026">
<style>
[data-saresp-chat]{--sc-blue:#0b3b60;--sc-line:#d2deeb;box-sizing:border-box;display:flex;flex-direction:column;width:100%;max-width:700px;height:720px;height:min(780px,100dvh);min-height:420px;margin:0 auto;border:1px solid var(--sc-line);border-radius:18px;overflow:hidden;background:#fff;color:#1a2c3f;font:14px/1.6 Arial,sans-serif;text-align:left;isolation:isolate;color-scheme:light}
[data-saresp-chat] *{box-sizing:border-box}
[data-saresp-chat] button,[data-saresp-chat] input{font:inherit}
[data-saresp-chat] button{cursor:pointer}
[data-saresp-chat] button:focus-visible,[data-saresp-chat] input:focus-visible,[data-saresp-chat] a:focus-visible{outline:3px solid #e08300;outline-offset:2px}
[data-saresp-chat] .sc-header{display:flex;gap:12px;align-items:center;padding:16px;border-bottom:1px solid var(--sc-line);flex-shrink:0}
[data-saresp-chat] .sc-header strong{font-size:17px;display:block;color:var(--sc-blue)}
[data-saresp-chat] .sc-header small{display:block;font-size:11px;color:#56697a}
[data-saresp-chat] .sc-avatar{display:block;position:relative;overflow:hidden;width:42px;height:42px;border-radius:50%;background:#f1ecdf;flex-shrink:0}
[data-saresp-chat] .sc-avatar img{position:absolute;width:156px;height:104px;max-width:none;left:-54px;top:-5px;mix-blend-mode:multiply}
[data-saresp-chat] .sc-reset{margin-left:auto;background:#fff;color:var(--sc-blue);border:1px solid var(--sc-line);border-radius:8px;min-width:38px;min-height:38px;font-size:23px}
[data-saresp-chat] .sc-log{padding:18px 14px;overflow-y:auto;flex:1;min-height:0;overscroll-behavior:contain;scrollbar-width:thin}
[data-saresp-chat] .sc-message{display:flex;align-items:flex-start;gap:8px;margin-bottom:16px}
[data-saresp-chat] .sc-message .sc-avatar{width:28px;height:28px}
[data-saresp-chat] .sc-message .sc-avatar img{width:108px;height:72px;left:-38px;top:-3px}
[data-saresp-chat] .sc-bubble{min-width:0;max-width:100%;padding:13px 15px;background:#edf3f8;border-radius:3px 14px 14px;white-space:pre-line;overflow-wrap:anywhere}
[data-saresp-chat] .sc-user{justify-content:flex-end}
[data-saresp-chat] .sc-user .sc-bubble{background:var(--sc-blue);color:white;border-radius:14px 3px 14px 14px;max-width:88%}
[data-saresp-chat] .sc-choices{display:flex;gap:7px;flex-wrap:wrap;margin-top:12px;white-space:normal}
[data-saresp-chat] .sc-choice{background:#fff;border:1px solid #c9d8e7;border-radius:9px;color:var(--sc-blue);padding:9px 11px;font-size:12px;line-height:1.5;text-align:left;max-width:100%;overflow-wrap:anywhere}
[data-saresp-chat] .sc-choice:hover{background:#dfebf6}
[data-saresp-chat] .sc-question{width:100%}
[data-saresp-chat] .sc-reference{font-size:11px;color:#56697a;border-top:1px solid var(--sc-line);margin-top:12px;padding-top:8px;white-space:normal}
[data-saresp-chat] .sc-form{display:flex;align-items:center;gap:8px;padding:12px;border-top:1px solid var(--sc-line);flex-shrink:0}
[data-saresp-chat] .sc-field{display:block;min-width:0;flex:1}
[data-saresp-chat] input{width:100%;min-width:0;background:#fafcfe;color:#1a2c3f;border:1px solid #c9d8e7;border-radius:9px;padding:11px;font-size:13px}
[data-saresp-chat] .sc-send{padding:10px 13px;border:0;border-radius:9px;background:var(--sc-blue);color:#fff;font-size:13px}
[data-saresp-chat] .sc-footer{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:0 12px 10px;font-size:10px;color:#56697a;flex-shrink:0}
[data-saresp-chat] .sc-link{background:none;border:0;text-decoration:underline;color:var(--sc-blue);padding:4px;font-size:12px}
[data-saresp-chat] .sc-source{padding:12px 16px;overflow-y:auto;max-height:45%;font-size:12px;background:#f6f9fc;border-top:1px solid var(--sc-line);flex-shrink:0}
[data-saresp-chat] .sc-source[hidden]{display:none}
[data-saresp-chat] .sc-source p{margin:0 0 10px}
[data-saresp-chat] .sc-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}
[data-saresp-chat] button:disabled,[data-saresp-chat] input:disabled{opacity:.6;cursor:default}
@media(max-width:420px){[data-saresp-chat]{border-radius:10px;font-size:13px}[data-saresp-chat] .sc-header{padding:12px}[data-saresp-chat] .sc-header strong{font-size:15px}[data-saresp-chat] .sc-bubble{padding:11px}[data-saresp-chat] .sc-log{padding:14px 9px}}
</style>
<header class="sc-header">
<span class="sc-avatar"><img src="data:image/jpeg;base64,__IMAGE__" alt="Mascote da Unidade Regional de Ensino de Jaú"></span>
<div><strong>SARESP com você</strong><small>FAQ do Manual de Orientação · 2026</small></div>
<button type="button" class="sc-reset" aria-label="Recomeçar conversa">↻</button>
</header>
<div class="sc-log" role="log" aria-label="Conversa com o ajudante" aria-live="polite" aria-relevant="additions">
Carregando as perguntas. Se elas não aparecerem, verifique se o editor permite JavaScript ou incorpore este arquivo por iframe.
</div>
<form class="sc-form" role="search">
<label class="sc-field"><span class="sc-sr">Buscar uma pergunta cadastrada</span><input type="text" maxlength="160" placeholder="Digite uma dúvida. Ex.: horários" autocomplete="off" disabled></label>
<button class="sc-send" type="submit" disabled>Buscar</button>
</form>
<footer class="sc-footer"><span>Respostas fixas do documento fornecido.<br>Guia de apoio; não é um canal oficial.</span><button type="button" class="sc-link sc-toggle" aria-expanded="false">Ver fonte</button></footer>
<div class="sc-source" hidden>
<p><strong>FAQ do Manual de Orientação do SARESP 2026</strong></p>
<p>As 26 perguntas e respostas reproduzem o Word fornecido. Cada resposta indica seu número no FAQ. Não há geração de respostas por IA nem consulta automática à internet.</p>
<p class="sc-review"></p>
<button type="button" class="sc-link sc-download">Baixar documento-fonte (.docx)</button>
<p>O manual oficial e as orientações atualizadas da SEDUC/SP e da VUNESP prevalecem.</p>
</div>
<noscript>Ative o JavaScript para usar este chat.</noscript>
<script type="application/json" class="sc-data">__DATA__</script>
<script>
(() => {
  'use strict';
  const root = document.currentScript.closest('[data-saresp-chat]');
  const find = selector => root.querySelector(selector);
  const log = find('.sc-log');
  const input = find('input');
  const base = JSON.parse(find('.sc-data').textContent);
  const normalize = text => text.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase().replace(/[^a-z0-9\\s]/g,' ').replace(/\\s+/g,' ').trim();
  const stop = new Set(['que','qual','como','posso','para','uma','saresp','enem','quero','sobre','das','dos','tem','sao','com','por','nao']);
  function message(text,user=false) {
    const row = document.createElement('div'); row.className = 'sc-message' + (user?' sc-user':'');
    if (!user) {
      const avatar = find('.sc-header .sc-avatar').cloneNode(true);
      avatar.querySelector('img').alt = ''; row.append(avatar);
    }
    const bubble = document.createElement('div'); bubble.className='sc-bubble'; bubble.textContent=text;
    row.append(bubble); log.append(row); return bubble;
  }
  function choices(bubble,items) {
    const group = document.createElement('div'); group.className='sc-choices';
    items.forEach(item=>{
      const button=document.createElement('button'); button.type='button'; button.className='sc-choice'+(item.full?' sc-question':'');
      button.textContent=item.label; button.addEventListener('click',item.action); group.append(button);
    });
    bubble.append(group); log.scrollTop=log.scrollHeight;
  }
  function menu() {
    choices(message(base.messages.menu),base.categories.map(category=>({label:category.label,action:()=>categoryMenu(category.id)})));
  }
  function categoryMenu(id) {
    message(base.categories.find(item=>item.id===id).label,true);
    choices(message(base.messages.choose),base.questions.filter(item=>item.category===id).map(item=>({label:item.question,full:true,action:()=>answer(item.id)})));
  }
  function answer(id) {
    const item=base.questions.find(entry=>entry.id===id); if(!item)return;
    message(item.question,true); const bubble=message(item.answer);
    const reference=document.createElement('div'); reference.className='sc-reference';
    reference.textContent='Fonte: '+item.sourceItem+' · FAQ do Manual de Orientação do SARESP 2026'; bubble.append(reference);
    choices(bubble,[{label:'Ver outra dúvida',action:menu}]);
  }
  function restart() { log.replaceChildren(); input.value=''; message(base.messages.welcome); menu(); }
  const today = new Intl.DateTimeFormat('sv-SE',{timeZone:'America/Sao_Paulo'}).format(new Date());
  const expired = today>base.validUntil;
  find('.sc-review').textContent='Importado em '+base.reviewedAt.split('-').reverse().join('/')+'. Base da edição 2026. Validade técnica até '+base.validUntil.split('-').reverse().join('/')+'; consulte orientações atualizadas.';
  find('.sc-reset').addEventListener('click',()=>{if(!expired)restart();});
  find('.sc-toggle').addEventListener('click',()=>{
    const panel=find('.sc-source'); panel.hidden=!panel.hidden;
    find('.sc-toggle').setAttribute('aria-expanded',String(!panel.hidden));
  });
  find('.sc-download').addEventListener('click',()=>{
    const bytes=Uint8Array.from(atob(base.documentBase64),char=>char.charCodeAt(0));
    const url=URL.createObjectURL(new Blob([bytes],{type:'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}));
    const link=document.createElement('a'); link.href=url; link.download='FAQ do Manual de Orientação do SARESP 2026.docx';
    root.append(link); link.click(); link.remove(); setTimeout(()=>URL.revokeObjectURL(url),30000);
  });
  find('.sc-form').addEventListener('submit',event=>{
    event.preventDefault(); const text=input.value.trim(); if(expired||!text)return;
    input.value=''; message(text,true);
    const terms=[...new Set(normalize(text).split(' ').filter(term=>term.length>2&&!stop.has(term)))];
    const results=base.questions.map(item=>{
      const words=normalize(item.question+' '+item.keywords.join(' ')).split(' ');
      return {item,score:terms.filter(term=>words.some(word=>word===term||(term.length>=4&&word.startsWith(term)))).length};
    }).filter(result=>result.score>0).sort((a,b)=>b.score-a.score).slice(0,5).map(result=>result.item);
    const bubble=message(results.length?base.messages.results:'Não tenho uma resposta cadastrada para essa dúvida no documento fornecido. Escolha outro assunto ou consulte o FAQ em Ver fonte.');
    choices(bubble,[...results.map(item=>({label:item.question,full:true,action:()=>answer(item.id)})),{label:'Ver todos os assuntos',action:menu}]);
  });
  if(expired){log.replaceChildren(); message('Esta base do SARESP 2026 precisa de revisão antes de novas consultas. Consulte as orientações atuais da SEDUC/SP.');find('.sc-reset').disabled=true;}
  else {input.disabled=false;find('.sc-send').disabled=false;restart();}
})();
</script>
</section>
<!-- Fim do bloco do chat. -->
</body>
</html>
'''
template = template.replace('[data-saresp-chat]', '#saresp-chat')
template = template.replace('<section data-saresp-chat aria-label="Chat de dúvidas do SARESP 2026">', '<div id="saresp-chat">')
template = template.replace('</section>', '</div>')
template = template.replace('<header class="sc-header">', '<div class="sc-header">').replace('</header>', '</div>')
template = template.replace('<footer class="sc-footer">', '<div class="sc-footer">').replace('</footer>', '</div>')
template = template.replace('<script type="application/json" class="sc-data">__DATA__</script>', '')
template = template.replace("const root = document.currentScript.closest('#saresp-chat');", "const root = document.getElementById('saresp-chat');")
template = template.replace("const base = JSON.parse(find('.sc-data').textContent);", 'const base = __DATA__;')
template = template.replace('<!-- Para editores que permitem scripts, copie o bloco abaixo até seu fechamento. -->', '<!-- Chat em HTML e JavaScript comuns. -->')
out = ROOT / 'chat-saresp.html'
out.write_text(template.replace('__IMAGE__', image).replace('__DATA__', payload), encoding='utf-8')
print(f'Gerado: {out.name} ({out.stat().st_size:,} bytes), {len(data["questions"])} perguntas.')
