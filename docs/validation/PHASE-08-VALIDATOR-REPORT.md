# PHASE-08-VALIDATOR-REPORT

## Escopo

Implementação do MVP do validador oficial do DPF para uso local, seguro e determinístico.

## Arquitetura

O validador foi estruturado em módulos separados:

- `dpf_validator/discovery.py`: descoberta do projeto e classificação de documentos;
- `dpf_validator/parsing.py`: leitura segura, front matter e extrações textuais;
- `dpf_validator/validators.py`: regras estruturais e cruzadas;
- `dpf_validator/results.py`: modelo de findings e agregação;
- `dpf_validator/formatters.py`: saída humana e JSON;
- `dpf_validator/cli.py`: interface de execução provisória;
- `dpf_validator/__main__.py`: entrada `python -m`.

## Tecnologia

- linguagem: Python;
- dependências externas: nenhuma;
- testes: `unittest`;
- formato de saída: terminal e JSON.

Decisão registrada em [ADR-DPF-0002-validator-technology.md](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/docs/architecture/ADR-DPF-0002-validator-technology.md).

## Regras implementadas

- estrutura mínima obrigatória do projeto;
- presença de manifesto `dpf-project.yaml`;
- validação de IDs por tipo de artefato;
- validação de estados por tipo;
- detecção de IDs duplicados;
- detecção de links relativos quebrados;
- bloqueio de links fora da raiz;
- ignorar links simbólicos por segurança;
- rejeição de arquivos excessivamente grandes;
- Feature sem critérios de aceite;
- Task sem critérios de conclusão;
- Release sem itens incluídos;
- artefato cancelado sem justificativa;
- Task sem Feature pai identificável;
- parent de Task incompatível com a Feature do caminho;
- consistência entre Task e `TASKS.md`;
- Feature concluída com Tasks abertas;
- Release concluída com Feature ausente ou incompleta;
- dependências circulares detectáveis;
- conflito entre status arquivado e caminho ativo.

## Cobertura de testes

Casos cobertos em [tests/test_validator.py](/Users/doistechti/Projetos/DOISTECH/doistech-project-framework/tests/test_validator.py):

- projeto mínimo válido;
- projeto completo válido;
- ID duplicado;
- link quebrado;
- Task órfã por parent incompatível;
- Feature sem aceite;
- estado inválido;
- Release inconsistente;
- arquivo malformado;
- caminho inseguro por link simbólico;
- saída JSON;
- códigos de saída.

## Comandos executados

Em 4 de agosto de 2026, executei:

```bash
python3 -m unittest -v tests/test_validator.py
python3 -m dpf_validator validate examples/minimal-project
python3 -m dpf_validator validate examples/minimal-project --format json
python3 -m dpf_validator validate examples/complete-project
```

## Resultados

- suíte de testes: `OK`
- projeto mínimo: `0 erros`
- projeto completo: `0 erros`
- saída JSON: produzida com `error_count`, `warning_count`, `info_count` e lista de findings

## Limitações

- a validação de schemas nesta fase é orientada pelas regras aprovadas e pelos contratos da Fase 7, mas não usa ainda uma engine externa completa de JSON Schema;
- o parser de front matter suporta apenas o subconjunto necessário ao DPF;
- o comando provisório ainda depende de `python -m`;
- não há empacotamento, instalador ou binário dedicado.

## Riscos

- divergências futuras se a Fase 2 operacional materializar templates com campos adicionais ainda não refletidos no parser;
- necessidade de expansão da validação de manifesto e compatibilidade de versões quando a Fase 9 formalizar distribuição;
- ausência atual de documentos em `docs/governance/` reduz o alcance de regras normativas futuras.

## Pendências para a CLI

- comando oficial `dpf validate`;
- seleção de alvo por perfil ou escopo;
- saída resumida e detalhada por opção;
- integração opcional com CI/CD;
- validação formal de schema com estratégia de compatibilidade versionada;
- validações incrementais e modo estrito.
