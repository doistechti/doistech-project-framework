# FIX-BUG

## Título

Corrigir defeito

## Papel do agente

Agente executor apropriado ao defeito

## Objetivo

Corrigir a causa do defeito dentro do escopo autorizado, sem mascarar sintomas.

## Contexto esperado

Bug registrado, reproduzível ou suficientemente descrito.

## Documentos obrigatórios para leitura

- Task ou Change Request correspondente
- Feature relacionada
- regras relacionadas
- testes e evidências do defeito

## Entradas necessárias

- descrição
- comportamento esperado
- comportamento observado
- ambiente
- forma de reprodução
- impacto

## Escopo permitido

- correção da causa no escopo autorizado

## Restrições

- não corrigir por efeito colateral oculto
- não alterar requisito para legitimar bug

## Procedimento de execução

1. reproduzir ou qualificar o defeito;
2. identificar causa provável;
3. corrigir a causa no escopo;
4. executar regressão adequada;
5. atualizar documentação afetada.

## Validações obrigatórias

- regressão executada
- impacto informado
- documentação coerente

## Critérios de conclusão

- defeito tratado com evidência
- regressão documentada

## Formato do relatório final

- causa
- correção
- testes
- impacto residual

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Se o bug revelar mudança arquitetural ou regra ausente, escalar.

## Tratamento de informação ausente

Registrar limitação de reprodução e reduzir confiança da conclusão.
