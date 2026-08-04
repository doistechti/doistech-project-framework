---
id: PRM-REL-RA-001
title: Release e operações
version: 1.0
status: active
category: release
agent_profile: release-agent
autonomy_level: 2-3
dpf_version: 1.0
created_at: 2026-08-04
updated_at: 2026-08-04
---

# Release and Operations Prompts

## PRM-REL-RA-001 - Preparar Release

Verificar:

- itens incluídos
- estados
- DoD
- testes
- segurança
- documentação
- compatibilidade
- migrações
- configuração
- observabilidade
- riscos
- rollback
- aprovação
- Change Log
- Release Notes

Saída:

- `Release Readiness Report`
- recomendação `GO`, `GO WITH CONDITIONS` ou `NO-GO`

## PRM-REL-RA-002 - Gerar Release Notes

Objetivo: resumir mudanças aprovadas, riscos, incompatibilidades e evidências.

## PRM-OPS-DO-001 - Diagnosticar problema operacional

Separar:

- sintomas
- evidências
- hipóteses
- testes realizados
- causa provável
- causa confirmada
- impacto
- solução provisória
- solução definitiva
- riscos

## PRM-LEG-LA-001 - Analisar projeto legado

Identificar:

- visão inferida
- arquitetura atual
- componentes
- funcionalidades existentes
- regras aparentes
- regras confirmadas
- riscos
- dívida técnica
- ausência de testes
- divergências
- próximos passos

Toda inferência deve ser marcada como hipótese.
