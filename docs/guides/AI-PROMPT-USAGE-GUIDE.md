# AI-PROMPT-USAGE-GUIDE

## Objetivo

Orientar o uso prático da biblioteca oficial de prompts operacionais do DPF.

## Princípios de uso

- começar pelo contexto antes da ação;
- escolher o prompt pela atividade, não pela conveniência;
- combinar o prompt específico com `prompts/PROMPT-BASE.md`;
- não usar prompt de execução quando a atividade é apenas análise;
- não usar prompt de Git sem autorização explícita.

## Escolha do prompt

- projeto novo: `INIT-DPF-PROJECT.md`
- projeto existente: `ASSESS-EXISTING-PROJECT.md`
- visão: `DEFINE-PRODUCT-VISION.md`
- arquitetura: `DEFINE-ARCHITECTURE.md`
- decisão arquitetural: `REGISTER-ARCHITECTURAL-DECISION.md`
- planejamento: `PLAN-FEATURE.md`, `DECOMPOSE-FEATURE-INTO-TASKS.md`
- execução: `EXECUTE-TASK.md`, `CONTINUE-TASK.md`
- revisão: `REVIEW-TASK.md`
- validação: `VALIDATE-TASK.md`, `VALIDATE-FEATURE.md`
- defeito: `FIX-BUG.md`
- release: `PREPARE-RELEASE.md`, `VALIDATE-RELEASE.md`, `CLOSE-RELEASE.md`
- retomada: `RESUME-INTERRUPTED-WORK.md`
- handoff: `HANDOFF-BETWEEN-AGENTS.md`
- auditoria: `AUDIT-DPF-PROJECT.md`

## Sequência recomendada para alteração

1. carregar contexto;
2. avaliar se a Task está pronta;
3. executar no escopo;
4. revisar;
5. validar;
6. atualizar documentação;
7. preparar release, se aplicável.

## Cuidados

- não interpretar silêncio documental como autorização;
- não promover hipótese a fato;
- não esconder falha de teste;
- não corrigir problema adjacente sem registro;
- não alterar critérios de aceite sem governança.

## Saídas esperadas

Todo uso sério da biblioteca deve resultar em:

- relatório final;
- lista de artefatos alterados;
- evidências;
- riscos;
- pendências;
- recomendação de próximo estado.
