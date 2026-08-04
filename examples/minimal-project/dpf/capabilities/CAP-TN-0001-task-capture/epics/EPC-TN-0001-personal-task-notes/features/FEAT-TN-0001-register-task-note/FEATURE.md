---
id: FEAT-TN-0001
title: Register task note
type: feature
status: released
version: 1.0
owner: product-owner
author: framework-example
approver: product-owner
created_at: 2026-08-04
updated_at: 2026-08-04
parent: EPC-TN-0001
related:
  - TASK-TN-0001
  - TASK-TN-0002
  - TASK-TN-0003
  - ADR-TN-0001
  - REL-TN-0001
---

# FEATURE.md

## Objetivo

Permitir que a pessoa usuária registre uma anotação curta de tarefa pessoal.

## Escopo

- capturar texto curto;
- persistir conceitualmente o registro;
- exibir o item criado em lista simples.

## Fora de escopo

- lembretes;
- prioridades automáticas;
- compartilhamento.

## Critérios de aceite

- AC-TN-0001: dado um texto válido, quando a pessoa confirmar o registro, então a anotação deve ser criada.
- AC-TN-0002: dado um registro criado, quando a lista for consultada, então o item deve aparecer.
- AC-TN-0003: a documentação relacionada deve refletir o estado da Feature.

## Rastreabilidade

- Visão: [PRODUCT-VISION.md](../../../../../../product/PRODUCT-VISION.md)
- Arquitetura: [SYSTEM-DESIGN.md](../../../../../../architecture/SYSTEM-DESIGN.md)
- Decisão: [ADR-TN-0001](../../../../../../decisions/ADR-TN-0001-single-user-document-boundary.md)
- Release: [REL-TN-0001](../../../../../../releases/REL-TN-0001-initial-task-note-capture.md)
