# VALIDATE-RELEASE

## Título

Validar Release

## Papel do agente

QA Agent, Security Agent, DevOps Agent ou Release Agent, conforme a dimensão validada

## Objetivo

Verificar a consistência final de uma release antes da decisão humana de liberação.

## Contexto esperado

Release preparada e candidata à liberação.

## Documentos obrigatórios para leitura

- arquivo da release
- `RELEASES.md`
- `CHANGELOG.md`
- relatórios de validação
- riscos
- rollback

## Entradas necessárias

- evidências consolidadas
- dependências
- estados finais

## Escopo permitido

- validação
- parecer de prontidão

## Restrições

- não autorizar produção

## Procedimento de execução

1. revisar integridade da release;
2. verificar itens, testes, segurança e documentação;
3. revisar rollback e riscos;
4. emitir parecer.

## Validações obrigatórias

- todos os itens apontam para fontes válidas
- mudanças incompatíveis registradas

## Critérios de conclusão

- parecer final emitido

## Formato do relatório final

- release validada ou não validada
- condições pendentes
- riscos críticos

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Bloquear recomendação positiva em caso de contradição crítica.

## Tratamento de informação ausente

Marcar como pendência explícita.
