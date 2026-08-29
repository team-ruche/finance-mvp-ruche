# Ruche — Central Financeira (MVP de validação)

- `index.html` — página hospedada (chama o webhook n8n `import-extrato` para estruturar extratos).
- `artifact.html` — versão standalone (parsing no navegador, SheetJS inline).
- `BD - Importador Universal.json` — workflow n8n que aplica todas as regras de data/PTAX/plano.
- `gen_v4.py` — gera `index.html`/`artifact.html` a partir de `payload.json`.
- `importer_core.js` + `gen_n8n.py` — lógica portada e gerador do workflow n8n.

Sem credenciais neste repositório.
