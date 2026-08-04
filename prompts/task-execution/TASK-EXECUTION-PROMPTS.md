---
id: PRM-IMP-UNI-001
title: Execução universal de task
version: 1.0
status: active
category: implementation
agent_profile: implementation-agents
autonomy_level: 3-4
dpf_version: 1.0
created_at: 2026-08-04
updated_at: 2026-08-04
---

# Task Execution Prompts

## PRM-CTX-ALL-001 - Carregamento de contexto

Objetivo: preparar contexto e emitir `Context Readiness Report` sem alterar artefatos.

## PRM-IMP-UNI-001 - Implementar Task universal

Procedimento obrigatório:

1. validar contexto;
2. confirmar DoR;
3. declarar plano;
4. executar somente o escopo;
5. preservar comportamentos existentes;
6. criar ou atualizar testes;
7. validar critérios;
8. registrar alterações;
9. atualizar documentação;
10. produzir relatório final.

Tratamento obrigatório:

- teste falhando: parar ou registrar bloqueio com evidência;
- regra ambígua: escalar;
- decisão arquitetural necessária: escalar;
- defeito adjacente: registrar fora do escopo;
- risco de segurança ou perda de dados: parar.

## PRM-IMP-BE-001 - Implementar Task de backend

Consultar no mínimo:

- Task
- Feature
- Business Rules
- APIs
- Database
- ADRs

## PRM-IMP-FE-001 - Implementar Task de frontend

Consultar no mínimo:

- Task
- Feature
- Use Cases
- Workflows
- estados
- critérios de acessibilidade e erro

## PRM-IMP-MOB-001 - Implementar Task mobile

Consultar no mínimo:

- Task
- Feature
- APIs
- conectividade
- sincronização
- permissões

## PRM-IMP-DB-001 - Executar alteração de dados autorizada

Consultar no mínimo:

- Task
- Feature
- Database
- migração
- rollback
- retenção

## PRM-OPS-DO-001 - Preparar alteração operacional controlada

Nunca autoriza produção automaticamente.

## PRM-FIX-UNI-001 - Corrigir defeito

Exigir:

- comportamento esperado
- observado
- reprodução
- impacto
- testes de regressão
- documentação afetada

## PRM-REF-UNI-001 - Refatorar

Exigir:

- comportamento preservado
- justificativa
- limites
- riscos
- rollback
- evidências

## PRM-TST-QA-001 - Gerar testes

Derivar cenários de:

- critérios de aceitação
- Business Rules
- Use Cases
- Workflows
- riscos
- defeitos anteriores

## PRM-DOC-DA-001 - Atualizar documentação

Atualizar apenas documentos comprovadamente afetados:

- Project State
- Implemented
- Planned
- Change Log
- Feature
- Task
- Release
- Decisions
- APIs
- Database
- Tests
