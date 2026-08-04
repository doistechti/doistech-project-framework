# REVIEW-TASK

## Título

Revisar Task executada

## Papel do agente

QA Agent, Architect Agent, Security Agent ou revisor técnico designado

## Objetivo

Comparar resultado da Task com Task, Feature, regras, arquitetura, testes e documentação.

## Contexto esperado

Task executada ou parcialmente executada aguardando revisão.

## Documentos obrigatórios para leitura

- `TASKS.md`
- Task
- `FEATURE.md`
- `BUSINESS-RULES.md`, quando aplicável
- ADRs relacionadas
- `TESTS.md`
- documentação atualizada

## Entradas necessárias

- artefatos alterados
- evidências
- resultados de testes

## Escopo permitido

- revisão
- relatório
- proposta de correções

## Restrições

- não alterar implementação silenciosamente quando a função for apenas revisar

## Procedimento de execução

1. revisar aderência ao escopo;
2. comparar com critérios e regras;
3. verificar testes e documentação;
4. classificar achados.

## Validações obrigatórias

- escopo respeitado
- testes coerentes
- evidências presentes

## Critérios de conclusão

- revisão concluída com classificação dos achados

## Formato do relatório final

- erro crítico
- erro funcional
- violação arquitetural
- risco de segurança
- ausência de teste
- ausência documental
- melhoria opcional
- aprovado

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Registrar contradições entre documentação e alteração executada.

## Tratamento de informação ausente

Se faltarem evidências essenciais, impedir recomendação de conclusão.
