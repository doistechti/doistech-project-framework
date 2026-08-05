# DoisTech Project Framework — DPF

O DoisTech Project Framework é uma metodologia de engenharia de software
criada para projetos desenvolvidos de forma colaborativa por pessoas e
agentes de Inteligência Artificial.

O DPF busca estabelecer uma forma padronizada, rastreável e segura de
planejar, especificar, implementar, validar e evoluir projetos de software
assistidos por agentes de IA.

## Princípios

O DPF adota os seguintes princípios fundamentais:

- Specification First
- Documentation as Source of Truth
- Context Driven Development
- AI Native
- Modularidade
- Evolução Incremental

## Objetivos

O framework tem como objetivos:

- organizar a colaboração entre humanos e agentes de IA;
- reduzir perda de contexto durante o desenvolvimento;
- transformar especificações em unidades rastreáveis de trabalho;
- estabelecer limites claros para execução por agentes;
- manter documentação e implementação sincronizadas;
- favorecer evolução incremental e controlada;
- permitir auditoria de decisões, alterações e entregas.

## Estrutura do repositório

- `docs/`: especificação, governança, arquitetura conceitual e guias;
- `templates/`: modelos reutilizáveis para projetos DPF;
- `prompts/`: prompts oficiais para agentes de IA;
- `examples/`: projetos de referência;
- `schemas/`: contratos para validação estrutural dos documentos;
- `scripts/`: futuras ferramentas e automações.

## Início rápido da CLI

Em modo de desenvolvimento:

```bash
./dpf --help
./dpf version
python -m dpf_cli --help
```

Instalação local editável:

```bash
pip install -e . --no-build-isolation
```

Fluxo mínimo:

```bash
./dpf init --path ./meu-projeto --name "Meu Projeto" --context MPRJ
./dpf validate ./meu-projeto
./dpf status --path ./meu-projeto
```

## Estado atual

O projeto já possui sua primeira cadeia operacional consolidada da Fase 1 à Fase 10.

Fases implementadas ou consolidadas no repositório:

1. especificação oficial da metodologia;
2. biblioteca oficial de templates em nível normativo e operacional mínimo;
3. estrutura oficial dos projetos;
4. biblioteca oficial de prompts e contratos para agentes;
5. projetos oficiais de referência;
6. biblioteca operacional de prompts;
7. contratos e schemas;
8. validador oficial;
9. CLI oficial;
10. integração e automação.

Referência operacional das fases 5 a 10:

- [Phases 05-10 Execution Order](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/reference/PHASES-05-10-EXECUTION-ORDER.md)

## Versão

Versão inicial em desenvolvimento:

```text
DPF Specification v1.0
```

Versões atualmente distintas no repositório:

- especificação metodológica do DPF: `v1.0`
- CLI oficial local: `0.1.0`
- release oficial estável do repositório: ainda não publicada

Política formal:

- [Versioning Policy](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/governance/VERSIONING-POLICY.md)

## Status

```text
Base operacional implementada
```

## Licença

A licença oficial será definida antes da publicação da primeira versão estável.
# doistech-project-framework
