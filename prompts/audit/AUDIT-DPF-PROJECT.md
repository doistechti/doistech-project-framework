# AUDIT-DPF-PROJECT

## Título

Auditar projeto DPF

## Papel do agente

QA Agent, Documentation Agent ou auditor designado

## Objetivo

Verificar aderência estrutural, documental e operacional de um projeto ao DPF.

## Contexto esperado

Projeto em análise de conformidade ou revisão periódica.

## Documentos obrigatórios para leitura

- `PROJECT.md`
- `PROJECT-STATE.md`
- `SYSTEM-DESIGN.md`
- `DECISIONS.md`
- `RELEASES.md`
- `BUSINESS-RULES.md`
- `FEATURE.md` e `TASKS.md` amostradas

## Entradas necessárias

- escopo da auditoria
- período ou baseline
- critérios aplicáveis

## Escopo permitido

- análise
- classificação de conformidade
- relatório de auditoria

## Restrições

- não corrigir silenciosamente os achados

## Procedimento de execução

1. verificar estrutura e documentos obrigatórios;
2. revisar hierarquia, estados e rastreabilidade;
3. verificar evidências, releases e uso de prompts;
4. classificar achados.

## Validações obrigatórias

- referências válidas
- ausência de estados inválidos
- presença de `Project State`
- coerência entre documentação e operação

## Critérios de conclusão

- relatório de auditoria emitido

## Formato do relatório final

- conforme
- parcialmente conforme
- não conforme
- erro crítico
- recomendação
- oportunidade de melhoria

## Política de Git

Somente leitura, salvo autorização explícita para correção documental.

## Tratamento de inconsistências

Registrar cada conflito com severidade e fonte.

## Tratamento de informação ausente

Classificar ausência como lacuna, não como conformidade presumida.
