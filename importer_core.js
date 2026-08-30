// ===== Ruche importador universal — lógica portada do dashboard (regras dos handoffs) =====
// Exporta runImport(rows2d, filename) -> { account, bank, rows:[MJ rows] }
// PTAX e plano são injetados como globais PTAX e PLANO (no n8n ficam inline; aqui via require).
function buildImporter(PTAX, PLANO, HISTCAT, HISTNOTES){
  HISTCAT = HISTCAT || {}; HISTNOTES = HISTNOTES || {};
  function normName(nm){var s=(nm||'').toLowerCase();s=s.replace(/zelle payment (from|to)/g,' ').replace(/conf#\s*\w+/g,' ').replace(/\bmobile purchase\b|\bpurchase\b|\bwithdrwl\b|\bwithdrawal\b/g,' ').replace(/\bfor\b\s+"[^"]*"/g,' ').replace(/\d{2}\/\d{2}(\/\d{2,4})?/g,' ').replace(/[*#]/g,' ').replace(/\s+/g,' ').trim();return s;}
  function keynorm(s){s=(s||'').toLowerCase();s=s.replace(/\b\d[\d.\-/]*\b/g,' ').replace(/[·|].*$/,'').replace(/[^a-zà-ú ]/g,' ').replace(/\s+/g,' ').trim();return s;}
  function titlecase(s){s=String(s||'').toLowerCase().replace(/\s*\b(ltda|llc|inc|s\/a|sa|me|epp)\b\.?/gi,'').replace(/\b([a-zà-ú])/g,function(m,c){return c.toUpperCase();}).replace(/\s+/g,' ').trim();return s;}
  function refine(row){var k=keynorm(row.nt)||keynorm(row.nm);var h=k&&HISTNOTES[k];if(h){if(h.nm)row.nm=h.nm;if(h.ct&&PLANO.indexOf(h.ct)>=0)row.ct=h.ct;if(h.pm)row.pm=h.pm;}return row;}
  function r2(n){return Math.round((n+Number.EPSILON)*100)/100;}
  function pad2(n){return String(n).padStart(2,'0');}
  var _MON={jan:1,feb:2,mar:3,apr:4,may:5,jun:6,jul:7,aug:8,sep:9,oct:10,nov:11,dec:12,fev:2,abr:4,mai:5,ago:8,set:9,out:10,dez:12};
  function pnum(s){if(s==null||s==='')return null;if(typeof s==='number')return isFinite(s)?s:null;s=String(s).trim().replace(/[^\d.,-]/g,'');if(!s||s==='-'||s==='.'||s===',')return null;var neg=/-/.test(s);s=s.replace(/-/g,'');var lc=s.lastIndexOf(','),ld=s.lastIndexOf('.');if(lc>=0&&ld>=0){if(lc>ld)s=s.replace(/\./g,'').replace(',','.');else s=s.replace(/,/g,'');}else if(lc>=0){var af=s.length-lc-1;if(af===1||af===2)s=s.replace(',','.');else s=s.replace(/,/g,'');}var n=parseFloat(s);if(isNaN(n))return null;return neg?-n:n;}
  function pdate(s,order){if(s==null)return null;s=String(s).trim();if(!s)return null;var m=s.match(/(\d{4})-(\d{2})-(\d{2})/);if(m)return m[1]+'-'+m[2]+'-'+m[3];m=s.match(/(\d{1,2})[\/.\-\s]+([A-Za-zçÇ]{3,})[,\/.\-\s]+(\d{2,4})/);if(m){var mo=_MON[m[2].slice(0,3).toLowerCase()];if(mo){var y0=m[3].length===2?'20'+m[3]:m[3];return y0+'-'+pad2(mo)+'-'+pad2(+m[1]);}}m=s.match(/(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{2,4})/);if(m){var a=+m[1],b=+m[2],y=m[3];if(y.length===2)y='20'+y;var dd,mm;if(a>12){dd=a;mm=b;}else if(b>12){mm=a;dd=b;}else if(order==='mdy'){mm=a;dd=b;}else{dd=a;mm=b;}return y+'-'+pad2(mm)+'-'+pad2(dd);}return null;}
  function ptaxFor(d){if(!d||!PTAX)return null;if(PTAX[d])return PTAX[d];var ks=Object.keys(PTAX).sort();var last=null;for(var i=0;i<ks.length;i++){if(ks[i]<=d)last=PTAX[ks[i]];else break;}return last;}
  function mkrow(o){return Object.assign({da:null,nm:'',pm:'',o:0,i:0,b:0,ct:'',ac:'',emp:'Ruche Digital',du:null,pd:null,av:null,pe:null,nt:''},o||{});}
  function setBRL(row,signed,dt){var abs=Math.abs(signed),isIn=signed>=0,p=ptaxFor(dt),usd=p?r2(abs/p):0;row.b=r2(isIn?abs:-abs);if(isIn){row.i=usd;row.o=0;}else{row.o=usd;row.i=0;}return isIn;}
  function setUSD(row,signed,dt){var abs=Math.abs(signed),isIn=signed>=0,p=ptaxFor(dt),brl=p?r2(abs*p):0;row.b=isIn?brl:-brl;if(isIn){row.i=r2(abs);row.o=0;}else{row.o=r2(abs);row.i=0;}return isIn;}
  function colIdx(H,subs){for(var i=0;i<H.length;i++){var h=String(H[i]==null?'':H[i]).toLowerCase();for(var j=0;j<subs.length;j++)if(h.indexOf(subs[j])>=0)return i;}return -1;}
  function rowHas(row,subs){var s=(row||[]).map(function(x){return String(x==null?'':x).toLowerCase();}).join('~|~');return subs.every(function(t){return s.indexOf(t)>=0;});}
  function findHdr(rows,subs){for(var i=0;i<Math.min(rows.length,25);i++)if(rowHas(rows[i],subs))return i;return -1;}
  function invoiceDue(fname,vday){var m=String(fname||'').match(/(0?[1-9]|1[0-2])[ _.\-\/](20\d{2})/);if(!m)return null;return m[2]+'-'+pad2(+m[1])+'-'+pad2(vday);}
  function pmBoA(nm){nm=(nm||'').toLowerCase();if(/zelle/.test(nm))return 'Zelle';if(/atm|withdrwl|withdrawal/.test(nm))return 'ATM';if(/\btransfer\b/.test(nm))return 'Wire Transfer';if(/purchase|mobile/.test(nm))return 'Debit Card';return '';}
  function pmUniCC(nm){nm=(nm||'').toLowerCase();if(/pix/.test(nm))return 'Pix';if(/ted|tef|transferencia/.test(nm))return 'Transferência';if(/boleto|titulo|liquidacao/.test(nm))return 'Boleto';if(/pagamento|debito/.test(nm))return 'Débito';if(/credito|recebimento/.test(nm))return 'Crédito';return '';}
  function guessAccount(fn){fn=(fn||'').toLowerCase();if(/unicred|sicredi/.test(fn)){if(/cart|fatura/.test(fn))return 'Unicred - Cartão';if(/invest|rdc|rentab/.test(fn))return 'Unicred - Invest';return 'Unicred - CC';}if(/c6/.test(fn)){if(/cart|fatura/.test(fn))return 'C6 - Cartão';return 'C6 - CC';}if(/boa|bank ?of ?america|bofa/.test(fn))return 'BoA';if(/payoneer|payoner/.test(fn))return 'Payoneer';if(/wise/.test(fn))return 'Wise - Cris';if(/stripe/.test(fn))return 'Stripe';if(/asaas/.test(fn))return 'Asaas';return null;}
  var KWRULES=[[/arranjo debito|arranjo débito|cred dom|stripe brasil/i,'12.3.1 - Inter-Account Transfers'],[/pagamento fatura|pag fatura|pgto fatura|pagamento recebido|pagamento de fatura/i,'12.3.1 - Inter-Account Transfers'],[/ruche digital/i,'12.3.1 - Inter-Account Transfers'],[/taxa de (boleto|mensageria|cart|pix|transfer)/i,'3.2.4 - Other Gateway Fees','out'],[/facebook|facebk|meta ?ads/i,'5.1.1 - Paid Traffic — Ruche Acquisition'],[/highlevel|gohighlevel|ghl/i,'3.1.2 - CRM - usage-based'],[/twilio|sonetel/i,'3.1.1 - Twilio / Telephony'],[/openai|anthropic|claude|chatgpt|manus/i,'4.2.4 - AI Tools'],[/google workspace|hostinger|lovable|hetzner|dicloak/i,'4.2.5 - Infrastructure / Technology'],[/\biof\b/i,'5.2.18 - Card IOF'],[/aluguel|\brent\b/i,'5.2.1 - Rent'],[/contabil|accounting|ferreira/i,'5.2.8 - Accounting'],[/simples nacional/i,'2.4.1 - Simples Nacional / DAS'],[/stripe/i,'3.2.1 - Stripe Fees','out']];
  function classify(nm,nt,inflow){var cat=null;
    var raw=(nm||'').trim().toLowerCase(),n=normName(nm);
    if(HISTCAT[raw])cat=HISTCAT[raw];else if(n&&HISTCAT[n])cat=HISTCAT[n];
    if(!cat){var hay=(nm+' '+(nt||''));for(var k=0;k<KWRULES.length;k++){var kr=KWRULES[k];if(kr[2]==='out'&&inflow)continue;if(kr[0].test(hay)){cat=kr[1];break;}}}
    if(!cat||(PLANO&&PLANO.indexOf(cat)<0))cat=inflow?'1.4.1 - Revenue to Classify':'5.4.1 - Expenses to Classify';return cat;}
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
  function parseBoA(rows,h){var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var amt=pnum(r[2]);if(amt==null)continue;var dt=pdate(r[0],'mdy');if(!dt)continue;var nm=String(r[1]==null?'':r[1]).trim();var row=mkrow({ac:'BoA',pm:pmBoA(nm),da:dt,pe:dt,du:dt,pd:dt,av:dt});var isIn=setUSD(row,amt,dt);row.nm=nm;row.ct=classify(nm,'',isIn);out.push(row);}return out;}
  function parsePayoneer(rows,h){var H=rows[h];var cD=colIdx(H,['date']),cN=colIdx(H,['description']),cA=colIdx(H,['amount']),cC=colIdx(H,['currency']),cT=colIdx(H,['transaction id','transaction']);var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var amt=pnum(r[cA]);if(amt==null)continue;var dt=pdate(r[cD],'dmy');if(!dt)continue;var nm=String((cN>=0?r[cN]:'')||'').trim();var cur=cC>=0?String(r[cC]||'').toUpperCase():'USD';var txn=cT>=0?String(r[cT]||'').trim():'';var row=mkrow({ac:'Payoneer',pm:'Payoneer',da:dt,pe:dt,du:dt,pd:dt,av:dt,nt:txn});var isIn=(cur==='BRL')?setBRL(row,amt,dt):setUSD(row,amt,dt);row.nm=nm;row.ct=classify(nm,txn,isIn);out.push(row);}return out;}
  function parseAsaas(rows,h){var H=rows[h];var cD=colIdx(H,['data']),cN=colIdx(H,['descri']),cV=colIdx(H,['valor']),cT=colIdx(H,['transação','transacao']);var out=[];for(var i=h+1;i<rows.length;i++){var r=rows[i];if(!r)continue;var dt=pdate(r[cD],'dmy');if(!dt)continue;var val=pnum(r[cV]);if(val==null)continue;
    var desc=String((cN>=0?r[cN]:'')||'').trim();
    var nm=desc,pm='';var mch=desc.match(/com chave para (.+)$/i);
    if(/taxa de/i.test(desc)){nm='Asaas';pm='Autopay';}
    else if(mch){nm=titlecase(mch[1]);pm='Pix';}
    else if(/cobran[çc]a recebida/i.test(desc)){var mp=desc.replace(/cobran[çc]a recebida\s*-?\s*fatura(\s+da cobrança)?\s*nr\.?\s*\d+\s*/i,'').trim();nm=titlecase(mp)||desc;pm='Fatura';}
    else if(/pix/i.test(desc)){pm='Pix';}
    var row=mkrow({ac:'Asaas',pm:pm,da:dt,pe:dt,du:dt,pd:dt,av:dt,nt:desc});var isIn=setBRL(row,val,dt);row.nm=nm;row.ct=classify(nm,desc,isIn);out.push(row);}return out;}
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
  function parseC6ccPDF(text){var L=text.split(/\r?\n/).map(function(s){return s.trim();}).filter(function(x){return x!=='';});var ym=text.match(/\d{2}\/\d{2}\/(20\d{2})/);var year=ym?ym[1]:'2026';var out=[];
    var tipos=/^(Entrada PIX|Sa[íi]da PIX|Entrada TED|Sa[íi]da TED|Pagamento|Entradas|Sa[íi]das|Transfer[eê]ncia|Estorno|Tarifa|D[ée]bito|Cr[ée]dito|Compra|Rendimento|Resgate|Aplica[çc][ãa]o)/i;
    // formato pdf.js: "DD/MM DD/MM Tipo Descrição R$ Valor" numa linha só
    var reOne=/^(\d{2})\/(\d{2})\s+\d{2}\/\d{2}\s+(.+?)\s+(-?\s*R\$\s*[\d.,]+)\s*$/;
    // formato pymupdf: DD/MM em linha isolada seguida de campos
    var isDM=function(s){return /^\d{2}\/\d{2}$/.test(s);};
    for(var i=0;i<L.length;i++){
      if(/^saldo do dia/i.test(L[i]))continue;
      var m=L[i].match(reOne),da,mid,val;
      if(m){da=year+'-'+m[2]+'-'+m[1];mid=m[3].trim();val=pnum(m[4]);}
      else if(isDM(L[i])&&isDM(L[i+1])){var dd=L[i].split('/');da=year+'-'+dd[1]+'-'+dd[0];mid=((L[i+2]||'')+' '+(L[i+3]||'')).trim();val=pnum(L[i+4]||'');i+=4;}
      else continue;
      if(val==null)continue;
      var tm=mid.match(tipos);var tipo=tm?tm[0]:'';var desc=tm?mid.slice(tipo.length).trim():mid;
      var nm=desc;var m1=desc.match(/recebido de (.+)$/i)||desc.match(/enviado para (.+)$/i);if(m1)nm=titlecase(m1[1].replace(/^\d+\s*/,''));
      var pm=/pix/i.test(tipo)?'Pix':(/pagamento/i.test(tipo)?'Débito':(/ted|transfer/i.test(tipo)?'Transferência':''));
      var row=mkrow({ac:'C6 - CC',pm:pm,da:da,pe:da,du:da,pd:da,av:da,nt:desc});var isIn=setBRL(row,val,da);row.nm=nm||desc;row.ct=classify(nm,desc,isIn);out.push(row);
    }return out;}
  function parseUnicredInvest(text){var cm=text.match(/Per[ií]odo de \d{2}\/\d{2}\/\d{4} a (\d{2})\/(\d{2})\/(\d{4})/);var close=cm?cm[3]+'-'+cm[2]+'-'+cm[1]:null;var out=[];
    var mr=text.match(/Per[ií]odo\s+([\d.]+,\d{2})\s+\1/);var rend=mr?pnum(mr[1]):null;
    var mi=text.match(/Retido\s+([\d.]+,\d{2})\s+\1/);var ir=mi?pnum(mi[1]):null;
    if(rend&&rend>0.004){var r1=mkrow({ac:'Unicred - Invest',pm:'Rendimento',da:close,pe:close,du:close,pd:close,av:close,nt:'Rendimento do período — Demonstrativo de Rentabilidade'});setBRL(r1,rend,close);r1.nm='Rendimento RDC Unicred';r1.ct='7.1.1 - Investment Income';out.push(r1);}
    if(ir&&ir>0.004){var r2=mkrow({ac:'Unicred - Invest',pm:'Imposto',da:close,pe:close,du:close,pd:close,av:close,nt:'IR retido — Demonstrativo de Rentabilidade'});setBRL(r2,-ir,close);r2.nm='IR Retido RDC Unicred';r2.ct='8.1.5 - Investment Income Tax (IRRF)';out.push(r2);}
    return out;}
  function detectPdf(text){var t=(text||'').toLowerCase();if(t.indexOf('demonstrativo de rentabilidade')>=0||(t.indexOf('recibo de dep')>=0&&t.indexOf('rdc')>=0))return 'unicredinvest';if(t.indexOf('saldo do dia')>=0&&(t.indexOf('entrada pix')>=0||t.indexOf('saída pix')>=0||t.indexOf('saida pix')>=0||t.indexOf('cheque especial')>=0))return 'c6cc';return null;}
  function runImportText(text,fname){var b=detectPdf(text);var list=[],acc=null;if(b==='unicredinvest'){list=parseUnicredInvest(text);acc='Unicred - Invest';}else if(b==='c6cc'){list=parseC6ccPDF(text);acc='C6 - CC';}else return {bank:'generic',account:null,rows:[],message:'PDF/imagem não reconhecido automaticamente.'};for(var j=0;j<list.length;j++)refine(list[j]);return {bank:b,account:acc,rows:list};}
  function runImport(rows,fname){
    rows=(rows||[]).filter(function(r){return r&&r.length&&r.some(function(x){return String(x==null?'':x).trim()!=='';});});
    if(rows.length<2)return {bank:'empty',account:null,rows:[],message:'Arquivo sem linhas de dados.'};
    var det=detectFormat(rows,fname);var list=[];
    if(det.bank==='stripe')list=parseStripe(rows,det.h);
    else if(det.bank==='boa')list=parseBoA(rows,det.h);
    else if(det.bank==='payoneer')list=parsePayoneer(rows,det.h);
    else if(det.bank==='asaas')list=parseAsaas(rows,det.h);
    else if(det.bank==='unicredcc')list=parseUnicredCC(rows,det.h);
    else if(det.bank==='c6card')list=parseCard(rows,det.h,'C6 - Cartão',1,fname,['data de compra'],['descri'],['valor (em r']);
    else if(det.bank==='unicredcard')list=parseCard(rows,det.h,'Unicred - Cartão',19,fname,['data'],['descri'],['valor']);
    else if(det.bank==='c6cc')return {bank:'c6cc',account:'C6 - CC',rows:[],message:'C6 Conta Corrente: sem movimentações.'};
    else return {bank:'generic',account:det.acc,rows:[],message:'Formato não reconhecido automaticamente.'};
    for(var j=0;j<list.length;j++)refine(list[j]);
    return {bank:det.bank,account:det.acc,rows:list};
  }
  return {runImport:runImport, runImportText:runImportText, detectFormat:detectFormat};
}
if(typeof module!=='undefined'){module.exports={buildImporter:buildImporter};}
