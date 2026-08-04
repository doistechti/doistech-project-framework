# PREPARE-RELEASE

## Título

Preparar Release

## Papel do agente

Release Agent ou Documentation Agent com apoio técnico

## Objetivo

Consolidar os artefatos necessários para uma release e emitir prontidão preliminar.

## Contexto esperado

Conjunto de itens candidatos a release.

## Documentos obrigatórios para leitura

- `RELEASES.md`
- release candidata
- `CHANGELOG.md`
- `PROJECT-STATE.md`
- validações, riscos e decisões relevantes

## Entradas necessárias

- itens incluídos
- evidências
- testes
- dependências

## Escopo permitido

- consolidação documental
- relatório de readiness

## Restrições

- não liberar produção
- não esconder pendências

## Procedimento de execução

1. verificar itens candidatos;
2. revisar estados e DoD;
3. revisar testes, riscos, rollback e documentação;
4. consolidar `Release Readiness Report`.

## Validações obrigatórias

- itens rastreáveis
- evidências mínimas presentes
- changelog e release notes alinhados

## Critérios de conclusão

- release preparada e classificada

## Formato do relatório final

- GO
- GO WITH CONDITIONS
- NO-GO
- riscos
- pendências

## Política de Git

Sem commit ou push automático.

## Tratamento de inconsistências

Escalar se release incluir itens sem validação mínima.

## Tratamento de informação ausente

Sem evidência suficiente, classificar como NO-GO ou GO WITH CONDITIONS.
