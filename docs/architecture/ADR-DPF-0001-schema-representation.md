# ADR-DPF-0001

## Título

Representação de contratos documentais por JSON validando metadados estruturados equivalentes ao front matter

## Contexto

O DPF define front matter YAML como formato oficial mínimo de metadados para documentos. A Fase 7 exige schemas verificáveis, legíveis por humanos e compatíveis com automação futura.

## Problema

JSON Schema valida JSON. Os artefatos oficiais do DPF são majoritariamente Markdown com front matter YAML e corpo textual. Validar integralmente o Markdown excede o escopo desta fase.

## Decisão

Os schemas da Fase 7 validarão uma representação JSON dos contratos estruturados equivalentes ao front matter e aos campos normativos verificáveis do artefato.

Essa representação:

- preserva o modelo oficial de metadados do DPF;
- evita duplicar o corpo integral do Markdown nos schemas;
- permite futura extração automática do front matter para validação;
- mantém compatibilidade com templates e exemplos.

## Consequências

- JSON Schema cobre metadados, enums, formatos, listas e relações estruturais declarativas;
- regras que dependem do repositório completo, links, unicidade global e coerência semântica entre arquivos ficam fora do alcance do schema isolado;
- futura CLI ou validador poderá extrair front matter YAML e validar contra estes contratos JSON.
