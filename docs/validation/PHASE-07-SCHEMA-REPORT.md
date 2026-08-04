# PHASE-07-SCHEMA-REPORT

## Regras cobertas

- contrato e versão do artefato
- tipo do artefato
- identificador e prefixo por artefato
- título
- status com enums oficiais por tipo
- owner, author, approver
- datas de criação e atualização
- relação pai de Feature e Task
- critérios de aceite da Feature
- riscos, evidências, documentos relacionados
- consequência, problema e decisão em ADR
- itens incluídos, testes e evidências em Release
- contexto resumido e referências prioritárias em contrato de contexto
- resultado de validação em relatório de validação

## Regras não cobertas por schema isolado

- unicidade global de IDs no repositório
- existência de links e arquivos referenciados
- coerência entre mapa de Tasks e documento da Feature
- coerência entre Project State e fontes detalhadas
- evidência efetivamente produzida
- atualização correta de versão histórica
- pertencimento real de uma Task ao arquivo correto da Feature

## Artefatos com schema

- `project.schema.json`
- `feature.schema.json`
- `task.schema.json`
- `decision.schema.json`
- `release.schema.json`
- `validation-report.schema.json`
- `change-request.schema.json`
- `context.schema.json`

## Conflitos encontrados

- `templates/` ainda não possuía materialização física suficiente para comparação estrutural direta por arquivo concreto no momento da fase
- `docs/governance/` permanece vazio

## Alterações em templates

Nenhuma alteração foi aplicada em `templates/`, porque a biblioteca operacional da Fase 2 ainda não estava materializada no momento da fase.

## Resultados técnicos

- arquivos JSON criados com sintaxe válida
- referências locais de `$ref` estruturadas
- exemplos válidos e inválidos criados para cada schema

## Limitações

- não há validador JSON Schema dedicado já instalado no ambiente
- a fase realizou validação sintática e estrutural local, não validação semântica completa de instâncias contra schema com ferramenta dedicada

## Riscos de compatibilidade

- divergências futuras se a Fase 2 operacional materializar templates com campos adicionais ou nomes diferentes

## Atualização posterior

Em 4 de agosto de 2026, a biblioteca operacional mínima da Fase 2 foi materializada em `templates/`.
- necessidade de alinhamento adicional entre exemplos em Markdown e representação JSON dos contratos

## Recomendação para a Fase 8

Implementar um validador de repositório que:

1. extraia front matter de Markdown;
2. converta para os contratos JSON esperados;
3. valide contra estes schemas;
4. cheque unicidade, links, coerência cruzada e rastreabilidade.
