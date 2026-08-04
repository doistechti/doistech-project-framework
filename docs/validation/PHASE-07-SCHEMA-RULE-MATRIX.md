# PHASE-07-SCHEMA-RULE-MATRIX

## Objetivo

Mapear regras documentais aprovadas para validações estruturais representáveis por schema.

| Regra documental | Fonte | Representação no schema | Cobertura |
| --- | --- | --- | --- |
| ID obrigatório | Fase 3, metadados | `id` requerido | coberta |
| Título obrigatório | Fase 3, metadados | `title` requerido | coberta |
| Tipo do artefato | Fase 3, metadados | `artifact_type` com `const` por schema | coberta |
| Status do artefato | Fase 3, estados | `status` com enum oficial por tipo | coberta |
| Versão obrigatória | Fase 3, metadados | `version` requerido | coberta |
| Owner/author/approver | Fase 3, metadados | campos requeridos | coberta |
| Datas mínimas | Fase 3, metadados | `created_at`, `updated_at` com formato de data | coberta |
| Parent quando aplicável | Fase 3, metadados | `parent_*_id` requerido em feature/task | coberta |
| Relações por IDs | Fase 1, rastreabilidade; Fase 3 | arrays de IDs | coberta parcialmente |
| Critérios de aceite da Feature | Fase 3, Feature | `acceptance_criteria` | coberta |
| Task vinculada à Feature | Fase 1 e Fase 3 | `parent_feature_id` | coberta estruturalmente |
| ADR com contexto, problema, decisão, riscos | Fase 1 | campos requeridos no schema de decisão | coberta |
| Release com itens, riscos, evidências | Fase 3 | campos requeridos e opcionais | coberta |
| Resultado de validação | Fase 5 exemplos, Fase 6 | `validation_result` | coberta estruturalmente |
| Motivo de cancelamento | Fase 3 | `cancellation_reason` condicional | coberta |
| Referências documentais | Fase 3, rastreabilidade | arrays `document_refs` / `evidence_refs` | coberta estruturalmente |
| Unicidade global de IDs | Fase 3 | exige validador de repositório | não coberta por schema isolado |
| Existência de links/arquivos | Fase 3 | exige validador complementar | não coberta por schema isolado |
| Coerência entre mapa e documento | Fase 5, Fase 6 | exige validação cruzada | não coberta por schema isolado |
