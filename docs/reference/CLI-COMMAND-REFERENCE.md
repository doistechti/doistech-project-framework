# CLI Command Reference

## `dpf version` ou `./dpf version`

Exibe a versão da CLI.

## `dpf init` ou `./dpf init`

Inicializa um projeto DPF.

Argumentos principais:

- `--path`
- `--name`
- `--context`
- `--owner`
- `--project-id`
- `--minimal`
- `--dry-run`

## `dpf validate` ou `./dpf validate`

Executa o validador oficial sobre o projeto informado.

Argumentos:

- `path`
- `--format human|json`

## `dpf status` ou `./dpf status`

Resume Features, Tasks, Releases e o resultado da validação atual.

Argumentos:

- `--path`
- `--format human|json`

## `dpf feature create` ou `./dpf feature create`

Cria uma Feature em uma Epic existente.

Argumentos:

- `--path`
- `--epic`
- `--title`

Comportamento:

- gera ID;
- cria `FEATURE.md`;
- cria `TASKS.md`;
- atualiza `FEATURES.md`;
- valida o projeto ao final.

## `dpf task create` ou `./dpf task create`

Cria uma Task em uma Feature existente.

Argumentos:

- `--path`
- `--feature`
- `--title`
- `--depends-on` (repetível)

Comportamento:

- gera ID;
- cria arquivo individual em `tasks/`;
- atualiza `TASKS.md`;
- valida o projeto ao final.

## `dpf decision create` ou `./dpf decision create`

Cria uma ADR.

Argumentos:

- `--path`
- `--title`
- `--related` (repetível)

Comportamento:

- gera ID;
- cria arquivo em `dpf/decisions/`;
- atualiza `DECISIONS.md`;
- valida o projeto ao final.

## `dpf release prepare` ou `./dpf release prepare`

Prepara uma Release sem marcá-la como concluída.

Argumentos:

- `--path`
- `--title`
- `--version`
- `--feature` (repetível)

Comportamento:

- gera ID;
- valida existência e estado das Features;
- cria documento em `dpf/releases/`;
- atualiza `RELEASES.md`;
- valida o projeto ao final.
