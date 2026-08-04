# REGISTER-ARCHITECTURAL-DECISION

## Título

Registrar decisão arquitetural

## Papel do agente

Architect Agent

## Objetivo

Preparar uma ADR completa, rastreável e pronta para revisão humana.

## Contexto esperado

Mudança estrutural, conflito técnico relevante ou necessidade de formalização de decisão.

## Documentos obrigatórios para leitura

- `SYSTEM-DESIGN.md`
- `DECISIONS.md`
- Feature e Task relacionadas
- riscos e dependências

## Entradas necessárias

- problema
- alternativas
- impactos
- artefatos afetados

## Escopo permitido

- criação ou atualização de ADR
- atualização do índice de decisões

## Restrições

- não aprovar a decisão
- não implementar a mudança no mesmo ato sem contrato próprio

## Procedimento de execução

1. registrar contexto e problema;
2. listar alternativas;
3. registrar decisão proposta;
4. explicitar consequências e riscos;
5. vincular artefatos impactados.

## Validações obrigatórias

- ADR com ID e estado
- relações com Feature e Task
- ausência de contradição com decisões vigentes

## Critérios de conclusão

- ADR pronta para revisão humana

## Formato do relatório final

- ADR criada ou atualizada
- impactos
- aprovações necessárias

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Registrar conflito entre ADRs e interromper a execução estrutural.

## Tratamento de informação ausente

Não preencher alternativas ou impactos com suposições silenciosas.
