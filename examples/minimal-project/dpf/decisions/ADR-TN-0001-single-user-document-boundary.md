---
id: ADR-TN-0001
title: Single-user document boundary
type: architecture-decision
status: approved
version: 1.0
owner: architecture-owner
author: framework-example
approver: architecture-owner
created_at: 2026-08-04
updated_at: 2026-08-04
related:
  - FEAT-TN-0001
---

# ADR-TN-0001

## Contexto

O exemplo mínimo precisa demonstrar fronteira funcional sem depender de componentes técnicos específicos.

## Problema

Sem uma decisão explícita, o exemplo poderia confundir regra funcional com detalhe técnico.

## Decisão

O projeto será modelado como fluxo de usuário único com armazenamento conceitual e sem componentes externos.

## Consequências

- menor ambiguidade para agentes;
- menor superfície documental;
- sem extrapolação para integração ou multiusuário.
