# VALIDATE-TASK

## Título

Validar Task

## Papel do agente

QA Agent ou Documentation Agent, conforme o tipo de validação

## Objetivo

Verificar se a Task atende seus critérios, evidências e atualização documental mínima.

## Contexto esperado

Task revisada ou pronta para checagem final proporcional.

## Documentos obrigatórios para leitura

- Task
- `TASKS.md`
- `FEATURE.md`
- `TESTS.md`
- relatórios de execução e revisão

## Entradas necessárias

- critérios
- resultados de testes
- evidências

## Escopo permitido

- validação
- relatório de conformidade

## Restrições

- não alterar requisitos para aprovar a Task

## Procedimento de execução

1. verificar critérios da Task;
2. checar evidências e testes;
3. checar atualização documental;
4. recomendar estado.

## Validações obrigatórias

- critérios cobertos
- evidências presentes
- falhas não omitidas

## Critérios de conclusão

- parecer claro: validada, parcialmente validada ou não validada

## Formato do relatório final

- critérios atendidos
- critérios não atendidos
- evidências
- bloqueios
- recomendação

## Política de Git

Somente leitura, salvo autorização documental explícita.

## Tratamento de inconsistências

Escalar se a Task parecer concluída sem base verificável.

## Tratamento de informação ausente

Não presumir validação na falta de evidência.
