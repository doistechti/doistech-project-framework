# ADR-DPF-0002

## Título

Tecnologia mínima do validador oficial do DPF

## Contexto

A Fase 8 autoriza a primeira implementação de software do repositório e exige um validador local, determinístico, seguro e portátil para projetos DPF.

O repositório ainda não possui estratégia de distribuição, empacotamento ou CLI completa aprovada. A solução escolhida precisa funcionar localmente em macOS, Linux e Windows sem depender de serviços externos.

## Alternativas avaliadas

### 1. Shell script

Vantagens:

- execução simples em ambientes Unix;
- baixa complexidade inicial.

Limitações:

- portabilidade fraca para Windows;
- parsing de Markdown e front matter pouco robusto;
- testes automatizados mais frágeis.

### 2. Node.js com dependências externas

Vantagens:

- ecossistema maduro para CLI e parsing;
- boa ergonomia para saída JSON e terminal.

Limitações:

- introduz gerenciador de dependências antes da Fase 9;
- aumenta superfície de instalação;
- adiciona churn estrutural desnecessário para o MVP.

### 3. Python com dependências externas

Vantagens:

- boa portabilidade;
- bibliotecas prontas para YAML e JSON Schema.

Limitações:

- adiciona bootstrap de dependências no primeiro validador;
- reduz determinismo do ambiente local antes de uma política oficial de distribuição.

### 4. Python padrão com biblioteca padrão

Vantagens:

- amplamente disponível;
- não requer instalação de dependências do projeto;
- permite parser controlado, leitura segura de arquivos, testes com `unittest` e saída JSON determinística;
- mantém o MVP pequeno e auditável.

Limitações:

- parser YAML deliberadamente restrito;
- sem execução completa de JSON Schema nesta fase;
- menos ergonomia que uma stack dedicada de CLI.

## Decisão

O validador oficial do MVP DEVE ser implementado em Python usando apenas a biblioteca padrão.

O comando provisório aprovado para a Fase 8 é:

```bash
python -m dpf_validator validate .
```

## Justificativa

Essa escolha atende melhor aos critérios aprovados para o MVP:

- portabilidade suficiente;
- baixa fricção de execução;
- ausência de dependências externas;
- testes automatizados simples;
- controle explícito sobre leitura segura, limites de arquivo e links simbólicos;
- separação clara entre descoberta, parsing, validação e formatação.

## Consequências

- o pacote `dpf_validator/` passa a ser a implementação oficial provisória do validador;
- a CLI completa permanece fora de escopo;
- a validação de schema nesta fase é orientada por regras do repositório e alinhada aos contratos da Fase 7, sem engine externa completa de JSON Schema;
- a Fase 9 poderá empacotar, distribuir ou expandir a interface sem invalidar o núcleo de validação já implementado.
