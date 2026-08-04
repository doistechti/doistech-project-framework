# HANDOFF-BETWEEN-AGENTS

## Título

Transferir trabalho entre agentes

## Papel do agente

Agente de origem e agente de destino autorizados

## Objetivo

Transferir contexto e responsabilidade operacional sem dependência do histórico completo da conversa.

## Contexto esperado

Troca de executor, revisão cruzada ou interrupção prolongada.

## Documentos obrigatórios para leitura

- Task
- Feature
- `PROJECT-STATE.md`
- relatório de execução anterior
- `AGENT-HANDOFF-CONTRACT.md`

## Entradas necessárias

- agente de origem
- agente de destino
- objetivo
- artefatos
- estado atual

## Escopo permitido

- preparação do handoff
- registro do contexto transferido

## Restrições

- não omitir riscos ou trabalho parcial

## Procedimento de execução

1. resumir contexto e trabalho feito;
2. listar artefatos relevantes;
3. registrar riscos, bloqueios e perguntas abertas;
4. indicar ação esperada do agente receptor.

## Validações obrigatórias

- objetivo claro
- artefatos referenciados
- bloqueios registrados

## Critérios de conclusão

- handoff completo e utilizável

## Formato do relatório final

- handoff emitido
- destino
- pendências
- condição de conclusão

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Registrar conflitos de contexto antes da transferência.

## Tratamento de informação ausente

Marcar explicitamente lacunas que o próximo agente deverá validar.
