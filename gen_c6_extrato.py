import json,re,os
SP=os.path.dirname(os.path.abspath(__file__))
core=open(f'{SP}/importer_core.js',encoding='utf-8').read()
core=re.sub(r"if\(typeof module.*$","",core,flags=re.S).strip()
ptax=open(f'{SP}/ptax.json',encoding='utf-8').read()
plano=open(f'{SP}/plano.json',encoding='utf-8').read()
histcat=open(f'{SP}/histcat.json',encoding='utf-8').read()
histnotes=open(f'{SP}/histnotes.json',encoding='utf-8').read()
sha1js=open(f'{SP}/_sha1.js',encoding='utf-8').read()

# ---- Code node: C6 /statement -> linhas do finance_journal (com dedup) ----
codeNode = (
"// ===== C6 /statement -> finance_journal =====\n"
"// De-para conforme OpenAPI 'Extrato' v1.0.0 (StatementResponse/Entries) + esquema finance_journal.\n"
"// Sinal vem de operation_type (amount e sempre positivo). Grava via upsert on_conflict=dedup_key.\n"
"const PTAX = " + ptax + ";\n"
"const PLANO = " + plano + ";\n"
"const HISTCAT = " + histcat + ";\n"
"const HISTNOTES = " + histnotes + ";\n"
+ sha1js + "\n"
+ core + "\n"
"const imp = buildImporter(PTAX, PLANO, HISTCAT, HISTNOTES);\n"
"const r2 = n => Math.round((Number(n)||0)*100)/100;\n"
"\n"
"// 1) corpo da resposta do no 'C6 · GET /statement'\n"
"const body = $input.first().json;\n"
"const raw = Array.isArray(body.entries) ? body.entries : (Array.isArray(body) ? body : []);\n"
"\n"
"// 2) de-para dos campos reais do C6\n"
"const num = s => { const n = Number(String(s).replace(/\\.(?=\\d{3}\\b)/g,'').replace(',', '.')); return isNaN(Number(s)) ? n : Number(s); };\n"
"const PIX_TT = /PIX|QRCODE/i, TRANSFER_TT = /TRANSFER/i, CARD_TT = /CARD_SALE|TAG|PARKY|TAGGY/i;\n"
"const norm = raw.map(t => {\n"
"  const income = String(t.operation_type).toUpperCase() === 'INCOMING';\n"
"  const tt = String(t.transaction_type || '');\n"
"  const pm = PIX_TT.test(tt) ? 'Pix' : (TRANSFER_TT.test(tt) ? 'Transferência' : (CARD_TT.test(tt) ? 'Cartão' : (income ? '' : 'Débito')));\n"
"  const desc = [t.title, t.description].filter(Boolean).join(' — ');\n"
"  return {\n"
"    da:   String(t.entry_date || '').slice(0,10),\n"
"    val:  num(t.amount),\n"
"    desc: desc,\n"
"    tipo: income ? 'Entrada' : 'Saída',\n"
"    pm:   pm,\n"
"    ref:  t.reference || t.local_reference || '',\n"
"    ttype: tt\n"
"  };\n"
"}).filter(x => /^\\d{4}-\\d{2}-\\d{2}$/.test(x.da) && !isNaN(x.val));\n"
"\n"
"// 3) PTAX + sinal-pelo-Tipo + classificacao + historico\n"
"const res = imp.runC6Extrato(norm, 'C6 - CC');\n"
"\n"
"// 4) mapeia para o esquema finance_journal (igual Stripe/Asaas), com dedup_key\n"
"const rows = res.rows.map(r => {\n"
"  const inflow = r2(r.i||0), outflow = r2(r.o||0), brl = r2(r.b||0);\n"
"  const usd = inflow > 0 ? inflow : outflow;\n"
"  const amount_usd = brl < 0 ? -outflow : inflow;\n"
"  const ptax = usd > 0 ? Math.round(Math.abs(brl)/usd*10000)/10000 : null;\n"
"  const ct = String(r.ct||''); const code = ct.split(' - ')[0].trim(); const cname = ct.split(' - ').slice(1).join(' - ').trim();\n"
"  const income = brl >= 0;\n"
"  const ref = r.ref || (r.pd + '|' + brl.toFixed(2) + '|' + (r.nm||''));\n"
"  return {\n"
"    period: String(r.pe || r.pd || '').slice(0,7),\n"
"    txn_date: r.pd, payment_date: r.pd,\n"
"    source: 'C6 - CC', account: 'C6 CC (BRL)',\n"
"    counterparty: r.nm || '', description: r.nt || r.nm || '',\n"
"    payment_method: r.pm || '',\n"
"    inflow: inflow, outflow: outflow,\n"
"    native_amount: brl, native_currency: 'BRL', ptax: ptax,\n"
"    amount_usd: amount_usd, amount_brl: brl,\n"
"    account_code: code, account_name: cname,\n"
"    status: income ? 'Received' : 'Paid',\n"
"    notes: '[auto-c6] ' + (r.ttype||'') + ' ' + (r.ref||''),\n"
"    dedup_key: sha1('c6:' + ref)\n"
"  };\n"
"});\n"
"return [{ json: { rows, count: rows.length } }];\n"
)

STICKY_MAIN = (
"## C6 · Extrato → Master Journal  (ESQUELETO — INATIVO)\n\n"
"Fonte: **Roteiro de Testes C6 Developers v3.0** (conta PJ confirmada).\n\n"
"### CONFIRMADO no roteiro\n"
"- **Auth:** POST **/auth** · `Content-Type: application/x-www-form-urlencoded`\n"
"  body: `client_id`, `client_secret`, `grant_type=client_credentials`\n"
"  → resposta `{access_token, expires_in:300, token_type:\"Bearer\", scope}` (token vale **5 min**)\n"
"- **Extrato:** GET **/statement** · escopo **`statement.read`**\n"
"  params **`start_date`** e **`end_date`** (YYYY-MM-DD, **máx. 30 dias**)\n"
"  header `Authorization: Bearer {token}`\n"
"- ⚠️ **mTLS obrigatório** — certificado **.crt/.key** que vem com as credenciais.\n\n"
"### Hosts (do portal)\n"
"- **Sandbox:** `https://baas-api-sandbox.c6bank.info/v1` (já preenchido)\n"
"- **Produção:** `https://baas-api.c6bank.info/v1` (trocar ao ir pra prod)\n\n"
"### Schema da resposta (OpenAPI v1.0.0) — já mapeado\n"
"`{entries:[{entry_date, amount(+), operation_type(INCOMING/OUTGOING), transaction_type, title, description}]}`\n"
"Sinal vem de **operation_type** (amount é sempre positivo). Já tratado no nó *Mapear*.\n\n"
"### Auth confirmado (OpenAPI v1.1.2)\n"
"POST `/v1/auth` (form-urlencoded) → `{access_token, expires_in:300, token_type, scope}`. Token expira em ~10 min. Sandbox seg-sex 07-22h.\n\n"
"### FALTA preencher (só isto)\n"
"1. **Certificado mTLS** (.crt/.key, vem junto das credenciais sandbox) → importar nos 2 nós HTTP — ver nota ao lado.\n"
"2. **Segredos** `C6_CLIENT_ID`/`C6_CLIENT_SECRET` em env do n8n ou credencial — **nunca no git**.\n"
)
STICKY_MTLS = (
"### mTLS via PROXY nginx (validado 22/09)\n"
"- Testado por fora: mTLS + /auth 200 + escopo statement.read OK.\n"
"- n8n **não** apresenta certificado cliente nativamente → usar **proxy nginx**\n"
"  que apresenta o .crt/.key ao C6. n8n chama o proxy em texto puro.\n"
"- Definir env **C6_BASE** = URL do proxy, ex.: `http://127.0.0.1:8686/v1`\n"
"  (sandbox) — trocar upstream do proxy p/ produção depois.\n"
"- Segredos **C6_CLIENT_ID**/**C6_CLIENT_SECRET** em env do n8n (nunca no git).\n"
"- Config do proxy: `c6-proxy.nginx.conf` no repo."
)

wf = {
  "name": "C6 - Extrato (integração)",
  "nodes": [
    {"parameters":{"content":STICKY_MAIN,"height":470,"width":440,"color":6},
     "id":"note_main","name":"LEIA-ME","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[80,40]},
    {"parameters":{"content":STICKY_MTLS,"height":230,"width":340,"color":3},
     "id":"note_mtls","name":"mTLS e segredos","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[560,-210]},
    {"parameters":{},
     "id":"trg_manual","name":"Executar manualmente","type":"n8n-nodes-base.manualTrigger","typeVersion":1,"position":[560,120]},
    {"parameters":{
        "method":"POST",
        "url":"={{ $env.C6_BASE }}/auth",
        "sendHeaders":True,
        "headerParameters":{"parameters":[{"name":"Content-Type","value":"application/x-www-form-urlencoded"}]},
        "sendBody":True,
        "contentType":"form-urlencoded",
        "bodyParameters":{"parameters":[
            {"name":"grant_type","value":"client_credentials"},
            {"name":"client_id","value":"={{ $env.C6_CLIENT_ID }}"},
            {"name":"client_secret","value":"={{ $env.C6_CLIENT_SECRET }}"}
        ]},
        "options":{}
     },
     "id":"http_auth","name":"C6 · POST /auth","type":"n8n-nodes-base.httpRequest","typeVersion":4.2,"position":[780,120],
     "notes":"mTLS: importar certificado .crt/.key (Options → SSL)"},
    {"parameters":{
        "method":"GET",
        "url":"={{ $env.C6_BASE }}/statement",
        "sendHeaders":True,
        "headerParameters":{"parameters":[{"name":"Authorization","value":"=Bearer {{ $json.access_token }}"}]},
        "sendQuery":True,
        "queryParameters":{"parameters":[
            {"name":"start_date","value":"={{ $today.minus({days:30}).toFormat('yyyy-MM-dd') }}"},
            {"name":"end_date","value":"={{ $today.toFormat('yyyy-MM-dd') }}"}
        ]},
        "options":{}
     },
     "id":"http_stmt","name":"C6 · GET /statement","type":"n8n-nodes-base.httpRequest","typeVersion":4.2,"position":[1000,120],
     "notes":"mTLS: mesmo certificado. Escopo statement.read. Máx 30 dias."},
    {"parameters":{"jsCode":codeNode},
     "id":"code_map","name":"Montar linhas (finance_journal)","type":"n8n-nodes-base.code","typeVersion":2,"position":[1220,120]},
    {"parameters":{
        "method":"POST",
        "url":"https://api.ruchedigital.com/rest/v1/finance_journal?on_conflict=dedup_key",
        "authentication":"predefinedCredentialType",
        "nodeCredentialType":"supabaseApi",
        "sendHeaders":True,
        "headerParameters":{"parameters":[
            {"name":"Prefer","value":"resolution=merge-duplicates,return=representation"},
            {"name":"Content-Type","value":"application/json"}]},
        "sendBody":True,
        "contentType":"raw",
        "rawContentType":"application/json",
        "body":"={{ JSON.stringify($json.rows) }}",
        "options":{"response":{"response":{"neverError":True,"fullResponse":True}}}
     },
     "id":"sb_upsert","name":"Supabase upsert (finance_journal)","type":"n8n-nodes-base.httpRequest","typeVersion":4.2,"position":[1440,120],
     "credentials":{"supabaseApi":{"id":"9Sq6hZefK0R6kZhu","name":"BD - Supabase Self-Hosted (supabaseApi)"}}}
  ],
  "connections": {
    "Executar manualmente":{"main":[[{"node":"C6 · POST /auth","type":"main","index":0}]]},
    "C6 · POST /auth":{"main":[[{"node":"C6 · GET /statement","type":"main","index":0}]]},
    "C6 · GET /statement":{"main":[[{"node":"Montar linhas (finance_journal)","type":"main","index":0}]]},
    "Montar linhas (finance_journal)":{"main":[[{"node":"Supabase upsert (finance_journal)","type":"main","index":0}]]}
  },
  "settings":{"executionOrder":"v1"},
  "active": False
}
out=f'{SP}/C6 - Extrato (integracao).json'
open(out,'w',encoding='utf-8').write(json.dumps(wf,ensure_ascii=False,indent=1))
open(f'{SP}/_c6_codenode.js','w',encoding='utf-8').write(codeNode)
print('gerado:',out, round(os.path.getsize(out)/1024),'KB')
