# DoisTech Project Framework — DPF

O DoisTech Project Framework é um framework de engenharia de software para
projetos desenvolvidos de forma colaborativa por pessoas e agentes de
Inteligência Artificial.

O DPF define uma estrutura clara para transformar contexto, documentação,
planejamento, execução e validação em um fluxo rastreável, previsível e
seguro.

## Visão geral

Projetos com uso de IA costumam sofrer com perda de contexto, decisões mal
registradas, mudanças sem rastreabilidade e documentação desalinhada da
implementação.

O DPF foi criado para resolver esse problema com uma abordagem
documentation-first, orientada por contexto e preparada para colaboração
entre humanos e agentes.

Em vez de tratar IA como um atalho isolado, o framework a incorpora como
parte do processo de engenharia, com regras, limites, contratos e artefatos
claros.

## O que o DPF oferece

O repositório reúne os componentes centrais do framework:

- especificação oficial da metodologia;
- estrutura oficial para projetos DPF;
- biblioteca oficial de templates;
- prompts operacionais para agentes;
- projetos de referência;
- schemas de validação;
- validador oficial;
- CLI oficial;
- base inicial de automação.

## Problemas que o DPF ajuda a resolver

- perda de contexto durante o desenvolvimento;
- execução por IA sem escopo claramente definido;
- decisões espalhadas ou não documentadas;
- dificuldade de rastrear Features, Tasks e Releases;
- inconsistência entre documentação e implementação;
- baixa previsibilidade em fluxos colaborativos entre humanos e agentes.

## Princípios

O DPF é baseado nos seguintes princípios:

- Specification First
- Documentation as Source of Truth
- Context Driven Development
- AI Native
- Modularidade
- Evolução Incremental
- Human Accountability
- Least Necessary Change
- Traceability by Design

## Como funciona

O framework organiza o projeto com base na hierarquia oficial:

```text
Projeto
└── Capability
    └── Epic
        └── Feature
            └── Task
```

A partir dessa estrutura, o DPF define:

- onde cada artefato deve existir;
- como ele deve ser identificado;
- como se relaciona com os demais;
- quais estados são válidos;
- como agentes devem consumir contexto;
- como validar consistência documental e estrutural.

## Casos de uso

O DPF pode ser usado em projetos como:

- APIs;
- aplicações web;
- produtos SaaS;
- aplicativos mobile;
- integrações;
- automações;
- bibliotecas;
- modernização de sistemas legados;
- produtos internos;
- projetos conduzidos com apoio de agentes de IA.

## Início rápido

### Explorar a CLI

```bash
./dpf --help
./dpf version
python -m dpf_cli --help
```

### Inicializar um projeto DPF

```bash
./dpf init --path ./meu-projeto --name "Meu Projeto" --context MPRJ
```

### Validar um projeto

```bash
./dpf validate ./meu-projeto
```

### Ler o status documental do projeto

```bash
./dpf status --path ./meu-projeto
```

## Estrutura do repositório

```text
docs/           documentação oficial do framework
templates/      templates oficiais
prompts/        prompts e contratos para agentes
examples/       projetos de referência
schemas/        contratos e schemas de validação
scripts/        automações e quality gates
dpf_cli/        CLI oficial
dpf_validator/  validador oficial
```

## Documentação principal

- [DPF Specification v1.0](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/specification/DPF-SPECIFICATION-v1.0.md)
- [DPF Templates Specification v1.0](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/specification/DPF-TEMPLATES-SPECIFICATION-v1.0.md)
- [DPF Project Structure](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/architecture/DPF-PROJECT-STRUCTURE.md)
- [CLI Usage Guide](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/guides/CLI-USAGE-GUIDE.md)
- [Validator Usage Guide](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/guides/VALIDATOR-USAGE-GUIDE.md)
- [Versioning Policy](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/governance/VERSIONING-POLICY.md)
- [Release 0.1.0 Notes](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/reference/RELEASE-0.1.0-NOTES.md)

## Status do projeto

Estado atual do repositório:

- especificação metodológica vigente: `DPF Specification v1.0`
- CLI oficial local: `0.1.0`
- release atual do repositório: `0.1.0`

O projeto já possui uma base operacional funcional para estruturação,
validação e apoio à execução de projetos com DPF.

## Posicionamento do projeto

Este repositório tem dois papéis ao mesmo tempo:

- framework open-source para organização de projetos com IA;
- base pública de referência do trabalho da DoisTech em engenharia de
  software assistida por agentes.

## Licença

A licença final do projeto ainda está em definição.
Até sua publicação oficial, consulte o arquivo `LICENSE` do repositório.
