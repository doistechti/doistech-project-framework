# DEFINE-ARCHITECTURE

## Título

Definir arquitetura conceitual

## Papel do agente

Architect Agent

## Objetivo

Descrever arquitetura conceitual aderente aos requisitos, sem impor tecnologia.

## Contexto esperado

Projeto sem arquitetura formal ou com necessidade de atualização controlada.

## Documentos obrigatórios para leitura

- `PROJECT.md`
- `PROJECT-STATE.md`
- `PRODUCT-VISION.md`
- `BUSINESS-RULES.md`
- ADRs vigentes

## Entradas necessárias

- visão de produto
- requisitos e limites
- dependências conhecidas

## Escopo permitido

- documentação arquitetural
- proposta de limites e componentes conceituais

## Restrições

- não aprovar decisão arquitetural sozinho
- não escolher stack por conveniência

## Procedimento de execução

1. mapear contextos e dependências;
2. identificar limites e fluxos;
3. registrar arquitetura conceitual;
4. explicitar riscos e decisões pendentes.

## Validações obrigatórias

- coerência com regras e escopo
- ausência de mudança silenciosa de arquitetura

## Critérios de conclusão

- arquitetura conceitual navegável
- limites claros
- dependências registradas

## Formato do relatório final

- proposta
- riscos
- decisões necessárias

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Emitir proposta de ADR quando necessário.

## Tratamento de informação ausente

Declarar lacunas de arquitetura antes de estabilizar o documento.
