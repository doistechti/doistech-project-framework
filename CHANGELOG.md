# Changelog

Todas as alterações relevantes do DoisTech Project Framework serão
documentadas neste arquivo.

O formato será baseado em versões e categorias de mudança.

## Não publicado

### Adicionado

- estrutura inicial do repositório;
- documentação institucional;
- regras iniciais para agentes de IA;
- diretórios para especificação, templates, prompts, exemplos e schemas.
- especificação oficial da estrutura de projetos DPF.
- especificação oficial de agentes, prompts e contratos de execução do DPF;
- biblioteca mínima oficial de prompts do DPF.
- projetos oficiais de referência da Fase 5;
- auditoria de templates e relatório de validação da Fase 5.
- biblioteca oficial de prompts operacionais da Fase 6;
- guia de uso da biblioteca de prompts;
- relatório de validação da Fase 6.
- contratos e schemas de validação da Fase 7;
- exemplos válidos e inválidos de schemas;
- relatório e matriz de validação da Fase 7.
- validador oficial MVP do DPF em `dpf_validator/`;
- testes automatizados do validador;
- guia de uso do validador;
- ADR de tecnologia do validador;
- relatório de validação da Fase 8.
- CLI oficial MVP do DPF em `dpf_cli/`;
- entrada local `dpf` via `pyproject.toml`;
- testes automatizados da CLI;
- guia e referência de comandos da CLI;
- ADR e relatório da Fase 9.
- runner local de quality gate em `scripts/automation/`;
- workflows GitHub Actions para PR, main, release e validação manual;
- política de CI/CD e guias de integração;
- ADR e relatório da Fase 10.
- atualização do README principal com o estado consolidado das Fases 1 a 10;
- referência interna da ordem de execução das Fases 5 a 10.
- materialização da biblioteca operacional mínima de templates em `templates/`.
- política formal de versionamento do repositório, da especificação e da CLI.

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
