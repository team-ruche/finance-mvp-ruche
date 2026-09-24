import json,re,os
SP=os.path.dirname(os.path.abspath(__file__))
core=open(f'{SP}/importer_core.js',encoding='utf-8').read()
core=re.sub(r"if\(typeof module.*$","",core,flags=re.S).strip()
ptax=open(f'{SP}/ptax.json',encoding='utf-8').read()
plano=open(f'{SP}/plano.json',encoding='utf-8').read()
histcat=open(f'{SP}/histcat.json',encoding='utf-8').read()
histnotes=open(f'{SP}/histnotes.json',encoding='utf-8').read()
sha1js=open(f'{SP}/_sha1.js',encoding='utf-8').read()

codeNode = (
"// ===== BoA (Plaid) -> finance_journal =====\n"
"// Chama /transactions/sync (incremental via cursor guardado no static data), mapeia p/ finance_journal\n"
"// e devolve { rows } p/ upsert. Convencao BoA: USD puro (native_currency=USD, amount_brl/ptax=null).\n"
"// Plaid: amount>0 = SAIDA, amount<0 = ENTRADA -> invertemos para a convencao interna (+ entrada).\n"
"const PTAX = " + ptax + ";\n"
"const PLANO = " + plano + ";\n"
"const HISTCAT = " + histcat + ";\n"
"const HISTNOTES = " + histnotes + ";\n"
+ sha1js + "\n"
+ core + "\n"
"const imp = buildImporter(PTAX, PLANO, HISTCAT, HISTNOTES);\n"
"const r2 = n => Math.round((Number(n)||0)*100)/100;\n"
"\n"
"const BASE = process.env.PLAID_BASE || 'https://sandbox.plaid.com';\n"
"const client_id = process.env.PLAID_CLIENT_ID;\n"
"const secret = process.env.PLAID_SECRET;\n"
"const access_token = process.env.PLAID_BOA_ACCESS_TOKEN;\n"
"if (!client_id || !secret || !access_token) { throw new Error('Faltam variaveis PLAID_CLIENT_ID / PLAID_SECRET / PLAID_BOA_ACCESS_TOKEN no n8n'); }\n"
"\n"
"const store = $getWorkflowStaticData('global');\n"
"let cursor = store.boa_cursor || null;\n"
"let added = [], modified = [], hasMore = true, guard = 0;\n"
"while (hasMore && guard < 50) {\n"
"  guard++;\n"
"  const body = { client_id, secret, access_token, count: 500 };\n"
"  if (cursor) body.cursor = cursor;\n"
"  const resp = await fetch(BASE + '/transactions/sync', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body) });\n"
"  const j = await resp.json();\n"
"  if (!resp.ok) { throw new Error('Plaid ' + resp.status + ': ' + JSON.stringify(j).slice(0,300)); }\n"
"  added = added.concat(j.added || []);\n"
"  modified = modified.concat(j.modified || []);\n"
"  cursor = j.next_cursor; hasMore = j.has_more;\n"
"}\n"
"store.boa_cursor = cursor;  // persiste p/ a proxima execucao (so traz o que mudou)\n"
"\n"
"const txs = added.concat(modified);\n"
"const norm = txs.map(t => ({\n"
"  da:   String(t.date || t.authorized_date || '').slice(0,10),\n"
"  amt:  -Number(t.amount),                 // Plaid +saida -> interna +entrada\n"
"  nm:   t.merchant_name || t.name || '',\n"
"  nt:   t.name || '',\n"
"  ref:  t.transaction_id,\n"
"  ttype:(t.personal_finance_category && t.personal_finance_category.primary) || ''\n"
"})).filter(x => /^\\d{4}-\\d{2}-\\d{2}$/.test(x.da) && !isNaN(x.amt));\n"
"\n"
"const res = imp.runBoAPlaid(norm);\n"
"const rows = res.rows.map(r => {\n"
"  const inflow = r2(r.i||0), outflow = r2(r.o||0);\n"
"  const amount_usd = inflow > 0 ? inflow : -outflow;\n"
"  const ct = String(r.ct||''); const code = ct.split(' - ')[0].trim(); const cname = ct.split(' - ').slice(1).join(' - ').trim();\n"
"  const income = amount_usd >= 0;\n"
"  const ref = r.ref || (r.pd + '|' + amount_usd.toFixed(2) + '|' + (r.nm||''));\n"
"  return {\n"
"    period: String(r.pe || r.pd || '').slice(0,7),\n"
"    txn_date: r.pd, payment_date: r.pd,\n"
"    source: 'BoA', account: 'BoA (USD)',\n"
"    counterparty: r.nm || '', description: r.nt || r.nm || '',\n"
"    payment_method: r.pm || '',\n"
"    inflow: inflow, outflow: outflow,\n"
"    native_amount: amount_usd, native_currency: 'USD', ptax: null,\n"
"    amount_usd: amount_usd, amount_brl: null,\n"
"    account_code: code, account_name: cname,\n"
"    status: income ? 'Received' : 'Paid',\n"
"    notes: (r.nt||''),\n"
"    dedup_key: sha1('boa:' + ref)\n"
"  };\n"
"});\n"
"return [{ json: { rows, count: rows.length, cursor } }];\n"
)

STICKY = (
"## BoA (Plaid) → finance_journal  (aguardando access_token)\n\n"
"Puxa o extrato do **Bank of America via Plaid** (`/transactions/sync`) e grava no `finance_journal` (upsert, dedup).\n\n"
"### Variáveis no n8n (Environment)\n"
"- **PLAID_BASE** = `https://sandbox.plaid.com` (teste) / `https://production.plaid.com` (prod)\n"
"- **PLAID_CLIENT_ID**, **PLAID_SECRET** (do painel Plaid → Keys)\n"
"- **PLAID_BOA_ACCESS_TOKEN** (gerado no Quickstart após conectar o BoA)\n\n"
"### Como funciona\n"
"- Cursor guardado no *static data* → 1ª execução traz o histórico, depois só o que mudou.\n"
"- Plaid: `amount>0` = saída, `amount<0` = entrada (já tratado).\n"
"- Convenção BoA: **USD puro** (native_currency=USD, amount_brl/ptax=null), source `BoA`, account `BoA (USD)`.\n"
"- dedup_key = sha1('boa:' + transaction_id).\n\n"
"### Sandbox tem dados fictícios → dá pra validar tudo antes da produção."
)

wf = {
  "name": "BoA - Extrato (Plaid → finance_journal)",
  "nodes": [
    {"parameters":{"content":STICKY,"height":360,"width":420,"color":6},
     "id":"note","name":"LEIA-ME","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[80,40]},
    {"parameters":{},
     "id":"trg","name":"Executar manualmente","type":"n8n-nodes-base.manualTrigger","typeVersion":1,"position":[560,140]},
    {"parameters":{"jsCode":codeNode},
     "id":"code","name":"Plaid sync → linhas (finance_journal)","type":"n8n-nodes-base.code","typeVersion":2,"position":[780,140]},
    {"parameters":{
        "method":"POST",
        "url":"https://api.ruchedigital.com/rest/v1/finance_journal?on_conflict=dedup_key",
        "authentication":"predefinedCredentialType",
        "nodeCredentialType":"supabaseApi",
        "sendHeaders":True,
        "headerParameters":{"parameters":[
            {"name":"Prefer","value":"resolution=merge-duplicates,return=representation"},
            {"name":"Content-Type","value":"application/json"}]},
        "sendBody":True,"contentType":"raw","rawContentType":"application/json",
        "body":"={{ JSON.stringify($json.rows) }}",
        "options":{"response":{"response":{"neverError":True,"fullResponse":True}}}
     },
     "id":"sb","name":"Supabase upsert (finance_journal)","type":"n8n-nodes-base.httpRequest","typeVersion":4.2,"position":[1020,140],
     "credentials":{"supabaseApi":{"id":"9Sq6hZefK0R6kZhu","name":"BD - Supabase Self-Hosted (supabaseApi)"}}}
  ],
  "connections": {
    "Executar manualmente":{"main":[[{"node":"Plaid sync → linhas (finance_journal)","type":"main","index":0}]]},
    "Plaid sync → linhas (finance_journal)":{"main":[[{"node":"Supabase upsert (finance_journal)","type":"main","index":0}]]}
  },
  "settings":{"executionOrder":"v1"},
  "active": False
}
out=f'{SP}/BoA - Extrato (Plaid).json'
open(out,'w',encoding='utf-8').write(json.dumps(wf,ensure_ascii=False,indent=1))
open(f'{SP}/_boa_codenode.js','w',encoding='utf-8').write(codeNode)
print('gerado:',out, round(os.path.getsize(out)/1024),'KB')
