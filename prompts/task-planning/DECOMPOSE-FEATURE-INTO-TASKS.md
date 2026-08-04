# DECOMPOSE-FEATURE-INTO-TASKS

## Título

Decompor Feature em Tasks

## Papel do agente

Business Analyst Agent

## Objetivo

Gerar Tasks pequenas, delimitadas e verificáveis a partir de uma Feature aprovada.

## Contexto esperado

Feature pronta para planejamento operacional.

## Documentos obrigatórios para leitura

- `FEATURE.md`
- `BUSINESS-RULES.md`
- `USE-CASES.md`
- `WORKFLOWS.md`
- `SYSTEM-DESIGN.md`, quando aplicável

## Entradas necessárias

- Feature
- critérios de aceite
- dependências

## Escopo permitido

- `TASKS.md`
- arquivos individuais de Task, quando necessário

## Restrições

- não transformar uma Epic inteira em uma única Task
- não criar Tasks sem objetivo verificável

## Procedimento de execução

1. separar trabalho por objetivo e evidência;
2. definir entradas, saídas e limites;
3. identificar tarefas com risco ou necessidade de arquivo individual;
4. registrar DoR e DoD proporcionais.

## Validações obrigatórias

- toda Task aponta para a Feature
- nenhuma Task contém escopo de outra Feature

## Critérios de conclusão

- conjunto coerente de Tasks executáveis

## Formato do relatório final

- Tasks criadas
- justificativas
- riscos

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Escalar quando a Feature não estiver suficientemente definida.

## Tratamento de informação ausente

Bloquear decomposição se faltar contexto crítico.
