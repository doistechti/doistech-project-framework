# Validator Usage Guide

## Objetivo

O validador oficial do DPF verifica estrutura, metadados, identificadores, links, relações entre artefatos e consistência mínima de projetos DPF.

Nesta fase, o comando provisório aprovado é:

```bash
python -m dpf_validator validate .
```

## Requisitos

- Python 3.11 ou superior RECOMENDADO;
- acesso local ao repositório ou ao projeto DPF a ser validado;
- projeto contendo diretório `dpf/`.

## Instalação local

Nenhuma dependência externa precisa ser instalada nesta fase.

O validador utiliza apenas a biblioteca padrão do Python.

## Execução

Validar o diretório atual:

```bash
python -m dpf_validator validate .
```

Validar um projeto específico:

```bash
python -m dpf_validator validate examples/minimal-project
```

Emitir saída estruturada:

```bash
python -m dpf_validator validate examples/minimal-project --format json
```

## Opções

- `validate`: executa a validação do projeto informado;
- `path`: caminho do projeto DPF. O padrão é `.`;
- `--format human`: saída legível para terminal;
- `--format json`: saída estruturada para automações futuras.

## Códigos de saída

- `0`: validação concluída sem erros impeditivos;
- `1`: validação concluída com um ou mais erros;
- `2`: erro de uso do comando, caminho inexistente ou comando inválido.

## Severidades

- `erro`: bloqueia conformidade mínima;
- `aviso`: sinaliza problema relevante, mas não impeditivo;
- `informacao`: registro operacional da execução.

## Regras cobertas no MVP

- presença de `dpf/`, `PROJECT.md`, `PROJECT-STATE.md` e manifesto;
- IDs obrigatórios e formato por tipo de artefato;
- estados válidos por tipo;
- critérios de aceite de Feature;
- critérios de conclusão de Task;
- Release sem conteúdo;
- artefato cancelado sem justificativa;
- IDs duplicados;
- links relativos quebrados ou que escapam do projeto;
- inconsistência entre Task e `TASKS.md`;
- Feature concluída com Task aberta;
- Release concluída com Feature incompleta;
- dependências circulares detectáveis;
- proteção contra links simbólicos e arquivos grandes.

## Exemplos

Projeto mínimo válido:

```bash
python -m dpf_validator validate examples/minimal-project
```

Projeto completo válido:

```bash
python -m dpf_validator validate examples/complete-project
```

## Limitações atuais

- não executa correção automática;
- não acessa rede;
- não executa scripts do projeto validado;
- não implementa ainda uma engine completa de JSON Schema;
- não verifica unicidade global entre múltiplos repositórios;
- não resolve referências externas fora da raiz validada.

## Solução de problemas

`STRUCTURE_NO_DPF_ROOT`:
- o caminho informado não aponta para um projeto DPF.

`DOC_ID_MISSING` ou `DOC_STATUS_MISSING`:
- o documento normativo não contém metadados mínimos nem seção equivalente parseável.

`LINK_BROKEN`:
- o link relativo aponta para arquivo inexistente.

`SECURITY_SKIPPED_SYMLINK`:
- um link simbólico foi ignorado por segurança; substitua por arquivo real ou referência documental explícita.

`TASK_STATUS_MISMATCH`:
- o estado da Task diverge do mapa em `TASKS.md`.
