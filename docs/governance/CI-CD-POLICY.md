# CI/CD Policy

## Objetivo

Definir a política oficial de automação, integração e execução contínua do DPF.

## Princípios

- a documentação permanece a fonte oficial da verdade;
- automações DEVEM chamar ferramentas oficiais já aprovadas;
- erros críticos DEVEM bloquear;
- avisos PODEM ser reportados sem bloquear, conforme o perfil da execução;
- publicação automática NÃO É permitida no MVP.

## Perfis de execução

### Pull request

Bloqueadores:

- falha de testes automatizados;
- falha do validador oficial;
- falha de sanity check dos schemas;
- falha de preparação do ambiente mínimo do runner.

Não bloqueadores:

- ausência de arquivo de changed files no runner local;
- avisos emitidos pelo validador sem erro impeditivo.

### Branch principal

Bloqueadores:

- qualquer erro do pull request;
- inconsistência nos exemplos oficiais;
- falha de status ou execução do quality gate principal.

### Preparação de Release

Bloqueadores:

- documento de release ausente;
- nome do arquivo fora da convenção;
- seção de itens incluídos ausente;
- `CHANGELOG` ausente;
- erros do validador ou dos testes.

### Validação manual

Bloqueadores:

- os mesmos do profile executado;
- qualquer erro da ferramenta oficial chamada.

## Permissões

Os workflows do MVP DEVEM usar:

- `contents: read`

Permissões adicionais NÃO DEVEM ser concedidas sem necessidade comprovada e decisão registrada.

## Forks

- workflows DEVEM usar o evento `pull_request`, não `pull_request_target`;
- segredos NÃO DEVEM ser exigidos para execução básica;
- automação NÃO DEVE comentar em PR automaticamente;
- automação NÃO DEVE executar código com credenciais persistidas.

## Supply chain

- ações DEVEM ser fixadas em versão estável explícita;
- `persist-credentials` DEVE ficar desabilitado no checkout;
- downloads adicionais NÃO DEVEM ser introduzidos sem justificativa;
- a automação DEVE preferir launcher local e código versionado no repositório.

## Exceções

Exceções temporárias DEVEM ser documentadas no relatório da fase ou em decisão formal.

O MVP NÃO prevê lista dinâmica de suppressions automáticas.

## Aprovação manual

Os workflows de preparação de release DEVEM servir como evidência de qualidade, não como autorização implícita de publicação.

Publicação, tag e release remota continuam dependentes de aprovação humana explícita.
