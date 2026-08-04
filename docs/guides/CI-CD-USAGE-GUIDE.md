# CI/CD Usage Guide

## Objetivo

Descrever como usar as automações do DPF localmente e no GitHub Actions.

## Runner local

Comando base:

```bash
python3 scripts/automation/run_quality_gate.py manual --project-path .
```

Perfis disponíveis:

- `pr`
- `main`
- `release`
- `manual`

## Exemplos

Pull request local:

```bash
python3 scripts/automation/run_quality_gate.py pr --project-path . --output-dir .dpf-artifacts
```

Branch principal:

```bash
python3 scripts/automation/run_quality_gate.py main --project-path . --output-dir .dpf-artifacts
```

Preparação de release:

```bash
python3 scripts/automation/run_quality_gate.py release --project-path . --release-doc examples/complete-project/dpf/releases/REL-COM-0001-community-event-publishing.md --output-dir .dpf-artifacts
```

## Artefatos

O runner gera:

- `quality-gate-report.json`
- `quality-gate-summary.md`

## Workflows

- `dpf-pr.yml`
- `dpf-main.yml`
- `dpf-release-preparation.yml`
- `dpf-manual-validation.yml`

## Falhas comuns

- documento de release ausente;
- launcher `dpf` sem permissão de execução;
- projeto inválido para o validador;
- schema JSON malformado;
- testes quebrados.

## Limitações

- não há execução local nativa de GitHub Actions nesta fase;
- não há publicação automática;
- não há integração com ambientes externos ou segredos.
