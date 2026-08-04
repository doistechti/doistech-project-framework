# Automation Reference

## Workflows

### `dpf-pr`

Evento:

- `pull_request`

Objetivo:

- executar quality gate de PR;
- coletar arquivos alterados;
- publicar artifacts com relatório.

### `dpf-main`

Evento:

- `push` em `main` ou `master`

Objetivo:

- executar validação completa;
- reforçar consistência dos exemplos e do status do repositório.

### `dpf-release-preparation`

Evento:

- `workflow_dispatch`

Objetivo:

- validar preparação de release sem publicar.

### `dpf-manual-validation`

Evento:

- `workflow_dispatch`

Objetivo:

- permitir execução manual do quality gate.

## Permissões

Todos os workflows do MVP usam apenas:

```yaml
permissions:
  contents: read
```

## Runner local

Arquivo:

```text
scripts/automation/run_quality_gate.py
```

Responsabilidades:

- chamar testes;
- chamar `./dpf validate`;
- validar exemplos;
- validar sanity dos schemas;
- produzir relatório JSON e summary Markdown.
