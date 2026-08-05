# Changelog

Todas as alterações relevantes do DoisTech Project Framework serão
documentadas neste arquivo.

O formato será baseado em versões e categorias de mudança.

## Não publicado

### Adicionado

- nenhum item.

### Alterado

- nenhum item.

### Corrigido

- nenhum item.

### Removido

- nenhum item.

## Versionamento

O DPF utilizará versionamento semântico quando sua primeira versão oficial
for publicada.

Formato:

```text
MAJOR.MINOR.PATCH
```

Exemplo:

```text
1.0.0
```

## 0.1.0 - 2026-08-05

### Adicionado

- estrutura inicial do repositório;
- documentação institucional;
- regras iniciais para agentes de IA;
- diretórios para especificação, templates, prompts, exemplos e schemas;
- especificação oficial da metodologia do DPF;
- especificação oficial da estrutura de projetos DPF;
- especificação oficial de agentes, prompts e contratos de execução do DPF;
- especificação normativa da biblioteca oficial de templates;
- biblioteca operacional mínima de templates em `templates/`;
- biblioteca mínima oficial de prompts do DPF;
- biblioteca oficial de prompts operacionais da Fase 6;
- projetos oficiais de referência da Fase 5;
- contratos e schemas de validação da Fase 7;
- exemplos válidos e inválidos de schemas;
- validador oficial MVP do DPF em `dpf_validator/`;
- testes automatizados do validador;
- CLI oficial MVP do DPF em `dpf_cli/`;
- entrada local `dpf` via `pyproject.toml`;
- testes automatizados da CLI;
- runner local de quality gate em `scripts/automation/`;
- workflows GitHub Actions para PR, main, release e validação manual;
- política de CI/CD;
- política formal de versionamento do repositório, da especificação e da CLI;
- guias, ADRs, relatórios de validação e referência operacional das Fases 5 a 10.

### Alterado

- README principal para refletir a base operacional consolidada do framework;
- documentação da CLI e da automação para refletir o uso da biblioteca oficial de templates;
- relatórios históricos para registrar que a materialização da Fase 2 ocorreu após as execuções originais das fases anteriores.

### Corrigido

- contagem de Tasks por estado no comando `dpf status`;
- contexto resolvido no quality gate de release quando a release pertence a um subprojeto DPF;
- comportamento de `dpf init --minimal`;
- consistência entre documentação operacional e estado real da Fase 2.

### Removido

- `.gitkeep` redundantes nos diretórios de `templates/` já materializados.
