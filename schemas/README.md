# Schemas do DPF

## Padrão adotado

Os schemas da Fase 7 validam uma representação JSON dos contratos estruturados equivalentes ao front matter YAML e aos campos normativos verificáveis dos artefatos DPF.

Esse padrão foi adotado porque:

- preserva legibilidade humana na origem Markdown;
- permite validação automática futura;
- mantém compatibilidade com a decisão de front matter da Fase 3;
- evita tentar validar todo o corpo textual do Markdown por schema.

## Versão do JSON Schema

- Draft: `2020-12`

## Schemas disponíveis

- `project.schema.json`
- `feature.schema.json`
- `task.schema.json`
- `decision.schema.json`
- `release.schema.json`
- `validation-report.schema.json`
- `change-request.schema.json`
- `context.schema.json`

## Como validar

Validação mínima possível nesta fase:

1. parse sintático de todos os arquivos JSON;
2. verificação de `$ref` locais;
3. inspeção de exemplos válidos e inválidos.

Validação semântica completa contra JSON Schema exige um validador dedicado, que não faz parte desta fase.

## Limitações

JSON Schema isolado NÃO garante:

- unicidade global de IDs no repositório;
- existência real de arquivos referenciados;
- validade de links relativos;
- coerência entre Task e Feature em arquivos separados;
- coerência entre mapas e documentos primários;
- evidência realmente produzida;
- correção do versionamento histórico.

Essas regras exigem validador complementar na futura Fase 8.

## Exemplos válidos

Ver `schemas/examples/valid/`.

## Exemplos inválidos

Ver `schemas/examples/invalid/`.

Os nomes dos arquivos inválidos indicam a regra principal violada.

## Compatibilidade

Os schemas são compatíveis com a modelagem estrutural aprovada nas Fases 1 a 6, mas ainda não com templates físicos materializados em `templates/`, porque essa biblioteca ainda não foi implementada operacionalmente.

## Política de evolução

- mudanças compatíveis: incremento menor;
- mudanças incompatíveis: incremento maior;
- novos artefatos: adicionar novo schema, sem expandir silenciosamente os existentes.
