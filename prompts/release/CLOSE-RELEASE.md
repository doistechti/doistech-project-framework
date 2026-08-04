# CLOSE-RELEASE

## Título

Encerrar Release

## Papel do agente

Documentation Agent ou Release Agent

## Objetivo

Encerrar documentalmente uma release após decisão humana de liberação ou cancelamento.

## Contexto esperado

Release já decidida.

## Documentos obrigatórios para leitura

- release alvo
- `RELEASES.md`
- `CHANGELOG.md`
- `PROJECT-STATE.md`
- `IMPLEMENTED.md`

## Entradas necessárias

- resultado da release
- data efetiva
- evidências finais

## Escopo permitido

- atualização documental pós-decisão

## Restrições

- não simular liberação não aprovada

## Procedimento de execução

1. confirmar decisão humana;
2. atualizar estado da release;
3. sincronizar índices e contexto;
4. registrar encerramento e efeitos.

## Validações obrigatórias

- estado final coerente
- contexto atualizado

## Critérios de conclusão

- release encerrada documentalmente

## Formato do relatório final

- estado final
- documentos atualizados
- itens remanescentes

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Escalar se a decisão humana não estiver registrada.

## Tratamento de informação ausente

Não concluir encerramento sem evidência de decisão final.
