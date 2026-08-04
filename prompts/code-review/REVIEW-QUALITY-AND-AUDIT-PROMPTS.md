---
id: PRM-REV-UNI-001
title: Revisão, qualidade e auditoria
version: 1.0
status: active
category: review
agent_profile: qa-agent
autonomy_level: 1-2
dpf_version: 1.0
created_at: 2026-08-04
updated_at: 2026-08-04
---

# Review, Quality and Audit Prompts

## PRM-REV-UNI-001 - Revisão universal

Comparar:

- Task
- Feature
- Business Rules
- ADRs
- implementação
- testes
- documentação
- DoD

Classificações mínimas:

- erro crítico
- erro funcional
- violação arquitetural
- risco de segurança
- alteração fora do escopo
- ausência de teste
- ausência documental
- melhoria opcional
- dívida técnica
- aprovado

## PRM-REV-ARC-001 - Revisar aderência arquitetural

Objetivo: verificar aderência a decisões e limites arquiteturais aprovados.

## PRM-REV-SEC-001 - Revisão de segurança

Objetivo: verificar autenticação, autorização, exposição de dados, segredos e riscos.

## PRM-REV-QA-001 - Emitir parecer de qualidade

Objetivo: classificar prontidão funcional e risco residual.

## PRM-AUD-QA-001 - Auditar conformidade DPF

Verificar:

- estrutura
- documentos obrigatórios
- hierarquia
- estados
- rastreabilidade
- Project State
- Business Rules
- ADRs
- Features
- Tasks
- evidências
- Releases
- documentação desatualizada
- links quebrados
- artefatos contraditórios
