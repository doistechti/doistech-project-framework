---
id: ADR-COM-0002
title: Release evidence before publication state change
type: decision
status: approved
version: 1.0
owner: architecture-owner
author: framework-example
approver: product-owner
created_at: 2026-08-04
updated_at: 2026-08-04
related:
  - REL-COM-0001
  - VAL-COM-0001
---

# ADR-COM-0002

## Contexto

O estado `released` precisa ser auditável no projeto de referência.

## Decisão

Mudança de estado para `released` depende de evidência documental mínima em validação e release.

## Consequências

- sincronização entre `TESTS.md`, relatórios e `RELEASES.md`.
