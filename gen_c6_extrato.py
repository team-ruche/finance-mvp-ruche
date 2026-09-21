import json,re,os
SP=os.path.dirname(os.path.abspath(__file__))
core=open(f'{SP}/importer_core.js',encoding='utf-8').read()
core=re.sub(r"if\(typeof module.*$","",core,flags=re.S).strip()
ptax=open(f'{SP}/ptax.json',encoding='utf-8').read()
plano=open(f'{SP}/plano.json',encoding='utf-8').read()
histcat=open(f'{SP}/histcat.json',encoding='utf-8').read()
histnotes=open(f'{SP}/histnotes.json',encoding='utf-8').read()

# ---- Code node: de-para do JSON real de /statement (VISÍVEL/EDITÁVEL) + regras do core ----
codeNode = (
"// ===== C6 /statement -> linhas do Master Journal =====\n"
"// Requisicao confirmada pelo Roteiro de Testes v3.0: GET /statement, escopo statement.read,\n"
"// params start_date/end_date (YYYY-MM-DD, max 30 dias), header Authorization: Bearer {token}.\n"
"// >>> O ESQUEMA DA RESPOSTA (nomes dos campos) fica na pagina da API (login). AJUSTAR o de-para abaixo. <<<\n"
"const PTAX = " + ptax + ";\n"
"const PLANO = " + plano + ";\n"
"const HISTCAT = " + histcat + ";\n"
"const HISTNOTES = " + histnotes + ";\n"
+ core + "\n"
"const imp = buildImporter(PTAX, PLANO, HISTCAT, HISTNOTES);\n"
"\n"
"// 1) corpo da resposta do no 'C6 · GET /statement'\n"
"const body = $input.first().json;\n"
"// CONFIRMAR: onde fica a lista de lancamentos (ex.: body.transactions / body.entries / body.data / body.movements)\n"
"const raw = body.transactions || body.entries || body.movements || body.lancamentos || body.data || (Array.isArray(body) ? body : []);\n"
"\n"
"// 2) de-para dos campos — TROCAR pelos nomes reais do JSON de /statement\n"
"function toIso(d){ if(!d) return null; if(/^\\d{4}-\\d{2}-\\d{2}/.test(d)) return String(d).slice(0,10);\n"
"  const m=String(d).match(/(\\d{2})\\/(\\d{2})\\/(\\d{4})/); return m? m[3]+'-'+m[2]+'-'+m[1] : null; }\n"
"const norm = raw.map(t => ({\n"
"  da:   toIso(t.date || t.data || t.postingDate || t.transactionDate || t.dataLancamento),  // CONFIRMAR\n"
"  val:  Number(t.amount ?? t.valor ?? t.value),                                             // CONFIRMAR (+ entrada / - saida)\n"
"  desc: t.description || t.descricao || t.historico || t.memo || t.counterparty || '',      // CONFIRMAR\n"
"  tipo: t.type || t.tipo || t.transactionType || t.entryType || ''                          // CONFIRMAR ('Entrada/Saida/Pagamento/...')\n"
"})).filter(x => x.da && !isNaN(x.val));\n"
"\n"
"// 3) PTAX + sinal-pelo-Tipo + classificacao + historico (mesmas regras dos outros bancos)\n"
"const res = imp.runC6Extrato(norm, 'C6 - CC');\n"
"return res.rows.map(r => ({ json: r }));\n"
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
"### FALTA preencher\n"
"1. **Nomes dos campos** do JSON de /statement → ajustar o de-para no nó *Mapear* (baixar o **OpenAPI** na página da API).\n"
"2. Confirmar o **caminho do /auth** (assumido `/v1/auth`) na página APIs → Auth / no OpenAPI.\n"
"3. **Certificado mTLS** → importar no nó HTTP — ver nota ao lado.\n"
"4. **Segredos** em env do n8n (`C6_CLIENT_ID`, `C6_CLIENT_SECRET`) ou credencial — **nunca no git**.\n"
)
STICKY_MTLS = (
"### mTLS + segredos\n"
"- Certificado **.crt/.key** é **obrigatório** nas 2 chamadas.\n"
"- n8n self-hosted: configurar o **certificado cliente** no nó HTTP Request\n"
"  (Options → *SSL Certificates*) ou via HTTPS agent. Ver doc do n8n.\n"
"- Variáveis: **C6_BASE**, **C6_CLIENT_ID**, **C6_CLIENT_SECRET** nas *Environment Variables* do n8n.\n"
"  (Se o acesso a env estiver bloqueado, cole os valores direto no nó — menos seguro.)"
)

wf = {
  "name": "C6 - Extrato (integração) [ESQUELETO]",
  "nodes": [
    {"parameters":{"content":STICKY_MAIN,"height":470,"width":440,"color":6},
     "id":"note_main","name":"LEIA-ME","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[80,40]},
    {"parameters":{"content":STICKY_MTLS,"height":230,"width":340,"color":3},
     "id":"note_mtls","name":"mTLS e segredos","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[560,-210]},
    {"parameters":{},
     "id":"trg_manual","name":"Executar manualmente","type":"n8n-nodes-base.manualTrigger","typeVersion":1,"position":[560,120]},
    {"parameters":{
        "method":"POST",
        "url":"https://baas-api-sandbox.c6bank.info/v1/auth",
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
        "url":"https://baas-api-sandbox.c6bank.info/v1/statement",
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
     "id":"code_map","name":"Mapear /statement → Master Journal","type":"n8n-nodes-base.code","typeVersion":2,"position":[1220,120]}
  ],
  "connections": {
    "Executar manualmente":{"main":[[{"node":"C6 · POST /auth","type":"main","index":0}]]},
    "C6 · POST /auth":{"main":[[{"node":"C6 · GET /statement","type":"main","index":0}]]},
    "C6 · GET /statement":{"main":[[{"node":"Mapear /statement → Master Journal","type":"main","index":0}]]}
  },
  "settings":{"executionOrder":"v1"},
  "active": False
}
out=f'{SP}/C6 - Extrato (integracao).json'
open(out,'w',encoding='utf-8').write(json.dumps(wf,ensure_ascii=False,indent=1))
open(f'{SP}/_c6_codenode.js','w',encoding='utf-8').write(codeNode)
print('gerado:',out, round(os.path.getsize(out)/1024),'KB')
