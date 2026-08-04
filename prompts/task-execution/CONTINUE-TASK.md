# CONTINUE-TASK

## Título

Continuar Task em andamento

## Papel do agente

Agente executor da Task ou agente sucessor autorizado

## Objetivo

Retomar a execução de uma Task parcialmente iniciada sem assumir que o trabalho anterior está correto.

## Contexto esperado

Task em andamento, retomada após interrupção ou troca de agente.

## Documentos obrigatórios para leitura

- `PROJECT-STATE.md`
- `TASKS.md`
- arquivo da Task
- histórico documental associado
- relatório de execução anterior, se existir

## Entradas necessárias

- ID da Task
- ponto de interrupção
- alterações locais existentes

## Escopo permitido

- continuação da mesma Task

## Restrições

- não assumir correção do trabalho anterior
- não ampliar escopo

## Procedimento de execução

1. inspecionar estado atual;
2. verificar alterações não commitadas;
3. comparar documentação e artefatos alterados;
4. executar testes pertinentes antes de prosseguir;
5. registrar ponto exato de retomada;
6. continuar somente no escopo original.

## Validações obrigatórias

- compatibilidade entre estado documental e estado real
- teste mínimo antes de seguir

## Critérios de conclusão

- retomada segura registrada
- nova etapa executada ou bloqueio explicado

## Formato do relatório final

- ponto de retomada
- inconsistências encontradas
- ação realizada
- evidências

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Bloquear se o estado parcial contradizer a Task ou a Feature.

## Tratamento de informação ausente

Registrar falta de histórico e reduzir autonomia para análise até estabilizar contexto.
