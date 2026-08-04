# VALIDATE-FEATURE

## Título

Validar Feature

## Papel do agente

QA Agent

## Objetivo

Verificar se uma Feature está pronta para ser recomendada como validada ou liberada.

## Contexto esperado

Feature com Tasks concluídas ou estado de pré-release.

## Documentos obrigatórios para leitura

- `FEATURE.md`
- `TASKS.md`
- regras relacionadas
- use cases e workflows
- `TESTS.md`
- relatórios de validação
- release candidata, quando aplicável

## Entradas necessárias

- Feature alvo
- evidências consolidadas

## Escopo permitido

- análise de conformidade funcional
- relatório de validação

## Restrições

- não aprovar release sozinho

## Procedimento de execução

1. revisar objetivo e critérios da Feature;
2. verificar cobertura pelas Tasks;
3. revisar testes, regras e documentação;
4. classificar prontidão.

## Validações obrigatórias

- Feature com critérios de aceite
- Tasks relacionadas com estados coerentes
- documentação sincronizada

## Critérios de conclusão

- parecer recomendando `validated`, `blocked` ou `needs-rework`

## Formato do relatório final

- escopo validado
- regras cobertas
- testes considerados
- riscos residuais
- recomendação

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Registrar Feature implementada com Tasks ou critérios incompletos.

## Tratamento de informação ausente

Bloquear recomendação de liberação se faltar evidência essencial.
