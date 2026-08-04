# Phases 05-10 Execution Order

## Objetivo

Registrar no repositório a ordem de execução consolidada do pacote de prompts das Fases 5 a 10 do DPF.

## Ordem de execução

1. `FASE-05-PROJETO-DE-REFERENCIA.md`
2. `FASE-06-BIBLIOTECA-DE-PROMPTS-OPERACIONAIS.md`
3. `FASE-07-CONTRATOS-E-SCHEMAS.md`
4. `FASE-08-VALIDADOR-DO-DPF.md`
5. `FASE-09-CLI-OFICIAL.md`
6. `FASE-10-INTEGRACAO-E-AUTOMACAO.md`

## Recomendação operacional

As fases DEVEM ser executadas sequencialmente.

Antes da fase seguinte, DEVE ser feito:

- revisão dos arquivos criados;
- execução das validações;
- correção das inconsistências;
- commit manual;
- aprovação humana da fase anterior.

## Commits sugeridos

```text
docs: add DPF reference projects
docs: add DPF operational prompt library
feat: add DPF artifact schemas
feat: implement DPF validator
feat: implement DPF CLI
ci: add DPF validation workflows
```

Os prompts mantêm a proibição de commit e push automáticos.
