# VERSIONING-POLICY

## Objetivo

Definir a política oficial de versionamento do repositório do DoisTech Project Framework.

Esta política separa explicitamente:

- versão da especificação metodológica do DPF;
- versão dos componentes executáveis do repositório, como CLI e validador;
- versão de release do repositório oficial;
- versão de releases de projetos que adotam o DPF.

## Princípio central

Essas versões NÃO DEVEM ser tratadas como sinônimos.

Cada uma responde a uma pergunta diferente:

- `Qual versão da metodologia está aprovada?`
- `Qual versão da ferramenta está instalada ou executando?`
- `Qual versão consolidada do repositório oficial foi publicada?`
- `Qual versão de produto foi liberada por um projeto que usa o DPF?`

## Tipos oficiais de versão

### 1. Versão da especificação do DPF

Identifica a versão normativa da metodologia.

Exemplos:

- `DPF Specification v1.0`
- `DPF Templates Specification v1.0`
- `DPF Project Structure Specification v1.0`

Regras:

- DEVE ser tratada como versão normativa;
- DEVE evoluir quando a metodologia, seus contratos ou suas regras oficiais forem alterados;
- NÃO DEVE ser inferida a partir da versão da CLI;
- PODE ser mantida em formato documental próprio, como `v1.0`, `v1.1` ou equivalente aprovado.

Estado atual em 5 de agosto de 2026:

- especificação-base vigente: `DPF Specification v1.0`

### 2. Versão da CLI e dos componentes executáveis

Identifica a versão do software distribuível deste repositório.

Abrange, no mínimo:

- `dpf_cli`
- `dpf_validator`
- launcher local `dpf`

Regras:

- DEVE usar versionamento semântico;
- DEVE ser registrada em local técnico canônico do pacote;
- NÃO DEVE ser confundida com a versão normativa da metodologia;
- PODE evoluir sem alterar a versão da especificação, desde que preserve compatibilidade com ela;
- DEVE registrar incompatibilidades relevantes em changelog e documentação.

Estado atual em 5 de agosto de 2026:

- versão da CLI local: `0.1.0`

### 3. Versão de release do repositório oficial do DPF

Identifica uma publicação consolidada do próprio repositório `doistech-project-framework`.

Exemplos conceituais:

- `0.1.0`
- `0.2.0`
- `1.0.0`

Regras:

- DEVE usar versionamento semântico;
- DEVE refletir o estado publicado do repositório como produto documental e operacional;
- PODE agrupar mudanças em documentação, templates, prompts, CLI, validador e automações;
- NÃO DEVE ser automaticamente igual à versão da especificação;
- NÃO DEVE ser automaticamente igual à versão interna da CLI.

Interpretação recomendada:

- `0.x.y`: base ainda em consolidação;
- `1.0.0`: primeira release oficial estável do repositório;
- `MAJOR` seguinte: mudança incompatível no contrato oficial do repositório;
- `MINOR`: evolução compatível de capacidade;
- `PATCH`: correção compatível.

Estado atual em 5 de agosto de 2026:

- não há release oficial estável formalmente publicada para o repositório;
- `1.0.0` aparece apenas como exemplo de formato, não como release publicada.

### 4. Versão de release de projetos que usam o DPF

Identifica a versão de produto ou entrega de um projeto estruturado com o DPF.

Exemplos:

- `1.0.0`
- `2.3.1`
- `2026.08`

Regras:

- pertence ao projeto consumidor do DPF, não ao framework em si;
- DEVE ser registrada em seus próprios artefatos de release;
- PODE usar semver ou outro padrão aprovado pelo projeto;
- NÃO DEVE ser confundida com a versão do framework.

## Matriz de responsabilidade

| Tipo | Pergunta respondida | Escopo | Formato padrão | Local canônico |
| --- | --- | --- | --- | --- |
| Especificação do DPF | Qual metodologia está aprovada? | Normativo | `v1.0` | documentos de especificação |
| CLI e executáveis | Qual ferramenta está rodando? | Software | `MAJOR.MINOR.PATCH` | manifesto técnico do pacote |
| Release do repositório DPF | Qual versão do framework foi publicada? | Repositório oficial | `MAJOR.MINOR.PATCH` | release oficial e changelog |
| Release de projeto DPF | Qual versão do produto foi liberada? | Projeto consumidor | definido pelo projeto | artefatos de release do projeto |

## Regras de evolução

### Especificação metodológica

- Mudança incompatível na metodologia DEVE gerar nova versão principal da especificação normativa.
- Adição compatível DEVE gerar nova versão secundária da especificação normativa.
- Correção editorial PODE gerar nova versão de correção ou revisão documental equivalente.

### CLI e validador

- Mudança incompatível na interface pública DEVE incrementar `MAJOR`.
- Nova capacidade compatível DEVE incrementar `MINOR`.
- Correção compatível DEVE incrementar `PATCH`.

### Repositório oficial

- A publicação oficial do repositório DEVE considerar o conjunto consolidado:
  - especificações;
  - templates;
  - prompts;
  - exemplos;
  - schemas;
  - CLI;
  - validador;
  - automações.

## Política de compatibilidade

- A CLI DEVE declarar com qual versão normativa do DPF é compatível.
- O validador DEVE evoluir de forma compatível com os contratos e schemas aprovados.
- O repositório DEVE evitar publicar artefatos executáveis incompatíveis com a especificação vigente sem documentação explícita de migração.

## Estado atual recomendado

Até a primeira publicação oficial estável, o repositório DEVERIA ser interpretado assim:

- especificação normativa do DPF: `v1.0`
- CLI oficial local: `0.1.0`
- release oficial do repositório: `não publicada`

## Próximos passos normativos

Antes da primeira release oficial do repositório, DEVE ser definido:

1. o identificador oficial da primeira release publicada;
2. o critério de compatibilidade entre especificação e CLI;
3. a política de migração quando a especificação avançar para nova versão;
4. a política de versionamento do validador e das automações;
5. o processo formal de publicação de release do repositório.
