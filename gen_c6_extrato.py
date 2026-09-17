import json,re,os
SP=os.path.dirname(os.path.abspath(__file__))
core=open(f'{SP}/importer_core.js',encoding='utf-8').read()
core=re.sub(r"if\(typeof module.*$","",core,flags=re.S).strip()
ptax=open(f'{SP}/ptax.json',encoding='utf-8').read()
plano=open(f'{SP}/plano.json',encoding='utf-8').read()
histcat=open(f'{SP}/histcat.json',encoding='utf-8').read()
histnotes=open(f'{SP}/histnotes.json',encoding='utf-8').read()

# ---- Code node: de-para do JSON real do C6 (VISÍVEL/EDITÁVEL) + regras do core ----
codeNode = (
"// ===== C6 Extrato -> linhas do Master Journal =====\n"
"// >>> AJUSTAR AQUI conforme o JSON REAL do extrato C6 (ver roteiro/Swagger). <<<\n"
"// Objetivo: transformar cada lançamento em {da:'YYYY-MM-DD', val:Number(±), desc, tipo}.\n"
"const PTAX = " + ptax + ";\n"
"const PLANO = " + plano + ";\n"
"const HISTCAT = " + histcat + ";\n"
"const HISTNOTES = " + histnotes + ";\n"
+ core + "\n"
"const imp = buildImporter(PTAX, PLANO, HISTCAT, HISTNOTES);\n"
"\n"
"// 1) pega o corpo da resposta da API C6 (o nó HTTP anterior)\n"
"const body = $input.first().json;\n"
"// CONFIRMAR: onde fica a lista de lançamentos no JSON do C6 (ex.: body.transactions / body.entries / body.data)\n"
"const raw = body.transactions || body.entries || body.lancamentos || body.data || (Array.isArray(body) ? body : []);\n"
"\n"
"// 2) de-para dos campos — TROCAR os nomes pelos campos reais do C6\n"
"function toIso(d){ if(!d) return null; if(/^\\d{4}-\\d{2}-\\d{2}/.test(d)) return d.slice(0,10);\n"
"  const m=String(d).match(/(\\d{2})\\/(\\d{2})\\/(\\d{4})/); return m? m[3]+'-'+m[2]+'-'+m[1] : null; }\n"
"const norm = raw.map(t => ({\n"
"  da:   toIso(t.date || t.data || t.postingDate || t.dataLancamento),        // CONFIRMAR\n"
"  val:  Number(t.amount ?? t.valor ?? t.value),                              // CONFIRMAR (sinal: + entrada / - saída)\n"
"  desc: t.description || t.descricao || t.historico || t.memo || '',         // CONFIRMAR\n"
"  tipo: t.type || t.tipo || t.transactionType || ''                          // CONFIRMAR ('Entrada/Saida/Pagamento/...')\n"
"})).filter(x => x.da && !isNaN(x.val));\n"
"\n"
"// 3) aplica PTAX + sinal-pelo-Tipo + classificação + histórico (mesmas regras dos outros bancos)\n"
"const res = imp.runC6Extrato(norm, 'C6 - CC');\n"
"return res.rows.map(r => ({ json: r }));\n"
)

STICKY_MAIN = (
"## C6 · Extrato → Master Journal  (ESQUELETO — INATIVO)\n\n"
"Pronto para completar **depois** de confirmar a conta PJ C6 com o Patrick.\n\n"
"### Checklist para ativar\n"
"1. **Conta PJ no C6** no mesmo CNPJ do Portal do Desenvolvedor (não MEI).\n"
"2. **Credencial OAuth2** (Client Credentials): criar em *Credentials → OAuth2 API*\n"
"   - Grant Type: **Client Credentials**\n"
"   - Token URL, Client ID, Client Secret, Scope: **do roteiro C6**\n"
"   - ⚠️ **Segredos SÓ aqui** (nunca no código/git).\n"
"3. No nó **C6 · GET Extrato**: preencher a **URL real** do endpoint de extrato\n"
"   e selecionar a credencial OAuth2 criada.\n"
"4. ⚠️ **mTLS**: se o C6 exigir **certificado cliente**, configurar em\n"
"   *HTTP Request → Options → SSL Certificates* (ou via env do n8n).\n"
"5. No nó **Mapear extrato**: ajustar o **de-para dos campos** conforme o JSON real.\n"
"6. Testar no **sandbox** (seg–sex, 7h–23h) e conferir os totais.\n"
)
STICKY_HTTP = ("### Preencher\n- **URL** do endpoint de extrato (roteiro C6)\n- **Credencial** OAuth2 (Client Credentials)\n- Query: datas início/fim (já sugeridas: últimos 35 dias)\n- **mTLS/certificado** se exigido")

wf = {
  "name": "C6 - Extrato (integração) [ESQUELETO]",
  "nodes": [
    {"parameters":{"content":STICKY_MAIN,"height":430,"width":420,"color":6},
     "id":"note_main","name":"LEIA-ME","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[120,60]},
    {"parameters":{"content":STICKY_HTTP,"height":220,"width":300,"color":5},
     "id":"note_http","name":"Config HTTP","type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[600,-140]},
    {"parameters":{},
     "id":"trg_manual","name":"Executar manualmente","type":"n8n-nodes-base.manualTrigger","typeVersion":1,"position":[600,120]},
    {"parameters":{
        "method":"GET",
        "url":"https://CONFIRMAR-no-roteiro-c6/extrato",
        "authentication":"genericCredentialType",
        "genericAuthType":"oAuth2Api",
        "sendQuery":True,
        "queryParameters":{"parameters":[
            {"name":"dataInicio","value":"={{ $today.minus({days:35}).toFormat('yyyy-MM-dd') }}"},
            {"name":"dataFim","value":"={{ $today.toFormat('yyyy-MM-dd') }}"}
        ]},
        "options":{}
     },
     "id":"http_extrato","name":"C6 · GET Extrato","type":"n8n-nodes-base.httpRequest","typeVersion":4.2,"position":[600,120],
     "notes":"Preencher URL real + credencial OAuth2 + (se preciso) certificado mTLS"},
    {"parameters":{"jsCode":codeNode},
     "id":"code_map","name":"Mapear extrato → Master Journal","type":"n8n-nodes-base.code","typeVersion":2,"position":[860,120]}
  ],
  "connections": {
    "Executar manualmente":{"main":[[{"node":"C6 · GET Extrato","type":"main","index":0}]]},
    "C6 · GET Extrato":{"main":[[{"node":"Mapear extrato → Master Journal","type":"main","index":0}]]}
  },
  "settings":{"executionOrder":"v1"},
  "active": False
}
# posiciona http e manual sem sobrepor
wf["nodes"][3]["position"]=[600,120]
wf["nodes"][2]["position"]=[380,300]
wf["nodes"][3]["position"]=[640,300]
wf["nodes"][4]["position"]=[900,300]
wf["nodes"][1]["position"]=[600,60]

out=f'{SP}/C6 - Extrato (integracao).json'
open(out,'w',encoding='utf-8').write(json.dumps(wf,ensure_ascii=False,indent=1))
open(f'{SP}/_c6_codenode.js','w',encoding='utf-8').write(codeNode)
print('gerado:',out, round(os.path.getsize(out)/1024),'KB')
