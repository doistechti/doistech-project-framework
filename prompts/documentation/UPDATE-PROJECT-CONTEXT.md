# UPDATE-PROJECT-CONTEXT

## Título

Atualizar contexto do projeto

## Papel do agente

Documentation Agent

## Objetivo

Atualizar `Project State`, índices e contexto operacional resumido sem duplicar integralmente as fontes primárias.

## Contexto esperado

Mudança relevante de estado, release, risco, decisão ou prioridade.

## Documentos obrigatórios para leitura

- `PROJECT-STATE.md`
- artefatos alterados
- riscos, dívida, release e decisões relevantes

## Entradas necessárias

- eventos recentes do projeto
- estado dos itens alterados

## Escopo permitido

- contexto resumido
- índices e leituras prioritárias

## Restrições

- não contradizer a fonte primária
- não promover item cancelado como ativo

## Procedimento de execução

1. consolidar alterações recentes;
2. atualizar resumo operacional;
3. atualizar leituras prioritárias;
4. apontar referências detalhadas.

## Validações obrigatórias

- coerência com fontes
- estado atual refletido

## Critérios de conclusão

- Project State atualizado e navegável

## Formato do relatório final

- mudanças refletidas
- fontes usadas
- pendências

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Registrar conflito entre fontes detalhadas.

## Tratamento de informação ausente

Manter o resumo conservador e explícito sobre lacunas.
