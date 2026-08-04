# RESUME-INTERRUPTED-WORK

## Título

Retomar trabalho interrompido

## Papel do agente

Agente sucessor autorizado ou mesmo agente em nova sessão

## Objetivo

Retomar trabalho parcial com inspeção rigorosa do estado real.

## Contexto esperado

Execução anterior interrompida, contexto parcial, artefatos possivelmente alterados.

## Documentos obrigatórios para leitura

- `PROJECT-STATE.md`
- Task e Feature
- relatórios anteriores
- handoff, se existir

## Entradas necessárias

- ponto de interrupção
- artefatos tocados
- evidências existentes

## Escopo permitido

- continuação controlada do trabalho aprovado

## Restrições

- não presumir correção do trabalho anterior
- não prosseguir sem verificação mínima

## Procedimento de execução

1. inspecionar estado atual;
2. ler histórico e contexto;
3. identificar trabalho parcial;
4. comparar documentação e artefatos;
5. verificar alterações não commitadas;
6. executar testes antes de continuar;
7. registrar ponto exato de retomada.

## Validações obrigatórias

- consistência entre estado e artefatos
- teste de referência executado quando aplicável

## Critérios de conclusão

- retomada segura registrada

## Formato do relatório final

- ponto retomado
- inconsistências
- ação executada
- evidências

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Escalar quando o trabalho parcial estiver em conflito com Task ou Feature.

## Tratamento de informação ausente

Limitar-se a análise e estabilização até obter contexto suficiente.
