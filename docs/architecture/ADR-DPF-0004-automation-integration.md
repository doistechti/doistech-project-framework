# ADR-DPF-0004

## Título

Arquitetura de integração e automação do DPF

## Contexto

A Fase 10 exige automações seguras para validação, revisão e preparação de release sem alterar a metodologia nem duplicar regras em scripts ad hoc.

O repositório já possui:

- validador oficial em `dpf_validator/`;
- CLI oficial MVP em `dpf_cli/`;
- launcher local `./dpf`.

## Problema

Os workflows de CI/CD precisam chamar a lógica já aprovada, produzir evidência de execução e continuar válidos fora do GitHub Actions.

## Decisão

O DPF adota uma arquitetura em duas camadas:

1. runner local reutilizável em `scripts/automation/run_quality_gate.py`;
2. workflows GitHub Actions finos que chamam esse runner.

Os workflows NÃO DEVEM reimplementar regras documentais do DPF em YAML.

## Justificativa

Essa decisão:

- preserva uma única implementação operacional de quality gate;
- facilita execução local por humanos e agentes;
- reduz divergência entre CI e execução manual;
- mantém o YAML pequeno, previsível e auditável.

## Consequências

- o runner local vira contrato de automação do MVP;
- GitHub Actions atua como orquestrador, não como fonte de regra;
- futuras integrações com outras plataformas podem reutilizar o mesmo runner com baixa adaptação.
