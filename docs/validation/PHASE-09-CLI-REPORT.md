# PHASE-09-CLI-REPORT

## Escopo

Implementação do MVP da CLI oficial do DPF com foco em:

- inicialização de projeto;
- validação;
- leitura de status;
- criação de Feature;
- criação de Task;
- criação de decisão;
- preparação de Release.

## Comandos implementados

- `dpf --help`
- `dpf version`
- `dpf init`
- `dpf validate`
- `dpf status`
- `dpf feature create`
- `dpf task create`
- `dpf decision create`
- `dpf release prepare`

## Arquitetura

- pacote: `dpf_cli/`
- parser: `argparse`
- validação: reutilização direta de `dpf_validator`
- manifesto: `dpf/dpf-project.yaml`
- templates do MVP: base canônica oficial em `templates/`, consumida pela CLI nos principais artefatos
- instalação local: launcher `./dpf` no repositório e `pyproject.toml` para empacotamento futuro

ADR relacionada:
- [ADR-DPF-0003-cli-architecture.md](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/architecture/ADR-DPF-0003-cli-architecture.md)

## Integração com o validador

Toda operação de escrita do MVP termina com validação do projeto resultante.

A CLI não duplica enums, severidades ou relatório humano/JSON do validador além do necessário para chamar o núcleo existente.

## Testes executados

Em 4 de agosto de 2026, executei:

```bash
python3 -m compileall dpf_cli dpf_validator tests
python3 -m unittest -v tests/test_cli.py
python3 -m unittest -v tests/test_validator.py tests/test_cli.py
python3 -m dpf_cli --help
python3 -m dpf_cli version
./dpf version
python3 -m dpf_cli init --path /tmp/... --dry-run
```

## Cobertura do MVP

- ajuda;
- versão;
- inicialização mínima;
- conflito com arquivos existentes;
- dry-run;
- criação de Feature;
- geração sequencial de IDs;
- criação de Task;
- Feature inexistente;
- criação de ADR;
- preparação de Release;
- status JSON;
- integração com validador;
- códigos de saída;
- caminho inseguro por symlink.

## Resultados

- suíte `tests/test_cli.py`: `OK`
- suíte combinada `tests/test_validator.py tests/test_cli.py`: `OK`
- `dpf init` cria projeto validável;
- `dpf validate` reutiliza a Fase 8 com saída humana e JSON;
- `dpf status` deriva o estado diretamente dos documentos.

## Compatibilidade

- Python 3.11 ou superior;
- compatível com a estrutura oficial definida na Fase 3;
- dependente dos contratos e convenções já consolidados nas Fases 1 a 8.

## Limitações

- não cria Capability nem Epic;
- não há modo interativo completo;
- a CLI ainda mantém alguns artefatos auxiliares simples fora do catálogo oficial de templates;
- a biblioteca operacional mínima de templates em `templates/` já foi materializada;
- não há ainda comando para fechar release, arquivar artefatos ou refatorar estado documental.

## Observação sobre instalação editável

No ambiente testado em 4 de agosto de 2026, a instalação via `pip install -e . --no-build-isolation` em venv limpo com Python 3.14 não foi concluída porque `setuptools` não estava disponível no ambiente de build local.

O launcher `./dpf` foi validado como caminho local funcional sem rede.

## Riscos

- futura divergência se templates auxiliares locais da CLI evoluírem sem sincronização com a biblioteca oficial;
- necessidade de ampliar a cobertura da biblioteca oficial para artefatos auxiliares ainda gerados localmente;
- ausência atual de governança preenchida em `docs/governance/` limita futuras validações e políticas de CLI.

## Pendências para a Fase 10

- ampliar a externalização de artefatos auxiliares para a biblioteca operacional oficial;
- expandir comandos de Capability e Epic;
- adicionar operações seguras de atualização de estado;
- preparar empacotamento e publicação controlada;
- definir integração opcional com automações e validadores mais estritos.
