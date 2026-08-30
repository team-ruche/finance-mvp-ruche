import json,re
SP='/private/tmp/claude-501/-Users-apple-Desktop-stripe-conciliacao/7e6c6c9a-350a-44b9-bedd-60c2d17fdb42/scratchpad'
core=open(f'{SP}/importer_core.js',encoding='utf-8').read()
# strip the module.exports line (n8n has no module)
core=re.sub(r"if\(typeof module.*$","",core,flags=re.S).strip()
ptax=open(f'{SP}/ptax.json',encoding='utf-8').read()
plano=open(f'{SP}/plano.json',encoding='utf-8').read()
histcat=open(f'{SP}/histcat.json',encoding='utf-8').read()
histnotes=open(f'{SP}/histnotes.json',encoding='utf-8').read()

jsCode = (
"// ===== Importador Universal Ruche — todas as regras dos handoffs =====\n"
"const PTAX = " + ptax + ";\n"
"const PLANO = " + plano + ";\n"
"const HISTCAT = " + histcat + ";\n"
"const HISTNOTES = " + histnotes + ";\n"
+ core + "\n"
"// ---- driver: lê body do webhook, aplica regras, devolve linhas ----\n"
"const _in = $input.first().json;\n"
"let body = _in && _in.body !== undefined ? _in.body : _in;\n"
"if (typeof body === 'string') { try { body = JSON.parse(body); } catch(e) { body = {}; } }\n"
"const rows = (body && body.rows) || [];\n"
"const filename = (body && (body.filename || body.fname)) || '';\n"
"const imp = buildImporter(PTAX, PLANO, HISTCAT, HISTNOTES);\n"
"const _txt = body && (body.text || body.pdftext);\n"
"const res = _txt ? imp.runImportText(_txt, filename) : imp.runImport(rows, filename);\n"
"return [{ json: res }];\n"
)

wf = {
  "name": "BD - Importador Universal (extrato → linhas)",
  "nodes": [
    {"parameters":{"httpMethod":"POST","path":"import-extrato","responseMode":"responseNode",
                   "options":{"allowedOrigins":"*"}},
     "id":"webhk0001","name":"Webhook (POST extrato)","type":"n8n-nodes-base.webhook","typeVersion":2,
     "position":[240,300],"webhookId":"import-extrato"},
    {"parameters":{"jsCode":jsCode},
     "id":"code00001","name":"Aplicar regras (datas/PTAX/plano)","type":"n8n-nodes-base.code","typeVersion":2,
     "position":[520,300]},
    {"parameters":{"respondWith":"firstIncomingItem",
                   "options":{"responseHeaders":{"entries":[
                       {"name":"Access-Control-Allow-Origin","value":"*"},
                       {"name":"Access-Control-Allow-Headers","value":"*"}]}}},
     "id":"resp00001","name":"Responder à página","type":"n8n-nodes-base.respondToWebhook","typeVersion":1,
     "position":[800,300]}
  ],
  "connections": {
    "Webhook (POST extrato)":{"main":[[{"node":"Aplicar regras (datas/PTAX/plano)","type":"main","index":0}]]},
    "Aplicar regras (datas/PTAX/plano)":{"main":[[{"node":"Responder à página","type":"main","index":0}]]}
  },
  "settings":{"executionOrder":"v1"},
  "active": False
}
out=f'/Users/apple/Desktop/stripe-conciliacao/BD - Importador Universal.json'
open(out,'w',encoding='utf-8').write(json.dumps(wf,ensure_ascii=False,indent=1))
# also write the pure jsCode for node --check
open(f'{SP}/_codenode.js','w',encoding='utf-8').write(jsCode)
import os;print('gerado:',out, round(os.path.getsize(out)/1024),'KB')
