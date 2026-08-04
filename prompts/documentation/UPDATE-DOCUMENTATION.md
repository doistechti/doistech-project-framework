# UPDATE-DOCUMENTATION

## Título

Atualizar documentação

## Papel do agente

Documentation Agent

## Objetivo

Sincronizar documentação impactada por mudança aprovada e comprovada.

## Contexto esperado

Task, Feature, Release ou decisão já executada ou validada.

## Documentos obrigatórios para leitura

- `PROJECT-STATE.md`
- Task e Feature relacionadas
- `IMPLEMENTED.md`
- `PLANNED.md`
- `CHANGELOG.md`
- `RELEASES.md`, quando aplicável

## Entradas necessárias

- artefatos alterados
- relatório de execução
- evidências

## Escopo permitido

- apenas documentos comprovadamente afetados

## Restrições

- não alterar regra para justificar implementação
- não reescrever histórico sem sinalização

## Procedimento de execução

1. identificar documentos impactados;
2. comparar fato executado com estado documental;
3. atualizar somente o necessário;
4. preservar rastreabilidade e histórico.

## Validações obrigatórias

- coerência com fonte primária
- links e relações válidas

## Critérios de conclusão

- documentação sincronizada
- mudanças relatadas

## Formato do relatório final

- documentos atualizados
- motivo
- relações afetadas
- pendências

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Escalar divergência entre implementação e intenção aprovada.

## Tratamento de informação ausente

Não documentar comportamento como oficial se não houver aprovação ou evidência suficiente.
