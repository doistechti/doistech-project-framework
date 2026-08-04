# ADR-DPF-0003

## Título

Arquitetura do MVP da CLI oficial do DPF

## Contexto

A Fase 9 exige a primeira interface oficial de linha de comando do DPF.

A Fase 8 já disponibiliza um núcleo de validação local em Python. A CLI precisa:

- reutilizar esse núcleo;
- gerar artefatos documentais sem esconder as regras do framework;
- manter portabilidade;
- evitar dependências externas desnecessárias.

## Problema

A CLI precisa oferecer comandos úteis de adoção e operação documental sem duplicar o comportamento do validador nem criar uma segunda fonte de verdade para o estado do projeto.

## Decisão

O MVP da CLI foi implementado como pacote Python separado:

```text
dpf_cli/
```

com entrada oficial:

```bash
dpf
```

e entrada provisória equivalente:

```bash
python -m dpf_cli
```

A arquitetura adota:

- `argparse` para interface de comandos;
- reutilização programática de `dpf_validator`;
- biblioteca oficial de templates em `templates/` como base canônica para os principais artefatos do MVP;
- manifesto `dpf/dpf-project.yaml` como fonte de contexto estrutural;
- escrita explícita de arquivos e atualização controlada de índices.

## Justificativa

Essa divisão:

- evita duplicar regras de validação;
- mantém separação entre interface, geração documental e validação;
- permite futura troca do frontend da CLI sem reescrever o núcleo;
- prepara a evolução para empacotamento e publicação futura.

## Consequências

- a CLI depende das regras já aprovadas na Fase 8;
- o MVP cobre inicialização, criação de artefatos e leitura de status;
- a CLI depende da biblioteca oficial materializada em `templates/` para os principais artefatos do MVP;
- ainda existem artefatos auxiliares simples mantidos localmente na CLI, fora do catálogo mínimo oficial de templates.
