import json
SP="/private/tmp/claude-501/-Users-apple-Desktop-stripe-conciliacao/7e6c6c9a-350a-44b9-bedd-60c2d17fdb42/scratchpad"
DATA=json.dumps(json.load(open(f"{SP}/payload.json")),separators=(',',':'),ensure_ascii=False)

HTML = r'''<meta charset="utf-8"><title>Ruche · Central Financeira</title>
<style>
:root{color-scheme:light;
 --bg:#F4F6F3;--card:#FFF;--sunk:#EDF0EB;--ink:#141D19;--mut:#5C6660;--fnt:#8B948E;
 --ln:#E1E6DF;--ln2:#C9D1C9;--acc:#10715A;--acc2:#0A4C3C;--asf:#E3F0EA;
 --rev:#1baf7a;--exp:#e0574d;--goal:#B7791F;--nt:#93A29B;--plan:#2a78d6;
 --up:#2E7D5B;--ups:#E4F1EA;--dn:#B4472E;--dns:#F6E5DF;--wr:#B7791F;--wrs:#F7EBD6;
 --sh:0 1px 2px rgba(20,29,25,.05),0 8px 24px rgba(20,29,25,.07);
 --redrow:#FBEBE7;--redrow2:#F6E0DA;
 --sf:Georgia,"Times New Roman",serif;--ss:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;--sm:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
 --bg:#0B100E;--card:#141B17;--sunk:#101614;--ink:#E9F0EC;--mut:#93A09A;--fnt:#75817B;--ln:#212B26;--ln2:#2E3A34;--acc:#4FB79C;--acc2:#7ED0B9;--asf:#132420;
 --rev:#22c98d;--exp:#e0574d;--goal:#E0A93F;--nt:#7B877F;--plan:#3987e5;--up:#5BC08C;--ups:#12241A;--dn:#E0705B;--dns:#291410;--wr:#E0A93F;--wrs:#28210F;--redrow:#3A1912;--redrow2:#431E16;--sh:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.4);}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#0B100E;--card:#141B17;--sunk:#101614;--ink:#E9F0EC;--mut:#93A09A;--fnt:#75817B;--ln:#212B26;--ln2:#2E3A34;--acc:#4FB79C;--acc2:#7ED0B9;--asf:#132420;--rev:#22c98d;--exp:#e0574d;--goal:#E0A93F;--nt:#7B877F;--plan:#3987e5;--up:#5BC08C;--ups:#12241A;--dn:#E0705B;--dns:#291410;--wr:#E0A93F;--wrs:#28210F;--redrow:#3A1912;--redrow2:#431E16;--sh:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.4);}
*{box-sizing:border-box}html,body{margin:0;background:var(--bg)}
.w{background:var(--bg);color:var(--ink);font-family:var(--ss);font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased;padding:26px 16px 60px}
.p{max-width:1180px;margin:0 auto}
h1,h2,h3{font-family:var(--sf);font-weight:600;margin:0;text-wrap:balance}
.eb{font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--acc);font-weight:700}
h1{font-size:24px;margin:8px 0 4px}
.flow{font-size:12.5px;color:var(--mut);margin-bottom:12px}.flow b{color:var(--ink)}
.top{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;padding-bottom:12px;border-bottom:2px solid var(--ln2)}
.selrow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:flex-end}
.msel{display:inline-flex;background:var(--sunk);border:1px solid var(--ln2);border-radius:9px;overflow:hidden;flex-wrap:wrap}
.mb{font:600 13px var(--ss);color:var(--mut);background:none;border:0;padding:8px 13px;cursor:pointer}.mb[aria-pressed="true"]{background:var(--acc);color:#fff}
.mb:focus-visible,.tb:focus-visible,button:focus-visible,select:focus-visible,input:focus-visible{outline:2px solid var(--acc);outline-offset:1px}
.esel,.din{font:600 13px var(--ss);color:var(--ink);background:var(--sunk);border:1px solid var(--ln2);border-radius:9px;padding:7px 11px;cursor:pointer}
.din{font-weight:400;padding:6px 8px}
.dirty{font-size:12px;color:var(--wr);font-weight:600;display:none}.dirty.on{display:inline}
.btn{font:600 12.5px var(--ss);color:var(--ink);background:var(--sunk);border:1px solid var(--ln2);border-radius:8px;padding:7px 12px;cursor:pointer}
.tabs{display:inline-flex;background:var(--sunk);border:1px solid var(--ln2);border-radius:10px;overflow-x:auto;margin-top:14px;max-width:100%}.tabs::-webkit-scrollbar{height:0}
.tb{font:600 13.5px var(--ss);color:var(--mut);background:none;border:0;padding:9px 18px;cursor:pointer;white-space:nowrap;flex:0 0 auto}.tb[aria-selected="true"]{background:var(--acc);color:#fff}
.pane[hidden]{display:none}.pane{max-width:100%}
sec{display:block;margin-top:24px}
.sh2{display:flex;align-items:baseline;gap:11px;margin-bottom:4px}.sh2 h2{font-size:19px}.sh2 .r{flex:1;height:1px;background:var(--ln)}
.sub{color:var(--mut);font-size:13px;margin:0 0 12px}
.kg{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:16px}
.k{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:14px;box-shadow:var(--sh);min-width:0}
.k .t{font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);font-weight:700}.k .v{font-family:var(--sf);font-size:26px;line-height:1.05;margin-top:8px;font-variant-numeric:tabular-nums;overflow-wrap:anywhere}.k .s{font-size:11.5px;color:var(--fnt);margin-top:5px}
.pn{background:var(--card);border:1px solid var(--ln);border-radius:14px;padding:18px;box-shadow:var(--sh);margin-top:14px}
.ph{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:flex-start}
.big{font-family:var(--sf);font-size:30px;line-height:1;font-variant-numeric:tabular-nums}
.rt{text-align:right}.rt .v{font-family:var(--sf);font-size:20px;font-variant-numeric:tabular-nums}.rt .l{font-size:11px;color:var(--mut)}
.leg{display:flex;flex-wrap:wrap;gap:13px;margin:11px 0 4px;font-size:12px;color:var(--mut)}.leg span{display:inline-flex;align-items:center;gap:6px}.leg i{width:11px;height:11px;border-radius:3px}.leg i.ln{height:3px;width:15px}
svg{display:block;width:100%;height:auto}.gl{stroke:var(--ln);stroke-width:1}.ax{fill:var(--mut);font-size:10px}.av{fill:var(--fnt);font-size:10px;font-variant-numeric:tabular-nums}.hit{fill:transparent;cursor:crosshair}.hit:hover{fill:var(--ink);opacity:.05}
.foot{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px;padding-top:12px;border-top:1px solid var(--ln)}.foot div{font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--mut);font-weight:700;min-width:0}.foot b{display:block;font-family:var(--sf);font-size:18px;color:var(--ink);margin-top:4px;text-transform:none;letter-spacing:0;font-variant-numeric:tabular-nums}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
.hb{display:grid;gap:8px;margin-top:10px}.hr{display:grid;grid-template-columns:1fr auto;gap:9px;align-items:center;font-size:13px}.hr .tr{grid-column:1/-1;height:9px;background:var(--sunk);border-radius:999px;overflow:hidden}.hr .tr i{display:block;height:100%;border-radius:999px}.hv{font-size:12px;color:var(--mut);font-variant-numeric:tabular-nums}
.txr{display:grid;grid-template-columns:32px 1fr auto;gap:10px;align-items:center;padding:8px 0;border-bottom:1px solid var(--ln);font-size:13px}.txr:last-child{border-bottom:none}.txd{font-size:11px;color:var(--fnt);text-align:center;background:var(--sunk);border-radius:6px;padding:3px 0;font-weight:700}.txn{font-weight:600}.txc{font-size:11px;color:var(--mut)}.txv{font-variant-numeric:tabular-nums;font-weight:600}
.gauge{height:24px;background:var(--sunk);border-radius:8px;position:relative;overflow:hidden;margin-top:10px}.gauge i{display:block;height:100%;border-radius:8px}.gauge .mk{position:absolute;top:-4px;bottom:-4px;width:2px;background:var(--goal)}.gauge .mkl{position:absolute;top:-18px;font-size:10px;color:var(--goal);font-weight:700;transform:translateX(-50%)}
.co{background:var(--asf);border:1px solid var(--ln);border-left:3px solid var(--acc);border-radius:10px;padding:13px 16px;margin-top:13px}.co.r{background:var(--dns);border-left-color:var(--dn)}.co p{margin:0;font-size:13.5px}.co p+p{margin-top:7px}
.stw{overflow-x:auto;border:1px solid var(--ln);border-radius:12px;background:var(--card);box-shadow:var(--sh);margin-top:12px;max-width:100%}
table.st{border-collapse:collapse;width:100%;min-width:640px;font-size:13px}table.st th,table.st td{padding:8px 12px;border-bottom:1px solid var(--ln);text-align:left}table.st thead th{font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);font-weight:700;background:var(--sunk);position:sticky;top:0}table.st td.n,table.st th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}table.st tr.tot td{font-weight:700;background:var(--asf);border-top:1px solid var(--ln2)}table.st tr.sub td{font-weight:600}table.st tr.item td:first-child{padding-left:28px;color:var(--mut)}table.st tr:last-child td{border-bottom:none}
.cd{font-family:var(--sm);font-size:11px;color:var(--fnt);margin-right:6px}.neg{color:var(--dn)}.pos{color:var(--up)}
.natg{display:grid;grid-template-columns:repeat(3,1fr);gap:11px;margin-top:12px}.nat{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:15px;box-shadow:var(--sh);min-width:0}.nat .t{font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);font-weight:700}.nat .v{font-family:var(--sf);font-size:22px;margin-top:7px;font-variant-numeric:tabular-nums}.nat .d{font-size:11px;color:var(--fnt);margin-top:4px;font-variant-numeric:tabular-nums}
.mjlive{display:flex;flex-wrap:wrap;gap:16px;align-items:center;background:var(--card);border:1px solid var(--ln);border-left:3px solid var(--acc);border-radius:12px;padding:13px 16px;box-shadow:var(--sh);margin-top:14px}.mjlive .cell{min-width:0}.mjlive .cell .t{font-size:10px;letter-spacing:.05em;text-transform:uppercase;color:var(--mut);font-weight:700}.mjlive .cell .v{font-family:var(--sf);font-size:20px;font-variant-numeric:tabular-nums;margin-top:3px}.mjlive .hint{font-size:11.5px;color:var(--fnt);margin-left:auto;max-width:240px}
.mjbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:12px}.mjbar input[type=search]{flex:1;min-width:160px;font:13.5px var(--ss);color:var(--ink);background:var(--card);border:1px solid var(--ln2);border-radius:8px;padding:8px 11px}.mjcount{font-size:12px;color:var(--mut);font-variant-numeric:tabular-nums}
.fullw{width:100vw;position:relative;left:50%;right:50%;margin-left:-50vw;margin-right:-50vw;padding:0 16px}
.mjscroll{max-height:74vh;overflow:auto;border:1px solid var(--ln);border-radius:12px;background:var(--card);box-shadow:var(--sh)}
table.mj{border-collapse:collapse;width:100%;font-size:12px}table.mj th,table.mj td{padding:4px 7px;border-bottom:1px solid var(--ln);text-align:left;white-space:nowrap}
table.mj thead th{font-size:9.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--mut);font-weight:700;background:var(--sunk);position:sticky;top:0;z-index:2;cursor:pointer}
table.mj thead tr.filt th{position:sticky;top:24px;background:var(--sunk);padding:3px 5px;cursor:auto}table.mj thead tr.filt input,table.mj thead tr.filt select{width:100%;min-width:64px;font:11px var(--ss);color:var(--ink);background:var(--card);border:1px solid var(--ln2);border-radius:5px;padding:3px 5px}
table.mj td.n{text-align:right;font-variant-numeric:tabular-nums}
table.mj tbody tr:nth-child(even){background:var(--sunk)}
table.mj tbody tr.norec{background:var(--redrow)}table.mj tbody tr.norec:nth-child(even){background:var(--redrow2)}
table.mj tbody tr.sel,table.mj tbody tr.sel:nth-child(even){background:var(--asf)}
table.mj tr.edited td.mark{box-shadow:inset 3px 0 0 var(--acc)}
.accdot{display:inline-block;width:8px;height:8px;border-radius:2px;margin-right:5px;vertical-align:middle}
.pill{display:inline-block;padding:1px 7px;border-radius:10px;font-size:11px;font-weight:700;line-height:1.55;white-space:nowrap}
/* congelar as 3 primeiras colunas (checkbox, Date Added, Name) — estilo Excel */
table.mj th:nth-child(1),table.mj td:nth-child(1){position:sticky;left:0;z-index:1;width:30px;min-width:30px}
table.mj th:nth-child(2),table.mj td:nth-child(2){position:sticky;left:30px;z-index:1;width:92px;min-width:92px}
table.mj th:nth-child(3),table.mj td:nth-child(3){position:sticky;left:122px;z-index:1;min-width:160px}
table.mj thead th:nth-child(1),table.mj thead th:nth-child(2),table.mj thead th:nth-child(3){z-index:4}
table.mj tbody tr td:nth-child(-n+3){background:var(--card)}
table.mj tbody tr:nth-child(even) td:nth-child(-n+3){background:var(--sunk)}
table.mj tbody tr.norec td:nth-child(-n+3){background:var(--redrow)}
table.mj tbody tr.norec:nth-child(even) td:nth-child(-n+3){background:var(--redrow2)}
table.mj tbody tr.sel td:nth-child(-n+3){background:var(--asf)}
table.mj input.ce[type=date]{width:84px;min-width:84px}
table.mj td.e{cursor:pointer}table.mj td.e:hover{background:var(--card);box-shadow:inset 0 0 0 1px var(--ln2)}table.mj td.ntc{max-width:180px;overflow:hidden;text-overflow:ellipsis;color:var(--mut)}
table.mj input.ce,table.mj select.ce{font:12px var(--ss);color:var(--ink);background:var(--card);border:1px solid var(--acc);border-radius:5px;padding:2px 4px;width:100%;min-width:90px}table.mj textarea.ce{font:12px var(--ss);color:var(--ink);background:var(--card);border:1px solid var(--acc);border-radius:5px;padding:4px;width:260px;height:70px}
.fg{display:inline-block;font-size:9px;font-weight:800;padding:1px 4px;border-radius:4px;margin-left:4px;background:var(--wr);color:#fff}.fg.d{background:var(--dn)}.fg.i{background:var(--plan)}
.bulk{display:none;flex-wrap:wrap;gap:8px;align-items:center;background:var(--asf);border:1px solid var(--acc);border-radius:10px;padding:10px 14px;margin-top:10px}.bulk.on{display:flex}.bulk b{color:var(--acc2)}.bulk select,.bulk input{font:13px var(--ss);color:var(--ink);background:var(--card);border:1px solid var(--ln2);border-radius:8px;padding:6px 9px}
.tip{position:fixed;pointer-events:none;z-index:60;background:var(--card);border:1px solid var(--ln2);border-radius:9px;padding:9px 11px;box-shadow:var(--sh);font-size:12px;opacity:0;transition:opacity .1s;min-width:150px}.tip h4{font-size:10.5px;margin:0 0 5px;font-family:var(--ss);letter-spacing:.04em;text-transform:uppercase;color:var(--mut)}.tip .r{display:flex;justify-content:space-between;gap:14px;padding:2px 0}.tip .r b{font-variant-numeric:tabular-nums}
@media(max-width:900px){.kg{grid-template-columns:1fr 1fr}.g2{grid-template-columns:1fr}.foot{grid-template-columns:1fr 1fr}.natg{grid-template-columns:1fr}}
@media(max-width:560px){.kg{grid-template-columns:1fr}h1{font-size:20px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<div class="w"><div class="p">
<div class="top">
  <div><div class="eb">Ruche Digital · Central Financeira</div><h1>Painel financeiro</h1>
    <div class="flow"><b>Master Journal</b> → alimenta → <b>DRE</b> · <b>Fluxo de Caixa</b> · <b>Resumo</b>. Edite o razão e tudo recalcula.</div></div>
  <div>
    <div class="selrow">
      <div class="msel" id="msel" role="group" aria-label="Período"></div>
      <span id="rangebox" style="display:none"><input type="date" id="rstart" class="din" aria-label="De"> <span style="color:var(--mut);font-size:12px">até</span> <input type="date" id="rend" class="din" aria-label="Até"></span>
      <select class="esel" id="esel" aria-label="Empresa" title="Empresa"></select>
    </div>
    <div style="margin-top:8px;display:flex;gap:8px;justify-content:flex-end;align-items:center;flex-wrap:wrap">
      <span class="dirty" id="dirty"></span>
      <button class="btn" id="themebtn" title="Alternar tema claro/escuro" aria-label="Tema" style="cursor:pointer">🌙</button>
      <label class="btn" for="impfile" style="cursor:pointer">Importar extratos</label>
      <button class="btn" id="exp">Exportar CSV</button>
      <button class="btn" id="disc" style="display:none">Descartar edições</button>
      <input type="file" id="impfile" accept=".csv,.txt,.xls,.xlsx,text/csv" multiple style="position:absolute;width:1px;height:1px;opacity:0;overflow:hidden">
    </div>
  </div>
</div>
<div class="tabs" role="tablist">
  <button class="tb" role="tab" data-p="resumo" aria-selected="true">Resumo</button>
  <button class="tb" role="tab" data-p="dre" aria-selected="false">DRE</button>
  <button class="tb" role="tab" data-p="fdc" aria-selected="false">Fluxo de Caixa</button>
  <button class="tb" role="tab" data-p="mj" aria-selected="false">Master Journal</button>
</div>

<div class="pane" id="pane-resumo">
  <div class="kg" id="kpis"></div>
  <sec><div class="sh2"><h2>Trajetória do período</h2><div class="r"></div></div><p class="sub">Receita e despesa acumuladas por dia. Calculado do Master Journal.</p>
    <div class="pn"><div class="ph"><div><div class="big" id="t1big"></div><div class="sub" id="t1sub" style="margin:2px 0 0"></div></div><div class="rt"><div class="v" id="t1r"></div><div class="l">receita no período</div></div></div>
      <div class="leg"><span><i class="ln" style="background:var(--rev)"></i>Receita</span><span><i class="ln" style="background:var(--exp)"></i>Despesa</span></div>
      <svg id="c1" viewBox="0 0 1100 280" role="img" aria-label="Trajetória"></svg><div class="foot" id="t1foot"></div></div></sec>
  <div class="g2">
    <div class="pn"><div class="ph"><div><h2 style="font-size:16px">Para onde foi</h2><div class="txc">despesa por categoria</div></div></div><div class="hb" id="cats"></div></div>
    <div class="pn"><div class="ph"><div><h2 style="font-size:16px">De onde veio</h2><div class="txc">receita por natureza</div></div></div><div class="hb" id="mix"></div></div></div>
  <sec><div class="sh2"><h2>Folha contra a meta</h2><div class="r"></div></div><p class="sub">Meta gerencial: 35% do faturamento.</p>
    <div class="pn"><div class="ph"><div><div class="big" id="pgbig"></div><div class="sub" id="pgsub" style="margin:2px 0 0"></div></div><div class="rt"><div class="v" id="pgv"></div><div class="l">folha no período</div></div></div><div class="gauge" id="pgauge"></div></div></sec>
  <sec><div class="sh2"><h2>Maiores saídas</h2><div class="r"></div></div><p class="sub">Acima de US$ 1.500.</p><div class="pn" id="txs"></div></sec>
</div>

<div class="pane" id="pane-dre" hidden>
  <sec><div class="sh2"><h2>Demonstração de Resultado</h2><div class="r"></div></div><p class="sub" id="dresub"></p>
    <div class="stw"><table class="st" id="dret"><thead></thead><tbody></tbody></table></div>
    <div class="co"><p><b>Fora do DRE, por definição:</b> transferências entre contas, empréstimos, aporte, distribuição de lucro e compra de equipamento (famílias 10, 11, 12) — aparecem no Fluxo de Caixa.</p></div></sec>
</div>

<div class="pane" id="pane-fdc" hidden>
  <sec><div class="sh2"><h2>Fluxo de Caixa</h2><div class="r"></div></div><p class="sub" id="fdcsub"></p>
    <div class="natg" id="natg"></div>
    <div class="stw"><table class="st" id="fdct"><thead><tr><th>Conta de caixa</th><th class="n">Entradas</th><th class="n">Saídas</th><th class="n">Líquido</th></tr></thead><tbody></tbody></table></div>
    <div class="co"><p id="transfnote"></p></div></sec>
</div>

<div class="pane" id="pane-mj" hidden>
  <sec><div class="sh2"><h2>Master Journal</h2><div class="r"></div></div>
    <p class="sub">A fonte de tudo. Filtre por qualquer coluna, edite (clique na célula) ou selecione várias linhas para alterar em bloco — DRE e Fluxo de Caixa recalculam. Linhas importadas entram com <b>Reconciled vazio</b> (coluna exclusiva do Patrick), com as datas pela regra de cada banco.</p>
    <div class="mjlive" id="mjlive"></div>
    <div class="mjbar"><input id="mjq" type="search" placeholder="Buscar em tudo (nome, descrição, conta…)" aria-label="Buscar">
      <button class="btn" id="mjf" aria-pressed="false">Só com problema</button>
      <button class="btn" id="mjclr">Limpar filtros</button>
      <span class="mjcount" id="mjn"></span></div>
    <div class="bulk" id="bulk"><b id="bulkn"></b> · alterar <select id="bulkfield"></select> para <span id="bulkvalwrap"></span>
      <button class="btn" id="bulkapply" style="background:var(--acc);color:#fff;border-color:var(--acc)">Aplicar</button>
      <button class="btn" id="bulkclear">Limpar seleção</button></div>
  </sec>
  <div class="fullw"><div class="mjscroll"><table class="mj" id="mjt"><thead></thead><tbody></tbody></table></div></div>
  <div class="co" style="margin:14px 16px 0"><p><b>Marcas:</b> <span class="fg d">DUP</span> possível duplicata · <span class="fg">COMP</span> competência ≠ mês do pagamento · <span class="fg">S/CONTA</span> sem conta · <span class="fg">S/DATA</span> sem data de pagamento · <span class="fg i">IMPORT</span> importada (confira e marque Reconciled). Editar/importar não altera a planilha original — fica neste navegador; use <b>Exportar CSV</b> para levar.</p></div>
</div>
<div class="co" style="margin-top:24px"><p><b>Fonte hoje:</b> planilha auditada (meses 5, 6, 7 e agosto até dia 12). Stripe e Asaas já entram automático; Bank of America e Wise entram em seguida; C6 e Unicred aguardam liberação das APIs. Quando os extratos preencherem esta lista, DRE, Fluxo de Caixa e Resumo continuam saindo do Master Journal.</p></div>
</div></div>
<div id="impmodal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:80;align-items:center;justify-content:center;padding:16px">
 <div style="background:var(--card);border:1px solid var(--ln2);border-radius:14px;max-width:580px;width:100%;padding:20px;box-shadow:var(--sh);color:var(--ink);font-family:var(--ss)">
  <h2 style="font-size:18px;margin-bottom:4px">Importar extrato</h2>
  <p class="sub" id="impinfo" style="margin:0 0 10px"></p>
  <div id="impdet" style="display:none;background:var(--sunk);border:1px solid var(--ln2);border-radius:10px;padding:9px 12px;margin-bottom:10px;font-size:13px"></div>
  <div style="display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:10px">
   <label style="font-size:13px;color:var(--mut)">Conta &nbsp;<select id="impacc" class="din"></select></label>
   <label style="font-size:13px;color:var(--mut)">Moeda &nbsp;<select id="impcur" class="din"><option>BRL</option><option>USD</option></select></label>
  </div>
  <div id="impcard" style="display:none;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:10px">
   <label style="font-size:13px;color:var(--mut)">Vencimento do cartão (Due Date) &nbsp;<input type="date" id="impvenc" class="din"></label>
   <label style="font-size:13px;color:var(--mut)">Pagamento da fatura (Payment Date) &nbsp;<input type="date" id="impfatura" class="din"><span style="font-size:11px;color:var(--fnt);display:block">vazio = fatura ainda não paga</span></label>
  </div>
  <div id="impprevwrap" style="display:none;margin-bottom:10px">
   <div style="font-size:12px;color:var(--mut);font-weight:700;margin-bottom:6px">Prévia (primeiras linhas já estruturadas):</div>
   <div style="overflow:auto;border:1px solid var(--ln);border-radius:8px;max-height:200px"><table id="impprev" style="width:100%;border-collapse:collapse;font-size:11.5px"></table></div>
  </div>
  <div id="impmapwrap" style="border-top:1px solid var(--ln);padding-top:10px;margin-bottom:10px">
   <div style="font-size:12px;color:var(--mut);font-weight:700;margin-bottom:6px">Aponte as colunas do arquivo (ajuste se necessário):</div>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px 14px">
    <label style="font-size:12.5px;color:var(--mut)">Data<br><select id="mapData" class="din" style="width:100%"></select></label>
    <label style="font-size:12.5px;color:var(--mut)">Nome / Histórico<br><select id="mapName" class="din" style="width:100%"></select></label>
    <label style="font-size:12.5px;color:var(--mut)">Saída / Débito<br><select id="mapDebit" class="din" style="width:100%"></select></label>
    <label style="font-size:12.5px;color:var(--mut)">Entrada / Crédito<br><select id="mapCredit" class="din" style="width:100%"></select></label>
    <label style="font-size:12.5px;color:var(--mut)">Valor único (com sinal)<br><select id="mapAmt" class="din" style="width:100%"></select></label>
   </div>
   <div style="font-size:11px;color:var(--fnt);margin-top:6px">Use <b>Saída + Entrada</b> (duas colunas) OU <b>Valor único</b> (uma coluna com sinal). O que não usar, deixe em "—".</div>
  </div>
  <div class="co" style="margin:0 0 14px"><p>Datas, valores, método e categoria vêm preenchidos automaticamente pelas regras de cada banco. <b>Reconciled fica vazio</b> (exclusivo do Patrick). A categoria é um <b>palpite</b>; ajuste o que precisar.</p></div>
  <div style="display:flex;gap:8px;justify-content:flex-end">
   <button class="btn" id="impcancel">Cancelar</button>
   <button class="btn" id="impdo" style="background:var(--acc);color:#fff;border-color:var(--acc)">Importar</button>
  </div>
 </div>
</div>
<div id="toast" style="position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:90;background:var(--ink);color:var(--bg);padding:11px 18px;border-radius:10px;font:600 13px var(--ss);box-shadow:var(--sh);opacity:0;transition:opacity .2s;max-width:90vw;text-align:center;white-space:pre-line;pointer-events:none"></div>
<div class="tip" id="tip" role="tooltip"></div>
<div id="impprog" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:95;align-items:center;justify-content:center;padding:16px"><div style="background:var(--card);border:1px solid var(--ln2);border-radius:14px;padding:22px 26px;width:380px;max-width:100%;box-shadow:var(--sh);color:var(--ink);font-family:var(--ss)"><div style="font:700 15px var(--ss);display:flex;align-items:center;gap:8px"><span class="spin" style="display:inline-block;width:14px;height:14px;border:2px solid var(--ln2);border-top-color:var(--acc);border-radius:50%;animation:spin 0.8s linear infinite"></span> Analisando extrato…</div><div id="impprogmsg" style="font-size:12.5px;color:var(--mut);margin:9px 0 12px;min-height:16px"></div><div style="height:8px;background:var(--sunk);border-radius:6px;overflow:hidden"><div id="impprogbar" style="height:100%;width:0%;background:var(--acc);transition:width .5s ease"></div></div></div></div>
<style>@keyframes spin{to{transform:rotate(360deg)}}</style>
__XLSXLOADER__
<script>
const P=__PAYLOAD__;
const WEBHOOK=__WEBHOOK__;
let EDITS={},IMPORTS=[];
try{EDITS=JSON.parse(localStorage.getItem('ruche_mj_edits')||'{}');}catch(e){}
try{IMPORTS=JSON.parse(localStorage.getItem('ruche_mj_imports')||'[]');}catch(e){}
IMPORTS.forEach(r=>{r._imp=true;P.mj.push(r);});
P.mj.forEach(r=>{if(!r.emp)r.emp='Ruche Digital';if(r.av===undefined)r.av=r.pd;const e=EDITS[r.id];if(e)for(const k in e)r[k]=e[k];});
let nextId=P.mj.reduce((m,r)=>Math.max(m,r.id),0)+1;
const MONTHS=['2026-05','2026-06','2026-07','2026-08'];
const MN={'2026-05':'MAIO','2026-06':'JUNHO','2026-07':'JULHO','2026-08':'AGOSTO'};
const MSH={'2026-05':'MAI','2026-06':'JUN','2026-07':'JUL','2026-08':'AGO'};
const RECS=['Yes','No','Patrick Verificar','Cris Verificar','Em Aberto'];
const ACCCOL={'Stripe':'#635bff','Asaas':'#2f7de0','BoA':'#d64b40','Unicred - CC':'#8a8446','Unicred - Cartão':'#9a9350','Unicred - Invest':'#b3ac66','C6 - CC':'#c3c7cf','C6 - Cartão':'#242a36','PayPal':'#83c3ec','Payoneer':'#ec5f2e','Wise - Cris':'#4f9e6a','Wise - Ruche':'#38a597'};
const EMPCOL={'Ruche Digital':'#e6c136','Floor to Door':'#3f7fc4','Revenue Share':'#46a35f'};
const CTFAM={'1':'#D9EAD3','2':'#CFE2F3','3':'#FCE5CD','4':'#F4CCCC','5':'#F6D8D2','6':'#C9DAF8','7':'#D9D2E9','8':'#EAD1DC','9':'#DEDEDE','10':'#DCE6F1','11':'#FFF2CC','12':'#E7E4EF'};
const CTFAMSOLID={'1':'#70AD47','2':'#5B9BD5','3':'#F4A460','4':'#D45B5B','5':'#C0504D','6':'#3C78D8','7':'#9B72C6','8':'#8A4A7D','9':'#595959','10':'#5BA8A3','11':'#BF9000','12':'#808080'};
function ctColor(v){var m=String(v==null?'':v).match(/^\s*(\d+)/);return m?CTFAM[m[1]]:null;}
function famColorSolid(v){var m=String(v==null?'':v).match(/^\s*(\d+)/);return m?CTFAMSOLID[m[1]]:null;}
function pillCt(v){if(!v)return '';var bg=ctColor(v)||'#8a8f98',fg=lum(bg)>150?'#15181e':'#fff';return '<span class="pill" style="background:'+bg+';color:'+fg+'">'+esc(v)+'</span>';}
function lum(hex){hex=String(hex).replace('#','');if(hex.length<6)return 128;var r=parseInt(hex.substr(0,2),16),g=parseInt(hex.substr(2,2),16),b=parseInt(hex.substr(4,2),16);return 0.299*r+0.587*g+0.114*b;}
function pill(v,map){if(!v)return '';var bg=map[v]||'#8a8f98',fg=lum(bg)>150?'#15181e':'#fff';return '<span class="pill" style="background:'+bg+';color:'+fg+'">'+esc(v)+'</span>';}
let cur='2026-07',curEmp='Ruche Digital',curMode='month',curStart='2026-07-01',curEnd='2026-07-31';
const META_REV=61263.52;
const codeOf=s=>{const m=String(s).match(/^\s*([\d.]+)/);return m?m[1].replace(/\.+$/,''):'';};
const famOf=s=>{const c=codeOf(s);return c?c.split('.')[0]:'';};
const r2=x=>Math.round((x||0)*100)/100;
const f0=n=>(n<0?'-':'')+'US$ '+Math.abs(Math.round(n)).toLocaleString('pt-BR');
const pc=n=>(n<0?'-':'')+Math.abs(n).toFixed(1).replace('.',',')+'%';
const cv=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const brdt=d=>d?d.slice(8,10)+'/'+d.slice(5,7)+'/'+d.slice(2,4):'';
const tip=document.getElementById('tip');
let _tt;function toast(msg){const t=document.getElementById('toast');if(!t)return;t.textContent=msg;t.style.opacity='1';clearTimeout(_tt);_tt=setTimeout(()=>t.style.opacity='0',4500);}
function st(e,h){tip.innerHTML=h;tip.style.opacity='1';const r=tip.getBoundingClientRect();let x=e.clientX+14,y=e.clientY-10;if(x+r.width>innerWidth-8)x=e.clientX-r.width-14;if(y+r.height>innerHeight-8)y=innerHeight-r.height-8;if(y<8)y=8;tip.style.left=x+'px';tip.style.top=y+'px';}
function ht(){tip.style.opacity='0';}
const row=(c,l,v)=>'<div class="r"><span style="color:var(--mut)"><i style="display:inline-block;width:9px;height:9px;border-radius:2px;background:'+c+';margin-right:6px"></i>'+l+'</span><b>'+v+'</b></div>';
const NS='http://www.w3.org/2000/svg';const el=(t,a)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;};const clr=s=>{while(s.firstChild)s.removeChild(s.firstChild);};const cum=a=>{let s=0;return a.map(v=>s+=v);};
const esc=s=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');

/* período */
function monthB(m){const y=+m.slice(0,4),mo=+m.slice(5,7),last=new Date(y,mo,0).getDate();return [m+'-01',m+'-'+String(last).padStart(2,'0')];}
function inR(d,b){return d&&d>=b[0]&&d<=b[1];}
function nextDay(iso){const p=iso.split('-').map(Number);return new Date(Date.UTC(p[0],p[1]-1,p[2]+1)).toISOString().slice(0,10);}
function dayList(b){const out=[];let d=b[0],n=0;while(d<=b[1]&&n<500){out.push(d);d=nextDay(d);n++;}return out.length?out:[b[0]];}
function curBounds(){return curMode==='month'?monthB(cur):[curStart,curEnd];}
function curLabel(){return curMode==='month'?MN[cur]:(brdt(curStart)+'–'+brdt(curEnd));}
function empOk(r){return curEmp==='Todos'||r.emp===curEmp;}

/* ===== MOTOR ===== */
function dreForB(b){
  const rows=P.mj.filter(r=>empOk(r)&&inR(r.pe,b));
  const F={};for(const f of '123456789'){let t=0;for(const r of rows)if(famOf(r.ct)===f)t+=(f==='1'||f==='7')?r.i:r.o;F[f]=r2(t);}
  const gr=F['1'],ded=F['2'],nr=r2(gr-ded),cogs=F['3'],gp=r2(nr-cogs),fix=F['4'],opx=F['5'],ebitda=r2(gp-fix-opx),dna=F['6'],ebit=r2(ebitda-dna),oi=F['7'],fx=F['8'],ebt=r2(ebit+oi-fx),tax=F['9'],ni=r2(ebt-tax);
  const agg={gross_revenue:gr,deductions:ded,net_revenue:nr,cogs:cogs,gross_profit:gp,fixed:fix,opex:opx,ebitda:ebitda,dna:dna,ebit:ebit,other_income:oi,fin_exp:fx,ebt:ebt,tax:tax,net_income:ni};
  const items={};for(const r of rows){const c=codeOf(r.ct);if(!c)continue;const f=famOf(r.ct);items[c]=r2((items[c]||0)+((f==='1'||f==='7')?r.i:r.o));}
  return {agg,items,F};
}
function dreFor(m){return dreForB(monthB(m));}
const TOTKEY=[['GROSS REVENUE','gross_revenue'],['NET REVENUE','net_revenue'],['GROSS PROFIT','gross_profit'],['EBITDA','ebitda'],['EBIT','ebit'],['EBT','ebt'],['NET INCOME','net_income']];
function lineVal(l,D){const c=l.code;if(l.lvl==='item')return D.items[c]||0;if(/^\d+$/.test(c))return D.F[c]||0;if(/^\d+\.\d+$/.test(c)){let s=0;for(const k in D.items)if(k.indexOf(c+'.')===0)s+=D.items[k];return r2(s);}const up=l.name.toUpperCase();for(const t of TOTKEY)if(up.indexOf(t[0])>=0)return D.agg[t[1]];return null;}
function natOf(c){const f=c.split('.')[0];if('123456789'.indexOf(f)>=0&&f!=='')return 'op';if(f==='10')return 'inv';return 'fin';}
function fdcForB(b){
  // FDC = posição de caixa por CONTA (igual à planilha): contas de caixa (exclui cartão de crédito), pela payment date, em USD.
  const rows=P.mj.filter(r=>empOk(r)&&(r.ac||'')&&!/cart[ãa]o/i.test(r.ac||'')&&inR(r.pd,b));
  const acc={};let ti=0,to=0;
  for(const r of rows){const a=r.ac||'—';acc[a]=acc[a]||[0,0];acc[a][0]+=(r.i||0);acc[a][1]+=(r.o||0);ti+=(r.i||0);to+=(r.o||0);}
  return {tot:[r2(ti),r2(to),r2(ti-to)],acc:Object.keys(acc).map(a=>({a,in:r2(acc[a][0]),out:r2(acc[a][1]),net:r2(acc[a][0]-acc[a][1])})).sort((x,y)=>Math.abs(y.net)-Math.abs(x.net))};
}
function bucket(c){if(c.indexOf('3.4')===0||c.indexOf('3.3')===0)return 'Entrega (time)';if(c.indexOf('3.')===0)return 'Entrega (gateway/CRM)';if(c.indexOf('4.1')===0)return 'Folha fixa';if(c.indexOf('4.2')===0)return 'Ferramentas';if(c.indexOf('5.1')===0)return 'Marketing';if(c.indexOf('5.2')===0||c.indexOf('5.3')===0)return 'Overhead';if(c.indexOf('2.')===0)return 'Deduções/perdas';if(c.indexOf('8.')===0)return 'Financeiro';if(c.indexOf('9.')===0)return 'Impostos';return 'Outros';}
function resumoForB(b){
  const rows=P.mj.filter(r=>empOk(r)&&inR(r.pe,b));
  const days=dayList(b),nD=days.length,idx={};days.forEach((d,i)=>idx[d]=i);
  const drev=new Array(nD).fill(0),dexp=new Array(nD).fill(0),cats={},mix={};let payroll=0;const tx=[];
  for(const r of rows){const f=famOf(r.ct),c=codeOf(r.ct);let di=0;const dt=r.pd||r.da;if(dt&&idx[dt]!=null)di=idx[dt];else if(r.pe&&idx[r.pe]!=null)di=idx[r.pe];
    if(f==='1'){drev[di]+=r.i;if(/^1\.(1|2)/.test(c))mix['Recorrente']=(mix['Recorrente']||0)+r.i;else if(/^1\.3/.test(c))mix['Setup']=(mix['Setup']||0)+r.i;else mix['A classificar']=(mix['A classificar']||0)+r.i;}
    else if('23456789'.indexOf(f)>=0&&f!==''){dexp[di]+=r.o;const bk=bucket(c);cats[bk]=(cats[bk]||0)+r.o;if(/^4\.1/.test(c)||/^3\.4/.test(c)||/^3\.3/.test(c))payroll+=r.o;if(r.o>=1500)tx.push({d:brdt(days[di]).slice(0,5),name:(r.nm||'').slice(0,40),v:r2(r.o),cat:bk,acc:r.ac,code:c});}}
  tx.sort((a,b)=>b.v-a.v);const arr=o=>Object.keys(o).map(k=>({k:k,v:r2(o[k])})).sort((a,b)=>b.v-a.v);
  return {days:nD,dates:days,drev:drev.map(r2),dexp:dexp.map(r2),cats:arr(cats),revmix:arr(mix),tx:tx.slice(0,12),payroll:r2(payroll)};
}
function dreCur(){return dreForB(curBounds());}function fdcCur(){return fdcForB(curBounds());}function resumoCur(){return resumoForB(curBounds());}

/* ===== RESUMO ===== */
function kpis(){const D=dreCur(),a=D.agg,R=resumoCur();const ni=a.net_income,mg=a.gross_revenue?100*ni/a.gross_revenue:0,pp=a.gross_revenue?100*R.payroll/a.gross_revenue:0;
  const items=[['Receita bruta',f0(a.gross_revenue),'famílias 1','var(--ink)'],['Custo do serviço',f0(a.cogs),'gateway, time, comissões','var(--ink)'],['Desp. fixas + adm',f0(a.fixed+a.opex),'folha, ferramentas, overhead','var(--ink)'],['EBITDA',f0(a.ebitda),'antes de juros e impostos',a.ebitda>=0?'var(--up)':'var(--dn)'],['Result. financeiro',f0(a.other_income-a.fin_exp),'rendimentos − juros/multas',(a.other_income-a.fin_exp)>=0?'var(--up)':'var(--dn)'],['Lucro líquido',f0(ni),'resultado do período',ni>=0?'var(--up)':'var(--dn)'],['Margem líquida',pc(mg),'meta 20%',mg>=20?'var(--up)':(mg>=0?'var(--wr)':'var(--dn)')],['Folha',pc(pp),'meta 35%',pp<=35?'var(--up)':'var(--dn)']];
  document.getElementById('kpis').innerHTML=items.map(i=>'<div class="k"><div class="t">'+i[0]+'</div><div class="v" style="color:'+i[3]+'">'+i[1]+'</div><div class="s">'+i[2]+'</div></div>').join('');}
function chart1(){const R=resumoCur(),D=dreCur(),s=document.getElementById('c1');clr(s);const W=1100,H=280,P0={t:14,r:64,b:28,l:64},iw=W-P0.l-P0.r,ih=H-P0.t-P0.b;const rev=cum(R.drev),exp=cum(R.dexp),nd=rev.length||1;const mx=Math.max(1,...rev,...exp)*1.08,Y=v=>P0.t+ih-(v/mx)*ih,X=i=>P0.l+(iw/Math.max(1,nd-1))*i;
  for(let i=0;i<=4;i++){const v=mx*i/4,y=Y(v);s.appendChild(el('line',{x1:P0.l,y1:y,x2:W-P0.r,y2:y,class:'gl'}));const t=el('text',{x:P0.l-8,y:y+3.5,class:'av','text-anchor':'end'});t.textContent=Math.round(v/1000)+'k';s.appendChild(t);}
  const area=(arr,col,op)=>{const pts=arr.map((v,i)=>[X(i),Y(v)]);s.appendChild(el('path',{d:'M'+X(0)+','+Y(0)+'L'+pts.map(p=>p.join(',')).join('L')+'L'+X(nd-1)+','+Y(0)+'Z',fill:col,opacity:op}));s.appendChild(el('polyline',{points:pts.map(p=>p.join(',')).join(' '),fill:'none',stroke:col,'stroke-width':2.5,'stroke-linejoin':'round'}));};
  area(exp,cv('--exp'),.13);area(rev,cv('--rev'),.15);
  const step=Math.max(1,Math.ceil(nd/9));
  for(let i=0;i<nd;i++){if(i%step===0){const t=el('text',{x:X(i),y:H-9,class:'ax','text-anchor':'middle'});t.textContent=brdt(R.dates[i]).slice(0,5);s.appendChild(t);}const hw=iw/Math.max(1,nd-1),hit=el('rect',{x:X(i)-hw/2,y:P0.t,width:hw,height:ih,class:'hit'});hit.addEventListener('mousemove',e=>st(e,'<h4>'+brdt(R.dates[i])+'</h4>'+row(cv('--rev'),'Receita acum.',f0(rev[i]))+row(cv('--exp'),'Despesa acum.',f0(exp[i]))+row(cv('--nt'),'Diferença',f0(rev[i]-exp[i]))));hit.addEventListener('mouseleave',ht);s.appendChild(hit);}
  const R2=rev[nd-1]||0,E2=exp[nd-1]||0,ni=D.agg.net_income;document.getElementById('t1big').innerHTML=f0(ni)+' <span style="font-size:15px">'+(ni>=0?'DE LUCRO':'DE PREJUÍZO')+'</span>';document.getElementById('t1big').style.color=ni>=0?cv('--up'):cv('--dn');
  document.getElementById('t1sub').textContent=curLabel()+' · '+curEmp+' · lucro líquido do DRE';document.getElementById('t1r').textContent=f0(D.agg.gross_revenue);const mg=D.agg.gross_revenue?100*ni/D.agg.gross_revenue:0;
  document.getElementById('t1foot').innerHTML='<div>Receita/dia<b>'+f0(R2/nd)+'</b></div><div>Despesa/dia<b>'+f0(E2/nd)+'</b></div><div>Margem<b style="color:'+(mg>=0?cv('--up'):cv('--dn'))+'">'+pc(mg)+'</b></div><div>Meta receita/mês<b>'+f0(META_REV)+'</b></div>';}
function panels(){const R=resumoCur(),D=dreCur();const exp=R.cats.reduce((a,c)=>a+c.v,0)||1,rev=D.agg.gross_revenue||1;const mxc=Math.max(1,...R.cats.map(c=>c.v));const CC={'Folha fixa':'--exp','Entrega (time)':'--exp','Entrega (gateway/CRM)':'--goal','Marketing':'--acc','Ferramentas':'--goal','Overhead':'--nt','Deduções/perdas':'--dn','Financeiro':'--dn','Impostos':'--nt','Outros':'--nt'};
  document.getElementById('cats').innerHTML=R.cats.map(c=>'<div class="hr"><span>'+c.k+'</span><span class="hv">'+f0(c.v)+' · '+Math.round(100*c.v/exp)+'%</span><div class="tr"><i style="width:'+(100*c.v/mxc)+'%;background:var('+(CC[c.k]||'--nt')+')"></i></div></div>').join('')||'<div class="txc">Sem despesa no período.</div>';
  const mxm=Math.max(1,...R.revmix.map(c=>c.v)),MC={'Setup':'--goal','Recorrente':'--rev','A classificar':'--nt'};document.getElementById('mix').innerHTML=R.revmix.map(c=>'<div class="hr"><span>'+c.k+'</span><span class="hv">'+f0(c.v)+' · '+Math.round(100*c.v/rev)+'%</span><div class="tr"><i style="width:'+(100*c.v/mxm)+'%;background:var('+(MC[c.k]||'--nt')+')"></i></div></div>').join('')||'<div class="txc">Sem receita no período.</div>';
  const pp=rev?100*R.payroll/rev:0;document.getElementById('pgbig').textContent=pc(pp);document.getElementById('pgbig').style.color=pp<=35?cv('--up'):(pp<=45?cv('--wr'):cv('--dn'));document.getElementById('pgsub').textContent='da receita — meta 35%';document.getElementById('pgv').textContent=f0(R.payroll);document.getElementById('pgauge').innerHTML='<i style="width:'+Math.min(pp,100)+'%;background:'+(pp<=35?cv('--up'):cv('--dn'))+'"></i><span class="mk" style="left:35%"></span><span class="mkl" style="left:35%">meta 35%</span>';
  document.getElementById('txs').innerHTML=R.tx.length?R.tx.map(t=>'<div class="txr"><span class="txd">'+t.d+'</span><span><span class="txn">'+esc(t.name)+'</span><br><span class="txc">'+t.cat+' · '+esc(t.acc||'—')+' · '+t.code+'</span></span><span class="txv" style="color:var(--dn)">'+f0(t.v)+'</span></div>').join(''):'<p class="txc" style="margin:0">Nenhuma saída acima de US$ 1.500.</p>';}

/* ===== DRE ===== */
function renderDRE(){const Ds={};MONTHS.forEach(m=>Ds[m]=dreFor(m));const Dsel=dreCur();const nrCur=Dsel.agg.net_revenue||1;const range=curMode==='range';
  document.getElementById('dresub').textContent='Empresa: '+curEmp+' · por competência. '+(range?'Coluna PERÍODO = '+curLabel()+'. ':'')+'A coluna % é sobre a receita líquida de '+curLabel()+'.';
  let head='<tr><th>Linha</th>'+(range?'<th class="n" style="color:var(--acc);font-weight:800">PERÍODO</th>':'')+'<th class="n">MAI</th><th class="n">JUN</th><th class="n">JUL</th><th class="n">AGO</th><th class="n">% receita</th></tr>';
  document.querySelector('#dret thead').innerHTML=head;
  document.querySelector('#dret tbody').innerHTML=P.dre.map(l=>{const cls=l.lvl==='tot'?'tot':(l.lvl==='sub'?'sub':'item');const cell=(D,acc)=>{const v=lineVal(l,D);return '<td class="n'+(v<0?' neg':'')+'"'+(acc?' style="color:var(--acc)"':'')+'>'+(v===0||v===null?'—':f0(v))+'</td>';};const vc=lineVal(l,Dsel),pct=nrCur?100*(vc||0)/nrCur:0;
    var fc=(cls!=='item')?famColorSolid(l.code):null;var acc=fc?' style="box-shadow:inset 4px 0 0 '+fc+'"':'';
    return '<tr class="'+cls+'"'+acc+'><td>'+(l.code?'<span class="cd">'+l.code+'</span>':'')+l.name+'</td>'+(range?cell(Dsel,true):'')+cell(Ds['2026-05'])+cell(Ds['2026-06'])+cell(Ds['2026-07'])+cell(Ds['2026-08'])+'<td class="n" style="color:var(--fnt)">'+(vc?pct.toFixed(1).replace('.',',')+'%':'—')+'</td></tr>';}).join('');
  if(!range)document.querySelectorAll('#dret thead th').forEach((th,i)=>{if(i>=1&&i<=4){const m=MONTHS[i-1];th.style.color=(m===cur)?cv('--acc'):'';th.style.fontWeight=(m===cur)?'800':'';}});}
/* ===== FDC ===== */
function renderFDC(){const F=fdcCur();document.getElementById('fdcsub').textContent='Empresa: '+curEmp+' · '+curLabel()+' · posição de caixa por conta, pela Payment Date (igual à aba FDC da planilha).';
  const cards=[['Entradas',F.tot[0],'var(--up)'],['Saídas',F.tot[1],'var(--dn)'],['Caixa líquido do período',F.tot[2],F.tot[2]>=0?'var(--up)':'var(--dn)']];
  document.getElementById('natg').innerHTML=cards.map(c=>'<div class="nat"><div class="t">'+c[0]+'</div><div class="v" style="color:'+c[2]+'">'+f0(c[1])+'</div></div>').join('');
  document.querySelector('#fdct tbody').innerHTML=F.acc.map(a=>'<tr><td><b>'+esc(a.a)+'</b></td><td class="n">'+f0(a['in'])+'</td><td class="n">'+f0(a.out)+'</td><td class="n '+(a.net>=0?'pos':'neg')+'">'+f0(a.net)+'</td></tr>').join('')+'<tr class="tot"><td>Consolidado (contas de caixa)</td><td class="n">'+f0(F.tot[0])+'</td><td class="n">'+f0(F.tot[1])+'</td><td class="n '+(F.tot[2]>=0?'pos':'neg')+'">'+f0(F.tot[2])+'</td></tr>';
  document.getElementById('transfnote').innerHTML='Cálculo idêntico à aba <b>FDC</b> da planilha: por conta de caixa, pela <b>Payment Date</b>, em USD. Cartão de crédito não é conta de caixa — o caixa sai quando a fatura é paga pela conta corrente. Transferências entre contas próprias aparecem em cada conta e se anulam no consolidado.';}

/* ===== MASTER JOURNAL ===== */
let mjSort='pd',mjDir=-1,mjOnlyBad=false,mjSel=new Set();
const COLS=[
 {k:'da',t:'Date Added',type:'date',filt:'month'},{k:'nm',t:'Name',type:'text',filt:'text'},{k:'pm',t:'Payment Method',type:'ro',filt:'sel'},
 {k:'o',t:'Outflow (USD)',type:'ro',cls:'n',filt:'num'},{k:'i',t:'Inflow (USD)',type:'ro',cls:'n',filt:'num'},{k:'b',t:'Currency (BRL)',type:'ro',cls:'n',filt:'num'},
 {k:'ct',t:'Chart of Accounts',type:'sel',opts:'plano',filt:'sel'},{k:'ac',t:'Account',type:'sel',opts:'contas',filt:'sel'},{k:'emp',t:'Empresa',type:'sel',opts:'empresas',filt:'sel'},
 {k:'du',t:'Due Date',type:'date',filt:'month'},{k:'pd',t:'Payment Date',type:'date',filt:'month'},{k:'av',t:'Available',type:'date',filt:'month'},{k:'pe',t:'Period',type:'date',filt:'month'},
 {k:'nt',t:'Notes',type:'notes'},{k:'rc',t:'Reconciled',type:'sel',opts:'recon',filt:'sel'}];
const OPTS={plano:P.plano,contas:P.contas,empresas:P.empresas,recon:RECS};
let mjFilt={};
function distinct(k){return [...new Set(P.mj.map(r=>r[k]).filter(v=>v!==''&&v!=null))].sort();}
function numMatch(val,fv){fv=fv.trim();if(!fv)return true;const a=Math.abs(val||0);const m=fv.match(/^(>=|<=|>|<|=)?\s*([\d.,]+)$/);if(!m)return String(Math.round(a)).indexOf(fv.replace(/\D/g,''))>=0;const op=m[1]||'~';let num=parseFloat(m[2].replace(/\./g,'').replace(',','.'));if(isNaN(num))num=parseFloat(m[2]);if(op==='>')return a>num;if(op==='<')return a<num;if(op==='>=')return a>=num;if(op==='<=')return a<=num;if(op==='=')return Math.abs(a-num)<0.5;return String(Math.round(a)).indexOf(String(Math.round(num)))>=0;}
function recomputeFlags(){const key={};P.mj.forEach(r=>{const k=[r.pd,r.nm,r.i,r.o,r.ac,r.b].join('|');(key[k]=key[k]||[]).push(r.id);});const dup={};for(const k in key)if(key[k].length>1)key[k].forEach(id=>dup[id]=1);P.mj.forEach(r=>{const f=[];const isCard=/cart[ãa]o/i.test(r.ac||'');if(dup[r.id])f.push('dup');if(!isCard&&r.pd&&r.pe&&r.pd.slice(0,7)!==r.pe.slice(0,7))f.push('per');if(!r.ac)f.push('acc');if(!r.pd&&!isCard)f.push('pdt');r.f=f;});}
function mjFiltered(){const q=(document.getElementById('mjq').value||'').toLowerCase().trim();const pb=curBounds();
  return P.mj.filter(r=>{if(!inR(r.pd||r.da||r.pe,pb))return false;if(!empOk(r))return false;if(mjOnlyBad&&!r.f.length)return false;if(q){const h=(r.nm+' '+r.nt+' '+r.ac+' '+r.ct+' '+r.pm+' '+r.emp).toLowerCase();if(h.indexOf(q)<0)return false;}
    for(const k in mjFilt){const fv=mjFilt[k];if(!fv)continue;const col=COLS.find(c=>c.k===k);if(col.filt==='month'){if(!((r[k]||'').slice(0,7)===fv))return false;}else if(col.filt==='sel'){if(String(r[k]||'')!==fv)return false;}else if(col.filt==='num'){if(!numMatch(r[k],fv))return false;}else{if(String(r[k]||'').toLowerCase().indexOf(fv.toLowerCase())<0)return false;}}
    return true;}).sort((a,b)=>{const x=a[mjSort],y=b[mjSort];if(typeof x==='number'&&typeof y==='number')return (x-y)*mjDir;return String(x||'').localeCompare(String(y||''))*mjDir;});}
function buildHead(){const arrow=k=>mjSort===k?(mjDir<0?' ▾':' ▴'):'';
  let h1='<tr><th style="width:26px"><input type="checkbox" id="mjall" title="Selecionar todas as filtradas"></th>';COLS.forEach(c=>h1+='<th data-s="'+c.k+'" class="'+(c.cls||'')+'">'+c.t+'<span class="ar">'+arrow(c.k)+'</span></th>');h1+='</tr>';
  let h2='<tr class="filt"><th></th>';COLS.forEach(c=>{if(c.filt==='sel'){const opts=(c.opts?OPTS[c.opts]:distinct(c.k));h2+='<th><select data-f="'+c.k+'"><option value="">todos</option>'+opts.map(o=>'<option'+(mjFilt[c.k]===o?' selected':'')+'>'+esc(o)+'</option>').join('')+'</select></th>';}else if(c.filt==='month'){const ms=[...new Set(P.mj.map(r=>(r[c.k]||'').slice(0,7)).filter(Boolean))].sort();h2+='<th><select data-f="'+c.k+'"><option value="">todos</option>'+ms.map(o=>'<option'+(mjFilt[c.k]===o?' selected':'')+'>'+o+'</option>').join('')+'</select></th>';}else if(c.filt==='text'){h2+='<th><input data-f="'+c.k+'" value="'+esc(mjFilt[c.k]||'')+'" placeholder="filtrar"></th>';}else if(c.filt==='num'){h2+='<th><input data-f="'+c.k+'" value="'+esc(mjFilt[c.k]||'')+'" placeholder="&gt;1000"></th>';}else h2+='<th></th>';});h2+='</tr>';
  document.querySelector('#mjt thead').innerHTML=h1+h2;
  document.querySelectorAll('#mjt thead th[data-s]').forEach(th=>th.addEventListener('click',()=>{const k=th.dataset.s;if(mjSort===k)mjDir=-mjDir;else{mjSort=k;mjDir=-1;}renderMJ();}));
  document.querySelectorAll('#mjt thead [data-f]').forEach(inp=>inp.addEventListener('input',()=>{mjFilt[inp.dataset.f]=inp.value;renderMJ(true);}));
  const all=document.getElementById('mjall');all.addEventListener('change',()=>{const ids=mjFiltered().map(r=>r.id);if(all.checked)ids.forEach(i=>mjSel.add(i));else ids.forEach(i=>mjSel.delete(i));renderMJ();updateBulk();});}
function cellDisplay(r,c){const k=c.k,v=r[k];if(k==='o')return v?'<span style="color:var(--dn)">'+f0(v)+'</span>':'';if(k==='i')return v?'<span style="color:var(--up)">'+f0(v)+'</span>':'';if(k==='b')return v?'<span style="color:var(--fnt)">'+v.toLocaleString('pt-BR',{minimumFractionDigits:2})+'</span>':'';if(c.type==='date')return brdt(v);if(k==='nm')return '<b>'+esc(v)+'</b>'+(r._imp?'<span class="fg i">IMPORT</span>':'')+r.f.map(f=>'<span class="fg '+(f==='dup'?'d':'')+'">'+({dup:'DUP',per:'COMP',acc:'S/CONTA',pdt:'S/DATA'}[f])+'</span>').join('');if(k==='nt')return esc((v||'').slice(0,60));if(k==='ac')return pill(v,ACCCOL);if(k==='emp')return pill(v,EMPCOL);if(k==='ct')return pillCt(v);return esc(v);}
function renderMJ(){if(!document.querySelector('#mjt thead').children.length)buildHead();else document.querySelectorAll('#mjt thead th[data-s] .ar').forEach(a=>{const k=a.parentNode.dataset.s;a.textContent=mjSort===k?(mjDir<0?' ▾':' ▴'):'';});
  const all=mjFiltered();
  document.querySelector('#mjt tbody').innerHTML=all.map(r=>{const tds=COLS.map(c=>{const disp=cellDisplay(r,c);if(c.type==='ro')return '<td class="'+(c.cls||'')+'">'+disp+'</td>';const ntc=c.k==='nt'?' ntc':'';return '<td class="e mark'+ntc+'" data-id="'+r.id+'" data-k="'+c.k+'" title="clique para editar">'+disp+'</td>';}).join('');
    return '<tr class="'+(r.rc==='Yes'?'':'norec ')+(mjSel.has(r.id)?'sel ':'')+(r._imp?'imp':(EDITS[r.id]?'edited':''))+'"><td><input type="checkbox" class="mjck" data-id="'+r.id+'"'+(mjSel.has(r.id)?' checked':'')+'></td>'+tds+'</tr>';}).join('')||'<tr><td colspan="'+(COLS.length+1)+'" style="text-align:center;color:var(--mut);padding:24px">Nenhum lançamento com esses filtros.</td></tr>';
  const nbad=all.filter(r=>r.f.length).length;document.getElementById('mjn').textContent=all.length.toLocaleString('pt-BR')+' de '+P.mj.length+' · '+nbad+' com problema';bindCellEdit();}
function bindCellEdit(){const tb=document.querySelector('#mjt tbody');tb.querySelectorAll('.mjck').forEach(ck=>ck.onchange=()=>{const id=+ck.dataset.id;if(ck.checked)mjSel.add(id);else mjSel.delete(id);ck.closest('tr').classList.toggle('sel',ck.checked);updateBulk();});tb.querySelectorAll('td.e').forEach(td=>td.onclick=()=>{if(td.querySelector('input,select,textarea'))return;startEdit(td);});}
function startEdit(td){const id=+td.dataset.id,k=td.dataset.k,c=COLS.find(x=>x.k===k),r=P.mj.find(x=>x.id===id);let ed;
  if(c.type==='sel'){ed=document.createElement('select');ed.className='ce';ed.innerHTML='<option value="">—</option>'+OPTS[c.opts].map(o=>'<option'+(o===r[k]?' selected':'')+'>'+esc(o)+'</option>').join('');}
  else if(c.type==='date'){ed=document.createElement('input');ed.type='date';ed.className='ce';ed.value=r[k]||'';}
  else if(c.type==='notes'){ed=document.createElement('textarea');ed.className='ce';ed.value=r[k]||'';}
  else {ed=document.createElement('input');ed.type='text';ed.className='ce';ed.value=r[k]||'';}
  td.innerHTML='';td.appendChild(ed);ed.focus();if(ed.select)try{ed.select();}catch(e){}
  let done=false;const commit=()=>{if(done)return;done=true;let v=ed.value;if(c.type==='date')v=v||null;applyEdit(id,k,v);td.innerHTML=cellDisplay(r,c);};const cancel=()=>{if(done)return;done=true;td.innerHTML=cellDisplay(r,c);};
  ed.addEventListener('blur',commit);if(c.type==='sel'||c.type==='date')ed.addEventListener('change',commit);ed.addEventListener('keydown',e=>{if(e.key==='Enter'&&c.type!=='notes'){e.preventDefault();commit();}if(e.key==='Escape')cancel();});}
function persistImports(){try{localStorage.setItem('ruche_mj_imports',JSON.stringify(P.mj.filter(r=>r._imp)));}catch(e){}}
function applyEdit(id,k,val){const r=P.mj.find(x=>x.id===id);if(!r)return;if(r[k]===val)return;r[k]=val;if(r._imp){persistImports();}else{EDITS[id]=EDITS[id]||{};EDITS[id][k]=val;try{localStorage.setItem('ruche_mj_edits',JSON.stringify(EDITS));}catch(e){}}recomputeFlags();markDirty();renderLive();const ck=document.querySelector('#mjt tbody .mjck[data-id="'+id+'"]');if(ck){const trr=ck.closest('tr');if(!r._imp)trr.classList.add('edited');trr.classList.toggle('norec',r.rc!=='Yes');const nmtd=trr.querySelector('td.e[data-k="nm"]');if(nmtd)nmtd.innerHTML=cellDisplay(r,COLS.find(c=>c.k==='nm'));}}
function renderLive(){const D=dreCur(),a=D.agg,F=fdcCur();document.getElementById('mjlive').innerHTML='<div class="cell"><div class="t">'+curLabel()+' · '+curEmp+' · Receita</div><div class="v">'+f0(a.gross_revenue)+'</div></div><div class="cell"><div class="t">Despesa</div><div class="v">'+f0(a.gross_revenue-a.net_income)+'</div></div><div class="cell"><div class="t">Lucro líquido (DRE)</div><div class="v" style="color:'+(a.net_income>=0?'var(--up)':'var(--dn)')+'">'+f0(a.net_income)+'</div></div><div class="cell"><div class="t">Caixa líquido (FDC)</div><div class="v" style="color:'+(F.tot[2]>=0?'var(--up)':'var(--dn)')+'">'+f0(F.tot[2])+'</div></div><div class="hint">Muda o período/empresa lá em cima. Edite e veja recalcular.</div>';}
function markDirty(){const n=Object.keys(EDITS).length,ni=P.mj.filter(r=>r._imp).length;const d=document.getElementById('dirty');const parts=[];if(n)parts.push(n+' editada'+(n>1?'s':''));if(ni)parts.push(ni+' importada'+(ni>1?'s':''));d.textContent=parts.join(' · ');d.classList.toggle('on',n+ni>0);document.getElementById('disc').style.display=(n+ni)?'inline-block':'none';}

/* bulk */
const BFIELDS=[['ct','Chart of Accounts','sel','plano'],['ac','Account','sel','contas'],['emp','Empresa','sel','empresas'],['rc','Reconciled','sel','recon'],['du','Due Date','date'],['pd','Payment Date','date'],['pe','Period','date']];
function updateBulk(){const b=document.getElementById('bulk');b.classList.toggle('on',mjSel.size>0);document.getElementById('bulkn').textContent=mjSel.size+' selecionada'+(mjSel.size>1?'s':'');const all=document.getElementById('mjall');if(all){const ids=mjFiltered().map(r=>r.id);all.checked=ids.length>0&&ids.every(i=>mjSel.has(i));}}
function buildBulkVal(){const f=BFIELDS.find(x=>x[0]===document.getElementById('bulkfield').value);const w=document.getElementById('bulkvalwrap');if(f[2]==='sel')w.innerHTML='<select id="bulkval">'+OPTS[f[3]].map(o=>'<option>'+esc(o)+'</option>').join('')+'</select>';else w.innerHTML='<input id="bulkval" type="date">';}

/* ===== IMPORT UNIVERSAL ===== */
function ptaxFor(d){if(!d||!P.ptax)return null;if(P.ptax[d])return P.ptax[d];const ks=Object.keys(P.ptax).sort();let last=null;for(const k of ks){if(k<=d)last=P.ptax[k];else break;}return last;}
function detectDelim(line){const c=(line.match(/,/g)||[]).length,sc=(line.match(/;/g)||[]).length,tab=(line.match(/\t/g)||[]).length;if(sc>=c&&sc>=tab)return ';';if(tab>c)return '\t';return ',';}
function parseCSV(txt,dl){txt=txt.replace(/^﻿/,'');const rows=[];let f='',row=[],q=false;for(let i=0;i<txt.length;i++){const ch=txt[i];if(q){if(ch==='"'){if(txt[i+1]==='"'){f+='"';i++;}else q=false;}else f+=ch;}else{if(ch==='"')q=true;else if(ch===dl){row.push(f);f='';}else if(ch==='\n'||ch==='\r'){if(ch==='\r'&&txt[i+1]==='\n')i++;if(f!==''||row.length){row.push(f);rows.push(row);row=[];f='';}}else f+=ch;}}if(f!==''||row.length){row.push(f);rows.push(row);}return rows;}
function pnum(s){if(s==null||s==='')return null;if(typeof s==='number')return isFinite(s)?s:null;s=String(s).trim().replace(/[^\d.,-]/g,'');if(!s||s==='-'||s==='.'||s===',')return null;var neg=/-/.test(s);s=s.replace(/-/g,'');var lc=s.lastIndexOf(','),ld=s.lastIndexOf('.');if(lc>=0&&ld>=0){if(lc>ld)s=s.replace(/\./g,'').replace(',','.');else s=s.replace(/,/g,'');}else if(lc>=0){var af=s.length-lc-1;if(af===1||af===2)s=s.replace(',','.');else s=s.replace(/,/g,'');}var n=parseFloat(s);if(isNaN(n))return null;return neg?-n:n;}
var _MON={jan:1,feb:2,mar:3,apr:4,may:5,jun:6,jul:7,aug:8,sep:9,oct:10,nov:11,dec:12,fev:2,abr:4,mai:5,ago:8,set:9,out:10,dez:12};
function pad2(n){return String(n).padStart(2,'0');}
function pdate(s,order){if(s==null)return null;s=String(s).trim();if(!s)return null;var m=s.match(/(\d{4})-(\d{2})-(\d{2})/);if(m)return m[1]+'-'+m[2]+'-'+m[3];m=s.match(/(\d{1,2})[\/.\-\s]+([A-Za-zçÇ]{3,})[,\/.\-\s]+(\d{2,4})/);if(m){var mo=_MON[m[2].slice(0,3).toLowerCase()];if(mo){var y0=m[3].length===2?'20'+m[3]:m[3];return y0+'-'+pad2(mo)+'-'+pad2(+m[1]);}}m=s.match(/(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{2,4})/);if(m){var a=+m[1],b=+m[2],y=m[3];if(y.length===2)y='20'+y;var dd,mm;if(a>12){dd=a;mm=b;}else if(b>12){mm=a;dd=b;}else if(order==='mdy'){mm=a;dd=b;}else{dd=a;mm=b;}return y+'-'+pad2(mm)+'-'+pad2(dd);}return null;}
const HSYN={da:['date added','data added','transaction date','data da transa','created','criação','criacao'],nm:['name','nome','descri','description','hist','memo','detalhe','payee','benefici','counterparty','merchant','lançamento','lancamento'],pm:['payment method','método','metodo','forma'],pd:['payment date','data de pagamento','value date','data valor','posted','settled','date','data'],du:['due date','vencimento'],pe:['period','compet'],nt:['notes','observ',' obs'],ac:['account','conta','banco'],amt:['amount','valor','value','montante'],debit:['outflow','débito','debito','debit','saída','saida','money out','withdrawal','paid out','retirada'],credit:['inflow','crédito','credito','credit','entrada','money in','deposit','paid in'],avail:['available','disponív','disponiv','available on','data disponível'],txn:['transaction id','balance_transaction','txn id','stripe id'],rc:['reconciled','conciliado']};
function mapHeaders(hdr){const map={},used={};hdr.forEach((h,i)=>{const H=String(h).trim().toLowerCase();for(const k in HSYN){if(used[k])continue;if(HSYN[k].some(syn=>H.indexOf(syn)>=0)){map[i]=k;used[k]=1;break;}}});return map;}
let HISTCAT=null;
function buildHist(){const byName={};P.mj.forEach(r=>{if(r._imp||!r.ct)return;const n=(r.nm||'').trim().toLowerCase();if(!n)return;byName[n]=byName[n]||{};byName[n][r.ct]=(byName[n][r.ct]||0)+1;});const best={};for(const n in byName)best[n]=Object.keys(byName[n]).sort((a,b)=>byName[n][b]-byName[n][a])[0];HISTCAT=best;}
const KWRULES=[[/arranjo debito|arranjo débito|cred dom|stripe brasil/i,'12.3.1 - Inter-Account Transfers'],[/pagamento fatura|pag fatura|pgto fatura|pagamento recebido|pagamento de fatura/i,'12.3.1 - Inter-Account Transfers'],[/facebook|facebk|meta ?ads/i,'5.1.1 - Paid Traffic — Ruche Acquisition'],[/highlevel|gohighlevel|ghl/i,'3.1.2 - CRM - usage-based'],[/twilio|sonetel/i,'3.1.1 - Twilio / Telephony'],[/openai|anthropic|claude|chatgpt|manus/i,'4.2.4 - AI Tools'],[/google workspace|hostinger|lovable|hetzner|dicloak/i,'4.2.5 - Infrastructure / Technology'],[/\biof\b/i,'5.2.18 - Card IOF'],[/aluguel|\brent\b/i,'5.2.1 - Rent'],[/contabil|accounting|ferreira/i,'5.2.8 - Accounting'],[/simples nacional/i,'2.4.1 - Simples Nacional / DAS'],[/stripe/i,'3.2.1 - Stripe Fees','out']];
function classify(nm,nt,inflow){const key=(nm||'').trim().toLowerCase();let cat=null;if(HISTCAT&&HISTCAT[key])cat=HISTCAT[key];if(!cat){const hay=(nm+' '+nt);for(const kr of KWRULES){if(kr[2]==='out'&&inflow)continue;if(kr[0].test(hay)){cat=kr[1];break;}}}if(!cat||P.plano.indexOf(cat)<0)cat=inflow?'1.4.1 - Revenue to Classify':'5.4.1 - Expenses to Classify';return cat;}
let IMPParsed=null,IMPPre=null,IMPMode=null,IMPIsCard=false;
function guessAccount(fn){fn=(fn||'').toLowerCase();
 if(/unicred|sicredi/.test(fn)){if(/cart|fatura/.test(fn))return 'Unicred - Cartão';if(/invest|rdc|rentab/.test(fn))return 'Unicred - Invest';return 'Unicred - CC';}
 if(/c6/.test(fn)){if(/cart|fatura/.test(fn))return 'C6 - Cartão';return 'C6 - CC';}
 if(/boa|bank ?of ?america|bofa/.test(fn))return 'BoA';
 if(/payoneer/.test(fn))return 'Payoneer';if(/wise/.test(fn))return 'Wise - Cris';
 if(/stripe/.test(fn))return 'Stripe';if(/asaas/.test(fn))return 'Asaas';return null;}
function defCur(a){a=a||'';return(/\bboa\b|payoneer/i.test(a)||a==='Wise - Ruche')?'USD':'BRL';}
function fillSel(id,hdr,sel){document.getElementById(id).innerHTML='<option value="">—</option>'+hdr.map((h,i)=>'<option value="'+i+'"'+(i===sel?' selected':'')+'>'+esc((h||('coluna '+(i+1))).slice(0,40))+'</option>').join('');}
/* ---- helpers de formato ---- */
function mkrow(o){return Object.assign({da:null,nm:'',pm:'',o:0,i:0,b:0,ct:'',ac:'',emp:'Ruche Digital',du:null,pd:null,av:null,pe:null,nt:''},o||{});}
function setBRL(row,signed,dt){var abs=Math.abs(signed),isIn=signed>=0,p=ptaxFor(dt),usd=p?r2(abs/p):0;row.b=r2(isIn?abs:-abs);if(isIn){row.i=usd;row.o=0;}else{row.o=usd;row.i=0;}return isIn;}
function setUSD(row,signed,dt){var abs=Math.abs(signed),isIn=signed>=0,p=ptaxFor(dt),brl=p?r2(abs*p):0;row.b=isIn?brl:-brl;if(isIn){row.i=r2(abs);row.o=0;}else{row.o=r2(abs);row.i=0;}return isIn;}
function colIdx(H,subs){for(var i=0;i<H.length;i++){var h=String(H[i]==null?'':H[i]).toLowerCase();for(var j=0;j<subs.length;j++)if(h.indexOf(subs[j])>=0)return i;}return -1;}
function rowHas(row,subs){var s=(row||[]).map(function(x){return String(x==null?'':x).toLowerCase();}).join('~|~');return subs.every(function(t){return s.indexOf(t)>=0;});}
function findHdr(rows,subs){for(var i=0;i<Math.min(rows.length,25);i++)if(rowHas(rows[i],subs))return i;return -1;}
function invoiceDue(fname,vday){var m=String(fname||'').match(/(0?[1-9]|1[0-2])[ _.\-\/](20\d{2})/);if(!m)return null;return m[2]+'-'+pad2(+m[1])+'-'+pad2(vday);}
function pmBoA(nm){nm=(nm||'').toLowerCase();if(/zelle/.test(nm))return 'Zelle';if(/atm|withdrwl|withdrawal/.test(nm))return 'ATM';if(/\btransfer\b/.test(nm))return 'Wire Transfer';if(/purchase|mobile/.test(nm))return 'Debit Card';return '';}
function pmUniCC(nm){nm=(nm||'').toLowerCase();if(/pix/.test(nm))return 'Pix';if(/ted|tef|transferencia/.test(nm))return 'Transferência';if(/boleto|titulo|liquidacao/.test(nm))return 'Boleto';if(/pagamento|debito/.test(nm))return 'Débito';if(/credito|recebimento/.test(nm))return 'Crédito';return '';}
var BANKLABEL={stripe:'Stripe (extrato)',boa:'Bank of America',payoneer:'Payoneer',asaas:'Asaas',unicredcc:'Unicred — Conta Corrente',c6card:'C6 — Fatura Cartão',unicredcard:'Unicred — Fatura Cartão',c6cc:'C6 — Conta Corrente'};
/* ---- detecção ---- */
function detectFormat(rows,fname){var h;
 if((h=findHdr(rows,['balance_transaction_id']))>=0)return {bank:'stripe',h:h,acc:'Stripe'};
 if((h=findHdr(rows,['data de compra','valor (em r']))>=0)return {bank:'c6card',h:h,acc:'C6 - Cartão'};
 if((h=findHdr(rows,['descri','portador','cotação']))>=0||(h=findHdr(rows,['descri','portador','cotacao']))>=0)return {bank:'unicredcard',h:h,acc:'Unicred - Cartão'};
 if((h=findHdr(rows,['lançamento','valor (r']))>=0||(h=findHdr(rows,['lancamento','valor (r']))>=0)return {bank:'unicredcc',h:h,acc:'Unicred - CC'};
 if((h=findHdr(rows,['transaction id','currency','amount']))>=0)return {bank:'payoneer',h:h,acc:'Payoneer'};
 if((h=findHdr(rows,['date','description','amount','running bal']))>=0)return {bank:'boa',h:h,acc:'BoA'};
 if((h=findHdr(rows,['transação','descrição','valor','saldo']))>=0||(h=findHdr(rows,['transacao','descricao','valor','saldo']))>=0)return {bank:'asaas',h:h,acc:'Asaas'};
 var flat=rows.slice(0,8).map(function(r){return (r||[]).join(' ');}).join(' ').toLowerCase();
 if(flat.indexOf('conta corrente c6')>=0||flat.indexOf('sem movimenta')>=0)return {bank:'c6cc',h:-1,acc:'C6 - CC'};
 return {bank:'generic',h:-1,acc:guessAccount(fname)};}
/* ---- parsers por banco ---- */
function parseBoA(rows,h){var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var amt=pnum(r[2]);if(amt==null)continue;var dt=pdate(r[0],'mdy');if(!dt)continue;var nm=String(r[1]==null?'':r[1]).trim();var row=mkrow({ac:'BoA',pm:pmBoA(nm),da:dt,pe:dt,du:dt,pd:dt,av:dt});var isIn=setUSD(row,amt,dt);row.nm=nm;row.ct=classify(nm,'',isIn);out.push(row);}return out;}
function parsePayoneer(rows,h){var H=rows[h];var cD=colIdx(H,['date']),cN=colIdx(H,['description']),cA=colIdx(H,['amount']),cC=colIdx(H,['currency']),cT=colIdx(H,['transaction id','transaction']);var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var amt=pnum(r[cA]);if(amt==null)continue;var dt=pdate(r[cD],'dmy');if(!dt)continue;var nm=String((cN>=0?r[cN]:'')||'').trim();var cur=cC>=0?String(r[cC]||'').toUpperCase():'USD';var txn=cT>=0?String(r[cT]||'').trim():'';var row=mkrow({ac:'Payoneer',pm:'Payoneer',da:dt,pe:dt,du:dt,pd:dt,av:dt,nt:txn});var isIn=(cur==='BRL')?setBRL(row,amt,dt):setUSD(row,amt,dt);row.nm=nm;row.ct=classify(nm,txn,isIn);out.push(row);}return out;}
function parseAsaas(rows,h){var H=rows[h];var cD=colIdx(H,['data']),cN=colIdx(H,['descri']),cV=colIdx(H,['valor']),cT=colIdx(H,['transação','transacao']);var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var dt=pdate(r[cD],'dmy');if(!dt)continue;var val=pnum(r[cV]);if(val==null)continue;var nm=String((cN>=0?r[cN]:'')||'').trim();if(!nm&&cT>=0)nm=String(r[cT]||'').trim();var pm=/pix/i.test(nm)?'Pix':(/boleto/i.test(nm)?'Boleto':'');var row=mkrow({ac:'Asaas',pm:pm,da:dt,pe:dt,du:dt,pd:dt,av:dt});var isIn=setBRL(row,val,dt);row.nm=nm;row.ct=classify(nm,'',isIn);out.push(row);}return out;}
function parseUnicredCC(rows,h){var H=rows[h];var cD=colIdx(H,['data']),cN=colIdx(H,['lançamento','lancamento']),cV=colIdx(H,['valor']);if(cD<0||cV<0)return [];var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var dc=r[cD];if(dc==null||String(dc).trim()==='')continue;var dt=pdate(dc,'dmy');if(!dt)continue;var vc=r[cV];var val=(typeof vc==='number')?vc:pnum(vc);if(val==null)continue;var nm=String((cN>=0?r[cN]:'')||'').trim();var row=mkrow({ac:'Unicred - CC',pm:pmUniCC(nm),da:dt,pe:dt,du:dt,pd:dt,av:dt});var isIn=setBRL(row,val,dt);row.nm=nm;row.ct=classify(nm,'',isIn);out.push(row);}return out;}
function parseCard(rows,h,accName,vday,fname,dsub,nsub,vsub){var H=rows[h];var cD=colIdx(H,dsub),cN=colIdx(H,nsub),cV=colIdx(H,vsub);if(cD<0||cV<0)return [];var due=invoiceDue(fname,vday);var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var dt=pdate(r[cD],'dmy');if(!dt)continue;var valR=pnum(r[cV]);if(valR==null||Math.abs(valR)<0.005)continue;var nm=String((cN>=0?r[cN]:'')||'').trim();var row=mkrow({ac:accName,pm:'Credit Card',da:dt,pe:dt,du:due,pd:null,av:null});var isIn=setBRL(row,-valR,dt);row.nm=nm;row.ct=classify(nm,'',isIn);out.push(row);}return out;}
function parseStripe(rows,h){var H=rows[h].map(function(x){return String(x==null?'':x).toLowerCase();});function ci(n){return H.indexOf(n);}
 var cCr=ci('created');if(cCr<0)cCr=ci('created_utc');var cAv=ci('available_on');if(cAv<0)cAv=ci('available_on_utc');
 var cGr=ci('gross'),cFe=ci('fee'),cNe=ci('net'),cCat=ci('reporting_category'),cDe=ci('description'),cCF=ci('customer_facing_amount'),cCFC=ci('customer_facing_currency'),cNm=ci('customer_name'),cTx=ci('balance_transaction_id'),cInv=ci('invoice_number');
 var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;
  var cat=String((cCat>=0?r[cCat]:'')||'').toLowerCase();var created=pdate(cCr>=0?r[cCr]:null,'ymd');if(!created)continue;var avail=pdate(cAv>=0?r[cAv]:null,'ymd')||created;
  var txn=cTx>=0?String(r[cTx]||'').trim():'',desc=cDe>=0?String(r[cDe]||'').trim():'',cust=cNm>=0?String(r[cNm]||'').trim():'',inv=cInv>=0?String(r[cInv]||'').trim():'';
  var gross=cGr>=0?pnum(r[cGr]):null,fee=cFe>=0?pnum(r[cFe]):0,net=cNe>=0?pnum(r[cNe]):null,cfAmt=cCF>=0?pnum(r[cCF]):null,cfCur=cCFC>=0?String(r[cCFC]||'').toLowerCase():'';
  var note=[txn,desc,inv?('inv '+inv):''].filter(Boolean).join(' · ');
  if(cat==='charge'){var isIn=(gross==null)?true:gross>=0,absG=Math.abs(gross||0),usd;if(cfAmt!=null&&cfCur==='usd')usd=Math.abs(cfAmt);else{var p=ptaxFor(created);usd=p?r2(absG/p):0;}
   var rowR=mkrow({ac:'Stripe',pm:'Stripe',da:created,pe:isIn?created:avail,pd:avail,av:avail,nm:cust||desc||'Stripe',nt:note,b:r2(isIn?absG:-absG),i:isIn?r2(usd):0,o:isIn?0:r2(usd)});rowR.ct=classify(rowR.nm,note,isIn);out.push(rowR);
   if(fee&&Math.abs(fee)>0.004){var p2=ptaxFor(created),fusd=p2?r2(Math.abs(fee)/p2):0;out.push(mkrow({ac:'Stripe',pm:'Stripe',da:created,pe:avail,pd:avail,av:avail,nm:'Stripe fee — '+(cust||desc||''),o:fusd,i:0,b:-Math.abs(r2(fee)),ct:'3.2.1 - Stripe Fees',nt:txn+' · fee'}));}
  }else{var amt=(net!=null)?net:(gross!=null?gross:null);if(amt==null||Math.abs(amt)<0.004)continue;var row1=mkrow({ac:'Stripe',pm:'Stripe',da:created,pd:avail,av:avail,nm:desc||cust||'Stripe',nt:note});var isIn2=setBRL(row1,amt,created);row1.pe=isIn2?created:avail;row1.ct=(cat==='fee'||cat==='other_adjustment')?'3.2.1 - Stripe Fees':classify(row1.nm,note,isIn2);out.push(row1);}
 }return out;}
/* ---- roteamento + commit ---- */
function dedupKey(r){return r.ac+'|'+r.da+'|'+(Math.round((r.b||0)*100)/100)+'|'+(r.nm||'').slice(0,24).toLowerCase();}
function mjKey(r){return (r.ac||'')+'|'+(r.pd||r.da||'')+'|'+(Math.round((r.o||0)*100)/100)+'|'+(Math.round((r.i||0)*100)/100);}
function commitRows(list){if(!list||!list.length){toast('Nada para importar.');return;}
  var seen={};P.mj.forEach(function(r){seen[mjKey(r)]=1;});
  var added=0,dup=0,addedRows=[];list.forEach(function(r){var k=mjKey(r);if(seen[k]){dup++;return;}seen[k]=1;r.rc='No';r.id=nextId++;r._imp=true;r.f=[];if(!r.nm)r.nm='(sem nome)';P.mj.push(r);addedRows.push(r);added++;});
  var jumped='';
  if(added){var ds=addedRows.map(function(r){return r.pd||r.da||r.pe;}).filter(Boolean).sort();if(ds.length){var mn=ds[0],mx=ds[ds.length-1];if(mn.slice(0,7)===mx.slice(0,7)){curMode='month';cur=mn.slice(0,7);jumped=' Período ajustado para '+cur+'.';}else{curMode='range';curStart=mn;curEnd=mx;jumped=' Período ajustado para '+mn+' → '+mx+'.';}try{buildMsel();}catch(e){}var rb=document.getElementById('rangebox');if(rb)rb.style.display=curMode==='range'?'inline':'none';if(curMode==='range'){var rs=document.getElementById('rstart'),re=document.getElementById('rend');if(rs)rs.value=curStart;if(re)re.value=curEnd;}}}
  recomputeFlags();persistImports();markDirty();buildHist();closeImport();if(window.__mjInit){renderActive();}toast(added?(added+' linha(s) importada(s), Reconciled = No.'+jumped+(dup?(' '+dup+' já constavam na planilha — ignoradas (sem duplicar).'):'')):(dup+' linha(s) já constavam na planilha — nada duplicado.'));}
function renderPreview(list){var t=document.getElementById('impprev');var head='<tr style="position:sticky;top:0;background:var(--sunk)"><th style="text-align:left;padding:4px 6px">Data</th><th style="text-align:left;padding:4px 6px">Nome</th><th style="text-align:right;padding:4px 6px">Saída</th><th style="text-align:right;padding:4px 6px">Entrada</th><th style="text-align:right;padding:4px 6px">R$</th><th style="text-align:left;padding:4px 6px">Categoria</th></tr>';var body=list.slice(0,6).map(function(r){return '<tr><td style="padding:3px 6px">'+brdt(r.da)+'</td><td style="padding:3px 6px">'+esc((r.nm||'').slice(0,26))+'</td><td style="padding:3px 6px;text-align:right;color:var(--dn)">'+(r.o?f0(r.o):'')+'</td><td style="padding:3px 6px;text-align:right;color:var(--up)">'+(r.i?f0(r.i):'')+'</td><td style="padding:3px 6px;text-align:right;color:var(--fnt)">'+(r.b?r.b.toLocaleString('pt-BR',{minimumFractionDigits:2}):'')+'</td><td style="padding:3px 6px;color:var(--fnt)">'+esc((r.ct||'').slice(0,22))+'</td></tr>';}).join('');t.innerHTML=head+body+(list.length>6?'<tr><td colspan="6" style="padding:4px 6px;color:var(--mut)">+ '+(list.length-6)+' linha(s)…</td></tr>':'');}
function routeImport(rows,fname){rows=(rows||[]).filter(function(r){return r&&r.length&&r.some(function(x){return String(x==null?'':x).trim()!=='';});});if(rows.length<2){toast('Arquivo sem linhas de dados.');return;}
 var det=detectFormat(rows,fname);document.getElementById('impacc').innerHTML=P.contas.map(function(a){return '<option>'+esc(a)+'</option>';}).join('');document.getElementById('impacc').value=det.acc||guessAccount(fname)||P.contas[0];document.getElementById('impcur').value=defCur(document.getElementById('impacc').value);
 if(det.bank==='generic'){IMPMode='manual';openManual(rows,fname);return;}
 if(det.bank==='c6cc'){toast('C6 Conta Corrente: sem movimentações no período — nada a importar.');return;}
 var venc=null;IMPIsCard=false;var list=[];
 if(det.bank==='stripe')list=parseStripe(rows,det.h);
 else if(det.bank==='boa')list=parseBoA(rows,det.h);
 else if(det.bank==='payoneer')list=parsePayoneer(rows,det.h);
 else if(det.bank==='asaas')list=parseAsaas(rows,det.h);
 else if(det.bank==='unicredcc')list=parseUnicredCC(rows,det.h);
 else if(det.bank==='c6card'){IMPIsCard=true;venc=invoiceDue(fname,1);list=parseCard(rows,det.h,'C6 - Cartão',1,fname,['data de compra'],['descri'],['valor (em r']);}
 else if(det.bank==='unicredcard'){IMPIsCard=true;venc=invoiceDue(fname,19);list=parseCard(rows,det.h,'Unicred - Cartão',19,fname,['data'],['descri'],['valor']);}
 if(!list.length){toast('Formato reconhecido ('+det.acc+'), mas nenhuma linha válida encontrada.');return;}
 IMPMode='auto';IMPPre=list;
 document.getElementById('impinfo').textContent=list.length+' lançamento(s) estruturado(s) a partir do arquivo.';
 var d2=document.getElementById('impdet');d2.style.display='block';d2.innerHTML='<b>Formato detectado:</b> '+esc(BANKLABEL[det.bank]||det.acc)+'. Datas, valores (PTAX quando em R$), método e categoria já preenchidos.';
 document.getElementById('impmapwrap').style.display='none';
 var cb=document.getElementById('impcard');if(IMPIsCard){cb.style.display='flex';document.getElementById('impvenc').value=venc||'';document.getElementById('impfatura').value='';}else cb.style.display='none';
 renderPreview(list);document.getElementById('impprevwrap').style.display='block';document.getElementById('impmodal').style.display='flex';}
function showImpProgress(){var o=document.getElementById('impprog'),bar=document.getElementById('impprogbar'),msg=document.getElementById('impprogmsg');o.style.display='flex';bar.style.width='0%';
 var steps=['Enviando extrato ao motor de conciliação…','Detectando o banco e estruturando as linhas…','Calculando datas e vencimentos (regra de cada banco)…','Convertendo BRL ↔ USD pela PTAX da data…','Classificando pelo plano de contas e histórico…','Conferindo transferências, taxas e IOF…'];
 var i=0,pct=0,start=Date.now();msg.textContent=steps[0];bar.style.width='6%';
 var t=setInterval(function(){i++;if(i<steps.length)msg.textContent=steps[i];pct=Math.min(92,pct+9);bar.style.width=pct+'%';},650);
 return {setMsg:function(m){msg.textContent=m;},done:function(ok,finalMsg){var el=Date.now()-start,wait=Math.max(0,3200-el);setTimeout(function(){clearInterval(t);bar.style.width='100%';msg.textContent=finalMsg||((ok===false)?'Não foi possível processar.':'Pronto!');setTimeout(function(){o.style.display='none';},450);},wait);}};}
async function readFileRows(f){var nm=f.name||'';
 if(/\.(xls|xlsx|xlsm)$/i.test(nm)){if(typeof XLSX==='undefined')throw new Error('Leitor de Excel indisponível');var buf=await f.arrayBuffer();var wb=XLSX.read(new Uint8Array(buf),{type:'array'});var ws=wb.Sheets[wb.SheetNames[0]];return XLSX.utils.sheet_to_json(ws,{header:1,raw:true,defval:''});}
 var txt=await f.text();var dl=detectDelim((txt.replace(/^﻿/,'').split(/\r?\n/)[0]||''));return parseCSV(txt,dl);}
async function importFiles(files){files=[].slice.call(files);if(!files.length)return;
 var prog=showImpProgress();var all=[],lines=[];
 for(var i=0;i<files.length;i++){var f=files[i];
  prog.setMsg('('+(i+1)+'/'+files.length+') '+f.name+' — enviando ao n8n…');
  try{
   if(/\.pdf$/i.test(f.name)){lines.push(f.name+': PDF não lido');continue;}
   var rows=await readFileRows(f);
   var resp=await fetch(WEBHOOK,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify({rows:rows,filename:f.name})});
   if(!resp.ok){lines.push(f.name+': n8n HTTP '+resp.status);continue;}
   var data=await resp.json();var list=(data&&data.rows)||[];
   if(list.length){all=all.concat(list);lines.push(f.name+': '+list.length+' ('+(data.account||data.bank)+')');}
   else lines.push(f.name+': '+((data&&data.message)||'0 linhas'));
  }catch(e){lines.push(f.name+': erro '+e.message);}
 }
 prog.done(true, files.length+' arquivo(s) processado(s).');
 setTimeout(function(){commitRows(all);},700);
}
async function routeViaWebhook(rows,fname){rows=(rows||[]).filter(function(r){return r&&r.length&&r.some(function(x){return String(x==null?'':x).trim()!=='';});});if(rows.length<2){toast('Arquivo sem linhas de dados.');return;}
 var prog=showImpProgress();
 try{
  var resp=await fetch(WEBHOOK,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify({rows:rows,filename:fname})});
  if(!resp.ok){prog.done(false);toast('n8n retornou '+resp.status+' — o workflow está ativo?');return;}
  var data=await resp.json();var list=(data&&data.rows)||[];
  if(!list.length){prog.done(false);toast((data&&data.message)||'Nenhuma linha reconhecida pelo n8n.');return;}
  IMPMode='auto';IMPPre=list;IMPIsCard=/cart[ãa]o/i.test(data.account||'');
  document.getElementById('impacc').innerHTML=P.contas.map(function(a){return '<option>'+esc(a)+'</option>';}).join('');
  document.getElementById('impacc').value=data.account||list[0].ac||P.contas[0];
  document.getElementById('impcur').value=defCur(document.getElementById('impacc').value);
  document.getElementById('impinfo').textContent=list.length+' lançamento(s) estruturado(s) pelo n8n.';
  var d2=document.getElementById('impdet');d2.style.display='block';d2.innerHTML='<b>Processado no n8n:</b> '+esc(data.account||data.bank)+'. Datas (por regra do handoff), PTAX e categoria aplicadas no servidor.';
  document.getElementById('impmapwrap').style.display='none';
  var cb=document.getElementById('impcard');if(IMPIsCard){cb.style.display='flex';document.getElementById('impvenc').value=list[0].du||'';document.getElementById('impfatura').value='';}else cb.style.display='none';
  renderPreview(list);document.getElementById('impprevwrap').style.display='block';document.getElementById('impmodal').style.display='flex';
  prog.done(true);
 }catch(e){prog.done(false);toast('Erro ao falar com o n8n: '+e.message+' (CORS/ativo?)');}}
function openManual(rows,fname){var hdr=rows[0];IMPParsed={rows:rows.slice(1),hdr:hdr};var map=mapHeaders(hdr);var io=function(k){for(var i in map)if(map[i]===k)return +i;return -1;};
 document.getElementById('impinfo').textContent=(rows.length-1)+' linhas · '+hdr.length+' colunas · formato não reconhecido — confira o mapeamento.';
 document.getElementById('impdet').style.display='none';document.getElementById('impprevwrap').style.display='none';document.getElementById('impmapwrap').style.display='block';
 var ga=guessAccount(fname);if(ga)document.getElementById('impacc').value=ga;document.getElementById('impcur').value=defCur(document.getElementById('impacc').value);
 fillSel('mapData',hdr,io('pd')>=0?io('pd'):io('da'));fillSel('mapName',hdr,io('nm'));fillSel('mapDebit',hdr,io('debit'));fillSel('mapCredit',hdr,io('credit'));fillSel('mapAmt',hdr,io('amt'));
 var toggleCard=function(){document.getElementById('impcard').style.display=/cart[ãa]o/i.test(document.getElementById('impacc').value)?'flex':'none';document.getElementById('impcur').value=defCur(document.getElementById('impacc').value);};
 document.getElementById('impacc').onchange=toggleCard;toggleCard();document.getElementById('impmodal').style.display='flex';}
function doImport(){if(IMPMode==='auto'){if(!IMPPre||!IMPPre.length){toast('Nada para importar.');return;}var acc=document.getElementById('impacc').value;if(IMPIsCard){var vd=document.getElementById('impvenc').value||null,fd=document.getElementById('impfatura').value||null;IMPPre.forEach(function(r){r.ac=acc;if(vd)r.du=vd;if(fd){r.pd=fd;r.av=fd;}});}else IMPPre.forEach(function(r){r.ac=acc;});commitRows(IMPPre);IMPPre=null;return;}doImportManual();}
function doImportManual(){if(!IMPParsed)return;var rows=IMPParsed.rows,hdr=IMPParsed.hdr,acc=document.getElementById('impacc').value,cur3=document.getElementById('impcur').value;
  var isCard=/cart[ãa]o/i.test(acc),isStripe=/stripe/i.test(acc);var venc=document.getElementById('impvenc').value||null,fat=document.getElementById('impfatura').value||null;
  if(isCard&&(!venc||!fat)){toast('Cartão: preencha o Vencimento e o Pagamento da fatura.');return;}
  var gv=function(id){var v=document.getElementById(id).value;return v===''?-1:+v;};var iDate=gv('mapData'),iName=gv('mapName'),iDeb=gv('mapDebit'),iCred=gv('mapCredit'),iAmt=gv('mapAmt');
  if(iDate<0){toast('Escolha a coluna de Data no mapeamento.');return;}
  if(iDeb<0&&iCred<0&&iAmt<0){toast('Escolha a coluna de valor: Saída/Entrada (duas) ou Valor único (uma).');return;}
  var map=mapHeaders(hdr),idx=function(k){for(var i in map)if(map[i]===k)return +i;return -1;};var iNt=idx('nt'),iPm=idx('pm'),iAvail=idx('avail'),iTxn=idx('txn');
  var list=[],ord=cur3==='USD'?'mdy':'dmy';
  rows.forEach(function(rr){var nm=iName>=0?String(rr[iName]||'').trim():'';var dt=pdate(rr[iDate],ord);if(!dt)return;var signed=null;if(iDeb>=0||iCred>=0){var d=Math.abs(pnum(iDeb>=0?rr[iDeb]:'')||0),c=Math.abs(pnum(iCred>=0?rr[iCred]:'')||0);if(d===0&&c===0)signed=null;else signed=c-d;}else if(iAmt>=0)signed=pnum(rr[iAmt]);if(signed==null)return;
    var nt=iNt>=0?String(rr[iNt]||''):'';var row=mkrow({ac:acc,pm:iPm>=0?String(rr[iPm]||''):(isCard?'Credit Card':'')});
    var isIn;if(cur3==='USD')isIn=setUSD(row,signed,dt);else isIn=setBRL(row,signed,dt);
    if(isCard){row.da=dt;row.pe=dt;row.du=venc;row.pd=fat;row.av=fat;}
    else if(isStripe){var avd=iAvail>=0?pdate(rr[iAvail],ord):null;row.da=dt;row.pd=dt;row.pe=dt;row.av=avd||dt;var txn=iTxn>=0?String(rr[iTxn]||''):'';nt=[txn,nm,nt].filter(Boolean).join(' · ');}
    else {row.da=dt;row.du=dt;row.pd=dt;row.av=dt;row.pe=dt;}
    row.nm=nm;row.nt=nt;row.ct=classify(nm,nt,isIn);list.push(row);});
  if(!list.length){toast('0 linhas: verifique o mapeamento (Data e Valor) — a coluna de valor pode estar vazia.');return;}commitRows(list);}
function closeImport(){document.getElementById('impmodal').style.display='none';IMPParsed=null;IMPPre=null;IMPMode=null;IMPIsCard=false;}

/* nav */
function renderResumo(){kpis();chart1();panels();}
function renderActive(){const p=document.querySelector('.tb[aria-selected="true"]').dataset.p;if(p==='resumo')renderResumo();else if(p==='dre')renderDRE();else if(p==='fdc')renderFDC();else if(p==='mj'){renderLive();renderMJ();}}
function buildMsel(){document.getElementById('msel').innerHTML=MONTHS.map(m=>'<button class="mb" data-m="'+m+'"'+(curMode==='month'&&m===cur?' aria-pressed="true"':' aria-pressed="false"')+'>'+MSH[m]+'</button>').join('')+'<button class="mb" data-m="custom"'+(curMode==='range'?' aria-pressed="true"':' aria-pressed="false"')+'>Personalizado</button>';
  document.querySelectorAll('#msel .mb').forEach(b=>b.addEventListener('click',()=>{if(b.dataset.m==='custom'){curMode='range';document.getElementById('rangebox').style.display='inline';document.getElementById('rstart').value=curStart;document.getElementById('rend').value=curEnd;}else{curMode='month';cur=b.dataset.m;document.getElementById('rangebox').style.display='none';}document.querySelectorAll('#msel .mb').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));renderActive();}));}
buildMsel();
document.getElementById('rstart').addEventListener('change',e=>{curStart=e.target.value||curStart;curMode='range';renderActive();});
document.getElementById('rend').addEventListener('change',e=>{curEnd=e.target.value||curEnd;curMode='range';renderActive();});
const esel=document.getElementById('esel');esel.innerHTML='<option>Ruche Digital</option><option>Floor to Door</option><option>Todos</option>';esel.value=curEmp;esel.addEventListener('change',()=>{curEmp=esel.value;renderActive();});
document.querySelectorAll('.tb').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.tb').forEach(x=>x.setAttribute('aria-selected',x===b?'true':'false'));document.querySelectorAll('.pane').forEach(p=>p.hidden=(p.id!=='pane-'+b.dataset.p));if(b.dataset.p==='mj'&&!window.__mjInit){window.__mjInit=1;initMJ();}else renderActive();}));
function initMJ(){document.getElementById('mjq').addEventListener('input',()=>renderMJ());
  const fb=document.getElementById('mjf');fb.addEventListener('click',()=>{mjOnlyBad=!mjOnlyBad;fb.setAttribute('aria-pressed',mjOnlyBad);fb.style.background=mjOnlyBad?cv('--wrs'):'';fb.style.color=mjOnlyBad?cv('--wr'):'';renderMJ();});
  document.getElementById('mjclr').addEventListener('click',()=>{mjFilt={};document.getElementById('mjq').value='';mjOnlyBad=false;const f=document.getElementById('mjf');f.setAttribute('aria-pressed',false);f.style.background='';f.style.color='';buildHead();renderMJ();});
  const bf=document.getElementById('bulkfield');bf.innerHTML=BFIELDS.map(f=>'<option value="'+f[0]+'">'+f[1]+'</option>').join('');bf.addEventListener('change',buildBulkVal);buildBulkVal();
  document.getElementById('bulkclear').addEventListener('click',()=>{mjSel.clear();renderMJ();updateBulk();});
  document.getElementById('bulkapply').addEventListener('click',()=>{const k=bf.value,v=document.getElementById('bulkval').value;if(!mjSel.size)return;mjSel.forEach(id=>{const r=P.mj.find(x=>x.id===id);if(!r)return;let val=v;if(BFIELDS.find(x=>x[0]===k)[2]==='date')val=val||null;r[k]=val;if(r._imp){}else{EDITS[id]=EDITS[id]||{};EDITS[id][k]=val;}});try{localStorage.setItem('ruche_mj_edits',JSON.stringify(EDITS));}catch(e){}persistImports();recomputeFlags();markDirty();renderLive();renderMJ();updateBulk();});
  renderLive();renderMJ();}
document.getElementById('impfile').addEventListener('change',async e=>{const files=[].slice.call(e.target.files||[]);if(!files.length)return;
  if(WEBHOOK){ await importFiles(files); e.target.value=''; return; }
  // fallback local (sem webhook): processa 1 a 1 pelo mapeamento manual
  var f=files[0],nm=f.name||'';
  if(/\.(xls|xlsx|xlsm)$/i.test(nm)){if(typeof XLSX==='undefined'){toast('Leitor de Excel indisponível.');e.target.value='';return;}const rb=new FileReader();rb.onload=()=>{try{const wb=XLSX.read(new Uint8Array(rb.result),{type:'array'});const ws=wb.Sheets[wb.SheetNames[0]];routeImport(XLSX.utils.sheet_to_json(ws,{header:1,raw:true,defval:''}),nm);}catch(err){toast('Erro: '+err.message);}};rb.readAsArrayBuffer(f);e.target.value='';return;}
  const rd=new FileReader();rd.onload=()=>{try{const txt=rd.result;const dl=detectDelim((txt.replace(/^﻿/,'').split(/\r?\n/)[0]||''));routeImport(parseCSV(txt,dl),nm);}catch(err){toast('Erro: '+err.message);}};rd.readAsText(f);e.target.value='';});
document.getElementById('impdo').addEventListener('click',doImport);
document.getElementById('impcancel').addEventListener('click',closeImport);
document.getElementById('exp').addEventListener('click',async()=>{const cols=['Date Added','Name','Payment Method','Outflow (USD)','Inflow (USD)','Currency (BRL)','Chart of Accounts','Account','Empresa','Due Date','Payment Date','Available','Period','Notes','Reconciled'];const q=v=>'"'+String(v==null?'':v).replace(/"/g,'""')+'"';const lines=[cols.join(',')];P.mj.forEach(r=>lines.push([r.da,r.nm,r.pm,r.o,r.i,r.b,r.ct,r.ac,r.emp,r.du,r.pd,r.av,r.pe,r.nt,r.rc].map(q).join(',')));const csv='﻿'+lines.join('\n');const dl=await (window.claude&&claude.use?claude.use('downloads'):Promise.resolve(null));if(dl){try{await dl.save({filename:'Master_Journal_Ruche.csv',data:csv});}catch(e){if(e&&e.code==='extension_not_enabled'){try{await dl.save({filename:'Master_Journal_Ruche.txt',data:csv});}catch(e2){if(e2&&e2.code!=='declined')toast('Não foi possível salvar: '+(e2.message||e2.code||e2));}}else if(e&&e.code!=='declined')toast('Não foi possível salvar: '+(e.message||e.code||e));}}else{try{const b=new Blob([csv],{type:'text/csv'});const u=URL.createObjectURL(b);const a=document.createElement('a');a.href=u;a.download='Master_Journal_Ruche.csv';a.click();URL.revokeObjectURL(u);}catch(e){}}});
let _discArm=false,_discT;document.getElementById('disc').addEventListener('click',()=>{const b=document.getElementById('disc');if(!_discArm){_discArm=true;b.textContent='Confirmar descarte?';toast('Clique de novo para descartar todas as edições e importações.');_discT=setTimeout(()=>{_discArm=false;b.textContent='Descartar edições';},4000);return;}clearTimeout(_discT);EDITS={};try{localStorage.removeItem('ruche_mj_edits');localStorage.removeItem('ruche_mj_imports');}catch(e){}location.reload();});
matchMedia('(prefers-color-scheme:dark)').addEventListener('change',renderActive);new MutationObserver(renderActive).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
(function(){var KEY='ruche_theme';function eff(){var t=document.documentElement.getAttribute('data-theme');if(t)return t;return matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';}
 function setIcon(){var b=document.getElementById('themebtn');if(b)b.textContent=eff()==='dark'?'☀️':'🌙';}
 try{var s=localStorage.getItem(KEY);if(s==='light'||s==='dark')document.documentElement.setAttribute('data-theme',s);}catch(e){}
 setIcon();
 var b=document.getElementById('themebtn');if(b)b.addEventListener('click',function(){var n=eff()==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',n);try{localStorage.setItem(KEY,n);}catch(e){}setIcon();});})();
recomputeFlags();buildHist();markDirty();renderResumo();addEventListener('resize',ht);
</script>'''
base=HTML.replace('__PAYLOAD__',DATA)
_xlsx=open(f"{SP}/xlsx.full.js",encoding="utf-8").read().replace('\ufffd','\\ufffd').replace('</script','<\\/script')
import os
WEBHOOK_URL="https://webhook.ruchedigital.online/webhook/import-extrato"
CDN_XLSX='<script src="https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js"></script>'
# 1) artifact (parsing local, SheetJS inline, sem webhook)
p1="/Users/apple/Desktop/stripe-conciliacao/central-financeira-ruche.html"
open(p1,"w",encoding="utf-8").write(base.replace('__WEBHOOK__','null').replace('__XLSXLOADER__','<script>'+_xlsx+'</script>'))
print("gerado (artifact):",round(os.path.getsize(p1)/1024),"KB")
# 2) hospedado (chama o n8n; SheetJS via CDN — hospedado não tem CSP)
p2="/Users/apple/Desktop/stripe-conciliacao/central-financeira-ruche-hosted.html"
open(p2,"w",encoding="utf-8").write(base.replace('__WEBHOOK__', '"'+WEBHOOK_URL+'"').replace('__XLSXLOADER__',CDN_XLSX))
print("gerado (hosted):",round(os.path.getsize(p2)/1024),"KB")
