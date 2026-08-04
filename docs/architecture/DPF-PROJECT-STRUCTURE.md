# DPF Project Structure Specification v1.0

**Status:** Oficial  
**Framework:** DoisTech Project Framework (DPF)  
**Versão:** 1.0  
**Data:** 2026-08-04  
**Classificação:** Especificação normativa da estrutura oficial de projetos  
**Documento ID:** DOC-DPF-STRUCTURE-0001  
**Documentos normativos relacionados:** `DPF-SPECIFICATION-v1.0.md`, `DPF-TEMPLATES-SPECIFICATION-v1.0.md`

> Este documento define a estrutura oficial para projetos que adotam o DoisTech Project Framework. Ele determina onde os artefatos existem, como são identificados, como se relacionam e como são mantidos ao longo do ciclo de vida do projeto. Não altera a metodologia definida na Fase 1 nem recria os templates definidos na Fase 2.

## 1. Identificação e status

Este documento é a referência oficial para organização estrutural de projetos DPF.

Seu conteúdo possui caráter normativo e DEVE ser utilizado como contrato estrutural por:

- projetos novos;
- projetos em adoção progressiva;
- futuras automações;
- futuros validadores;
- futura CLI;
- futuro dashboard;
- futuros agentes especializados.

## 2. Introdução

O DPF exige que a documentação seja navegável, estável, rastreável e consumível por humanos e agentes. Para isso, um projeto DPF NÃO PODE depender apenas de convenções implícitas de time, memória institucional ou organização casual de diretórios.

Esta especificação estabelece uma estrutura física e documental previsível, proporcional e independente de tecnologia.

## 3. Escopo

Esta especificação define:

- estrutura raiz do repositório;
- diretório oficial do DPF;
- organização dos artefatos metodológicos;
- representação física da hierarquia `Projeto > Capability > Epic > Feature > Task`;
- convenções de IDs, nomes, estados e metadados;
- políticas de índices, rastreabilidade, versionamento e arquivamento;
- perfis proporcionais para projetos pequenos, médios e grandes;
- estratégia de adoção em projetos legados.

Esta especificação NÃO define:

- código-fonte;
- ferramentas;
- automações;
- integração com fornecedores;
- infraestrutura específica;
- templates novos;
- processos fora do escopo documental e estrutural.

## 4. Termos normativos

Aplicam-se os termos normativos da `DPF Specification v1.0`.

- **DEVE / OBRIGATÓRIO:** requisito necessário para conformidade.
- **NÃO DEVE / PROIBIDO:** prática vedada.
- **DEVERIA / RECOMENDADO:** prática esperada, salvo justificativa registrada.
- **PODE / OPCIONAL:** escolha permitida.

## 5. Princípios estruturais

Toda estrutura DPF DEVE obedecer aos seguintes princípios:

1. **Specification First:** artefatos estruturais servem à especificação antes da implementação.
2. **Documentation as Source of Truth:** o repositório documental representa a intenção oficial do projeto.
3. **Context Driven Development:** a estrutura DEVE facilitar contexto proporcional por tarefa.
4. **AI Native:** caminhos, nomes e relações DEVE ser previsíveis para leitura automatizada.
5. **Modularidade:** documentos DEVE ser particionados por responsabilidade.
6. **Evolução Incremental:** a estrutura DEVE funcionar desde o primeiro dia do projeto.
7. **Human Accountability:** aprovação e transição de estados críticos DEVE ter responsável humano.
8. **Least Necessary Change:** a estrutura NÃO DEVE induzir movimentações desnecessárias.
9. **Traceability by Design:** cada artefato relevante DEVE apontar para sua origem, contexto e efeitos.

## 6. Análise das alternativas

### 6.1 Organização por tipo de documento

Vantagens:

- simples de entender;
- fácil de indexar.

Limitações:

- separa documentos que pertencem à mesma Feature;
- piora consumo contextual por agentes;
- aumenta navegação cruzada.

### 6.2 Organização estritamente hierárquica

Vantagens:

- excelente rastreabilidade ascendente;
- contexto local forte.

Limitações:

- artefatos globais ficam mal posicionados;
- regras, decisões e releases tendem a ser replicadas;
- dificulta itens transversais.

### 6.3 Organização híbrida

Vantagens:

- preserva hierarquia oficial onde ela importa;
- mantém artefatos transversais em áreas próprias;
- reduz duplicação;
- favorece automação e leitura por agentes.

Limitações:

- exige convenções mais explícitas;
- requer bons índices.

### 6.4 Decisão estrutural

O DPF ADOTA oficialmente uma **organização híbrida**:

- artefatos globais e transversais ficam em diretórios funcionais dentro de `dpf/`;
- a hierarquia `Capability > Epic > Feature > Task` é representada fisicamente em árvore dentro de `dpf/capabilities/`;
- artefatos de suporte permanecem referenciados, não copiados;
- índices resumem e conectam áreas sem substituir suas fontes primárias.

Essa decisão equilibra rastreabilidade, legibilidade, escalabilidade e automação futura.

## 7. Estrutura raiz

A raiz mínima oficial de um projeto DPF DEVE seguir o padrão abaixo:

```text
projeto/
├── AGENTS.md
├── README.md
├── dpf/
├── src/                # opcional
├── tests/              # opcional
├── infra/              # opcional
├── scripts/            # opcional
├── assets/             # opcional
├── docs-external/      # opcional
└── .gitignore
```

Regras:

- `AGENTS.md` DEVE existir na raiz para orientar agentes operacionais no repositório.
- `README.md` DEVE existir na raiz como ponto de entrada humano.
- `dpf/` DEVE existir em qualquer projeto que adote formalmente o DPF.
- `src/`, `tests/`, `infra/`, `scripts/` e `assets/` PODEM não existir em projetos ainda não implementados.
- diretórios de build, cache, ambientes locais, artefatos gerados e temporários NÃO DEVEM ser versionados.
- documentação metodológica oficial NÃO DEVE ficar misturada com documentação de fornecedor, IDE ou ferramenta.

## 8. Estrutura documental

O diretório oficial do DPF DEVE ser:

```text
dpf/
```

Justificativa:

- curto e previsível;
- semanticamente claro;
- neutro em relação à tecnologia;
- fácil de localizar por agentes;
- adequado à futura CLI, dashboard e validadores;
- separa metodologia de implementação sem esconder sua centralidade.

Estrutura documental oficial recomendada:

```text
dpf/
├── PROJECT.md
├── PROJECT-STATE.md
├── ROADMAP.md
├── RELEASES.md
├── CHANGELOG.md
├── PLANNED.md
├── IMPLEMENTED.md
├── CURRENT-SPRINT.md                # opcional
├── dpf-project.yaml
├── capabilities/
├── product/
├── architecture/
├── decisions/
├── releases/
├── validation/
├── context/
└── archive/
```

Responsabilidades:

- `PROJECT.md`: identidade e governança do projeto.
- `PROJECT-STATE.md`: resumo operacional atual.
- `ROADMAP.md`: direção temporal.
- `RELEASES.md`: índice consolidado de releases.
- `CHANGELOG.md`: mudanças relevantes do produto.
- `PLANNED.md`: visão consolidada do planejado.
- `IMPLEMENTED.md`: visão consolidada do entregue.
- `capabilities/`: árvore oficial da hierarquia principal.
- `product/`: visão, regras, casos de uso, workflows e glossário.
- `architecture/`: arquitetura vigente, integrações, dados, segurança e infraestrutura documental.
- `decisions/`: Architecture Decisions e índice associado.
- `releases/`: registros individuais de release e release notes.
- `validation/`: evidências, revisões, auditorias e relatórios de conformidade.
- `context/`: materiais contextuais complementares e estáveis.
- `archive/`: itens históricos cujo consumo operacional corrente não é mais esperado.

## 9. Representação da hierarquia

A hierarquia oficial do DPF DEVE ser representada fisicamente em `dpf/capabilities/`.

Árvore canônica:

```text
dpf/capabilities/
└── CAP-<contexto>-<nnnn>-<slug>/
    ├── CAPABILITY.md
    ├── EPICS.md
    ├── epics/
    │   └── EPC-<contexto>-<nnnn>-<slug>/
    │       ├── EPIC.md
    │       ├── FEATURES.md
    │       └── features/
    │           └── FEAT-<contexto>-<nnnn>-<slug>/
    │               ├── FEATURE.md
    │               ├── TASKS.md
    │               ├── tasks/
    │               │   └── TASK-<contexto>-<nnnn>-<slug>.md
    │               ├── validation/
    │               └── evidence/
    └── archive/
```

Regras:

- toda `Capability` DEVE possuir diretório próprio;
- toda `Epic` DEVE possuir diretório próprio;
- toda `Feature` DEVE possuir diretório próprio;
- toda `Task` DEVE existir ao menos em `TASKS.md`;
- `Task` individual em arquivo próprio DEVE ser criada quando a complexidade, criticidade, duração, risco ou necessidade de contexto detalhado justificar;
- nenhum componente técnico substitui um nível hierárquico do DPF.

## 10. Convenções de identificação

### 10.1 Padrão oficial

O padrão oficial de ID do DPF é:

```text
<TIPO>-<CONTEXTO>-<NNNN>
```

Onde:

- `TIPO`: prefixo fixo do artefato;
- `CONTEXTO`: código curto estável do projeto, domínio ou macrocontexto;
- `NNNN`: numeração sequencial com zero à esquerda.

Exemplos de prefixo:

- `PRJ`
- `CAP`
- `EPC`
- `FEAT`
- `TASK`
- `BR`
- `UC`
- `WF`
- `ADR`
- `DEBT`
- `RISK`
- `REL`
- `MILE`
- `PROMPT`
- `AGENT`
- `DOC`
- `CR`

### 10.2 Regras

- IDs DEVE ser imutáveis.
- IDs NÃO DEVEM carregar estado.
- IDs NÃO DEVEM ser reutilizados após cancelamento, substituição ou arquivamento.
- A numeração DEVE ser única por tipo e contexto de projeto.
- O contexto DEVE ser curto, estável e documentado em `dpf-project.yaml`.
- Projetos pequenos PODEM usar um único contexto principal.
- Projetos grandes PODEM usar contexto de domínio, desde que a regra seja uniforme.

### 10.3 Decisão sobre unicidade

O DPF ADOTA **unicidade contextual por projeto**, não unicidade global entre repositórios.

Exemplo:

- `FEAT-CORE-0042`
- `TASK-CORE-0187`

Essa decisão preserva legibilidade local, evita dependência de registradores externos e continua adequada à automação.

## 11. Convenções de nomenclatura

### 11.1 Diretórios

- Diretórios estruturais fixos DEVE usar `lowercase-kebab-case`.
- Diretórios de instância DEVE usar `<ID>-<slug>`.
- O `slug` DEVE usar apenas ASCII minúsculo, números e hífen.
- Espaços, acentuação, underscore e caracteres especiais NÃO DEVEM ser usados.

Exemplo:

```text
FEAT-CORE-0012-consultar-horarios-disponiveis
```

### 11.2 Arquivos

- Arquivos canônicos derivados da biblioteca oficial DEVE manter seus nomes oficiais em maiúsculas, por exemplo `PROJECT.md`, `FEATURE.md`, `TASKS.md`, `SYSTEM-DESIGN.md`.
- Arquivos individuais de instância DEVE usar o ID no nome.
- Datas PODEM aparecer em nomes apenas quando o documento for temporal por natureza.
- Status NÃO DEVE ser codificado no nome do arquivo; DEVE ficar nos metadados.
- Versão de documento PODE aparecer no nome apenas quando o documento for uma especificação normativa versionada.

## 12. Metadados

Todo documento DPF DEVE possuir front matter YAML mínimo no início do arquivo.

Formato base:

```yaml
id: FEAT-CORE-0012
title: Consultar horarios disponiveis
type: feature
status: active
version: 1.0
owner: product-owner
author: business-analyst
approver: product-owner
created_at: 2026-08-04
updated_at: 2026-08-04
parent: EPC-CORE-0004
related:
  - BR-CORE-0011
  - UC-CORE-0007
tags:
  - scheduling
```

Metadados mínimos:

- `id`
- `title`
- `type`
- `status`
- `version`
- `owner`
- `author`
- `approver`
- `created_at`
- `updated_at`
- `parent` quando aplicável
- `related`

Campos adicionais RECOMENDADOS quando aplicável:

- `release`
- `milestone`
- `dependencies`
- `supersedes`
- `superseded_by`
- `effective_from`
- `effective_until`

Front matter foi escolhido porque:

- é legível por humanos;
- é parseável por automação futura;
- é independente de ferramenta;
- reduz ambiguidade.

## 13. Estados

Estados oficiais mínimos:

| Artefato | Estados mínimos |
| --- | --- |
| Capability | `draft`, `active`, `blocked`, `done`, `canceled`, `archived` |
| Epic | `draft`, `active`, `blocked`, `done`, `canceled`, `archived` |
| Feature | `draft`, `ready`, `active`, `blocked`, `implemented`, `validated`, `released`, `canceled`, `archived` |
| Task | `draft`, `ready`, `active`, `blocked`, `done`, `validated`, `canceled`, `archived` |
| Architecture Decision | `proposed`, `approved`, `rejected`, `superseded`, `archived` |
| Release | `planned`, `ready`, `approved`, `released`, `rolled-back`, `canceled`, `archived` |
| Business Rule | `draft`, `active`, `deprecated`, `archived` |
| Technical Debt | `identified`, `planned`, `active`, `mitigated`, `accepted`, `archived` |
| Risk | `identified`, `monitoring`, `mitigating`, `accepted`, `closed`, `archived` |
| Documento | `draft`, `active`, `superseded`, `archived` |

Regras:

- transições críticas DEVE ser registradas no histórico do artefato;
- `approved`, `released`, `validated` e equivalentes DEVE ter responsável humano identificado;
- um item `archived` NÃO PODE ser apresentado como vigente em índices operacionais;
- transições inválidas DEVE ser tratadas como inconsistência estrutural.

## 14. Project State

O `Project State` DEVE ser representado por:

- `dpf/PROJECT-STATE.md` como documento central;
- índices auxiliares referenciados, não copiados;
- seções manualmente mantidas e futuramente automatizáveis.

O `PROJECT-STATE.md` DEVE responder rapidamente:

- qual é a situação geral do projeto;
- qual release está vigente ou em preparação;
- quais Capabilities e Epics estão ativas;
- quais Features estão planejadas, em andamento, validadas e liberadas;
- quais Tasks estão abertas ou bloqueadas;
- quais decisões recentes impactam execução;
- quais riscos e dívidas exigem atenção;
- quais documentos são prioritários para leitura;
- qual contexto mínimo um agente novo deve consultar.

Ele NÃO DEVE duplicar integralmente `FEATURE.md`, `TASKS.md`, `RELEASES.md` ou `DECISIONS.md`.

## 15. Organização de Capabilities

Cada Capability DEVE possuir:

- diretório próprio em `dpf/capabilities/`;
- arquivo principal `CAPABILITY.md`;
- índice `EPICS.md`;
- subdiretório `epics/`;
- histórico no próprio documento ou em seção dedicada;
- referência ao Projeto, responsáveis, dependências e documentos associados.

Roadmap específico por Capability:

- PODE existir quando a Capability for duradoura, transversal ou multi-time;
- DEVE ficar no diretório da Capability;
- NÃO substitui o `ROADMAP.md` global.

Capability transversal a múltiplos componentes técnicos:

- DEVE continuar representada como Capability única;
- PODE referenciar múltiplos componentes em `SYSTEM-DESIGN.md`, APIs, dados ou infraestrutura;
- NÃO DEVE ser fragmentada apenas por conveniência técnica.

## 16. Organização de Epics

Cada Epic DEVE possuir:

- diretório próprio dentro da Capability;
- arquivo principal `EPIC.md`;
- índice `FEATURES.md`;
- subdiretório `features/`;
- relacionamentos com `ROADMAP.md`, `MILESTONES.md` e `RELEASES.md`, quando aplicável.

Políticas:

- Epic concluída DEVE permanecer em seu caminho canônico com estado `done` ou `archived`;
- Epic cancelada DEVE permanecer rastreável com estado `canceled` e justificativa;
- Epic arquivada NÃO DEVE desaparecer do índice da Capability; DEVE aparecer em seção histórica.

## 17. Organização de Features

A Feature é a principal unidade documental operacional do DPF.

Cada Feature DEVE possuir diretório próprio contendo, no mínimo:

```text
FEAT-.../
├── FEATURE.md
├── TASKS.md
├── tasks/
├── validation/
└── evidence/
```

Distribuição de conteúdo:

- `FEATURE.md`: objetivo, escopo, comportamento, critérios de aceite, regras relacionadas, dependências, referências.
- `TASKS.md`: controle consolidado das Tasks da Feature.
- `tasks/`: arquivos individuais quando exigidos.
- `validation/`: relatórios de revisão, testes, conformidade e aceite.
- `evidence/`: referências ou manifestos de evidências permanentes.

Documentos separados PODEM ser adicionados quando a complexidade justificar, por exemplo:

- `USE-CASES.md`
- `WORKFLOW.md`
- `API.md`
- `TESTS.md`
- `DECISIONS.md`

Regra central:

- a Feature DEVE fornecer contexto suficiente para um agente executar uma Task sem ler o projeto inteiro.

## 18. Organização de Tasks

O DPF ADOTA política híbrida para Tasks:

- `TASKS.md` é OBRIGATÓRIO em toda Feature;
- arquivos individuais em `tasks/` são OBRIGATÓRIOS quando a Task:
  - for executada por agente;
  - durar mais de uma sessão relevante;
  - possuir risco ou impacto não trivial;
  - envolver múltiplas áreas permitidas;
  - exigir evidência própria;
  - depender de validação formal;
  - tratar segurança, dados, migração, release ou mudança arquitetural.

Cada Task individual DEVE possuir:

- identificador único;
- Feature relacionada;
- objetivo;
- escopo;
- contexto;
- entradas;
- saídas;
- áreas ou arquivos permitidos;
- restrições;
- dependências;
- critérios de aceitação;
- critérios de validação;
- testes;
- Definition of Ready;
- Definition of Done;
- responsável;
- executor humano ou agente;
- estado;
- resultado;
- evidências;
- documentação afetada.

## 19. Business Rules

As Business Rules DEVE ser organizadas em:

```text
dpf/product/business-rules/
├── BUSINESS-RULES.md
└── BR-<contexto>-<nnnn>-<slug>.md   # opcional
```

Política oficial:

- `BUSINESS-RULES.md` DEVE existir como catálogo consolidado;
- regras críticas, extensas ou de alto risco DEVE possuir arquivo individual;
- regras simples PODEM permanecer apenas no catálogo;
- Features NÃO DEVEM esconder regra inédita em seu próprio documento;
- toda Feature que depende de regra DEVE referenciar o ID da Business Rule.

## 20. Use Cases

Os Use Cases DEVE ser organizados em:

```text
dpf/product/use-cases/
├── USE-CASES.md
└── UC-<contexto>-<nnnn>-<slug>.md
```

Regras:

- Use Case é OBRIGATÓRIO quando a interação do ator impacta comportamento, exceções, aprovação, integração ou fluxo crítico;
- PODE ser opcional em Features pequenas e autoevidentes;
- cada Use Case DEVE referenciar atores, objetivo, fluxo principal, alternativos, exceções e regras relacionadas;
- um Use Case PODE fundamentar múltiplas Features.

## 21. Workflows

Os Workflows DEVE ser organizados em:

```text
dpf/product/workflows/
├── WORKFLOWS.md
└── WF-<contexto>-<nnnn>-<slug>.md
```

Regras:

- Workflow global DEVE ser usado quando o processo atravessa múltiplas Features;
- Workflow específico DEVE ficar referenciado pela Feature quando o escopo for local;
- diagramas gráficos são OPCIONAIS;
- representação textual é SUFICIENTE e OBRIGATÓRIA;
- versões e regras associadas DEVE ser explicitadas no próprio Workflow.

## 22. Architecture Decisions

As Architecture Decisions DEVE ser organizadas em:

```text
dpf/decisions/
├── DECISIONS.md
└── ADR-<contexto>-<nnnn>-<slug>.md
```

Regras:

- `DECISIONS.md` DEVE funcionar como índice oficial;
- cada ADR aprovada DEVE ser preservada permanentemente;
- ADR substituída DEVE apontar para a substituta;
- `SYSTEM-DESIGN.md` DEVE refletir o estado arquitetural vigente, mas NÃO substitui ADRs;
- Tasks ou Features com impacto arquitetural DEVE referenciar ADR aplicável.

## 23. APIs e dados

Artefatos de interface e dados DEVE ficar em:

```text
dpf/architecture/
├── SYSTEM-DESIGN.md
├── api/
│   ├── API.md
│   └── contracts/
└── data/
    ├── DATABASE.md
    └── models/
```

Regras:

- `API.md` PODE ser global ou por domínio;
- `DATABASE.md` PODE ser global ou por domínio;
- modelos específicos PODEM existir em subdiretórios;
- artefatos técnicos DEVE apontar para Features, regras e decisões relevantes;
- documentação técnica NÃO DEVE ficar apenas no código.

## 24. Testes e evidências

Testes e evidências documentais DEVE ficar em:

```text
dpf/validation/
├── TESTS.md
├── reviews/
├── reports/
└── evidence/
```

Além disso, cada Feature PODE manter `validation/` e `evidence/` locais.

Política:

- evidências leves PODEM ser armazenadas no repositório;
- evidências pesadas PODEM ser referenciadas externamente;
- referências externas DEVE ser estáveis e rastreáveis;
- toda Task concluída DEVE possuir evidência suficiente para auditoria proporcional;
- evidências permanentes DEVE cobrir aprovação, teste, revisão e implantação quando aplicável.

## 25. Releases

As Releases DEVE ser organizadas em:

```text
dpf/releases/
├── RELEASES.md
├── REL-<contexto>-<nnnn>-<slug>.md
└── notes/
```

Cada Release DEVE possuir:

- ID;
- versão do produto, quando aplicável;
- objetivo;
- escopo;
- Features;
- Tasks técnicas relevantes;
- correções;
- mudanças incompatíveis;
- riscos;
- dependências;
- testes;
- evidências;
- plano de implantação;
- rollback;
- aprovação;
- estado;
- data prevista;
- data efetiva;
- ambientes;
- referência ao `CHANGELOG.md`.

Diferenças obrigatórias:

- **versão do produto:** evolução funcional ou técnica do produto;
- **versão da documentação:** evolução de um documento específico;
- **versão de API:** evolução de contrato de interface;
- **versão do DPF:** versão da metodologia;
- **versão de Release:** identificação do pacote liberado.

## 26. Roadmap, Milestones e Sprints

Organização oficial:

```text
dpf/
├── ROADMAP.md
├── MILESTONES.md              # recomendado
└── CURRENT-SPRINT.md          # opcional
```

Regras:

- `ROADMAP.md` é permanente;
- `MILESTONES.md` é RECOMENDADO quando houver dependências, fases ou marcos relevantes;
- `CURRENT-SPRINT.md` é OPCIONAL e só existe quando o projeto usa Sprint;
- Sprint NÃO é obrigatória para conformidade com o DPF;
- fluxo contínuo DEVE usar `PLANNED.md`, `PROJECT-STATE.md` e `RELEASES.md` como substitutos operacionais suficientes.

## 27. Riscos e dívida técnica

Estrutura oficial:

```text
dpf/validation/
├── RISKS.md
├── TECH-DEBT.md
├── risks/
└── debt/
```

Política:

- `RISKS.md` e `TECH-DEBT.md` DEVE existir como catálogos;
- registros individuais são RECOMENDADOS para itens severos, transversais ou duradouros;
- itens resolvidos NÃO DEVEM ser apagados;
- itens resolvidos DEVE mudar de estado e permanecer históricos.

## 28. Change Log e histórico

Diferenças oficiais:

- `git history`: histórico técnico de commits; NÃO substitui Change Log nem histórico documental.
- `CHANGELOG.md`: mudanças relevantes do produto ao longo de versões e releases.
- histórico do documento: mudanças naquele artefato específico.
- histórico da Feature: evolução da Feature, não do produto inteiro.
- histórico de decisão: substituições, aprovações, rejeições e efeitos da ADR.
- release notes: comunicação específica de uma release.

Armazenamento:

- histórico do documento DEVE existir no próprio artefato ou em arquivo adjacente;
- `CHANGELOG.md` DEVE ficar em `dpf/`;
- release notes DEVE ficar em `dpf/releases/notes/` ou no registro da release.

## 29. Arquivamento

Política oficial:

- artefatos vigentes NÃO DEVEM mudar de caminho sem necessidade real;
- itens concluídos ou cancelados PODEM permanecer no caminho canônico com estado atualizado;
- `archive/` DEVE ser usado para itens históricos que deixaram de compor o contexto operacional padrão;
- antes de mover, o projeto DEVE atualizar índices e referências;
- um item arquivado DEVE apontar para sua origem e motivo;
- links quebrados NÃO SÃO aceitáveis.

Regra prática:

- Capabilities, Epics, Features e ADRs DEVERIAM permanecer em caminhos canônicos sempre que possível;
- sprints antigas, evidências antigas, snapshots e relatórios temporais são candidatos naturais a `archive/`.

## 30. Índices e navegação

Índices obrigatórios:

- `README.md` na raiz;
- `dpf/PROJECT.md`;
- `dpf/PROJECT-STATE.md`;
- `dpf/decisions/DECISIONS.md`;
- `dpf/releases/RELEASES.md` e ou `dpf/RELEASES.md`;
- `dpf/capabilities/<cap>/EPICS.md`;
- `dpf/capabilities/<cap>/epics/<epic>/FEATURES.md`;
- `dpf/capabilities/<...>/FEATURE/TASKS.md`.

Regras:

- índices DEVE apontar para fontes primárias;
- índices NÃO DEVEM duplicar integralmente documentos subordinados;
- links relativos DEVE ser preferidos;
- links bidirecionais são RECOMENDADOS para Feature, Task, Rule, ADR e Release.

Documento inicial recomendado por perfil de agente:

- Architect Agent: `PROJECT-STATE.md`, `SYSTEM-DESIGN.md`, `DECISIONS.md`.
- Business Analyst Agent: `PROJECT.md`, `PRODUCT-VISION.md`, `BUSINESS-RULES.md`, `USE-CASES.md`.
- Backend Agent: `PROJECT-STATE.md`, `FEATURE.md`, `TASKS.md`, `API.md`, `DATABASE.md`, ADRs relacionadas.
- Frontend Agent: `PROJECT-STATE.md`, `FEATURE.md`, `WORKFLOW.md`, `USE-CASES.md`, regras e estados.
- Mobile Agent: equivalente ao Frontend Agent com contexto adicional de integrações e estados.
- DevOps Agent: `PROJECT-STATE.md`, `RELEASES.md`, riscos, validação, arquitetura operacional.
- QA Agent: `FEATURE.md`, `TASKS.md`, `TESTS.md`, regras, releases, evidências.
- Security Agent: `SYSTEM-DESIGN.md`, ADRs, riscos, Features críticas, evidências.
- Database Agent: `DATABASE.md`, `SYSTEM-DESIGN.md`, regras, Features e Tasks afetadas.
- Documentation Agent: `PROJECT-STATE.md` e qualquer artefato alterado pela mudança.

## 31. Manifesto do projeto

O DPF ADOTA um manifesto estrutural opcional, porém RECOMENDADO:

```text
dpf/dpf-project.yaml
```

Finalidade:

- identificar formalmente o projeto como projeto DPF;
- registrar versão do DPF adotada;
- declarar diretórios canônicos;
- expor convenções estruturais para futura automação.

Conteúdo conceitual mínimo:

- ID do Projeto;
- nome;
- versão do DPF;
- perfil de porte;
- caminho do `PROJECT-STATE.md`;
- caminho das Capabilities;
- política de IDs;
- recursos habilitados;
- responsáveis documentais.

O manifesto NÃO DEVE duplicar conteúdo detalhado já pertencente a `PROJECT.md`.

## 32. Perfis por porte

### 32.1 Projeto pequeno

Obrigatório:

- `AGENTS.md`
- `README.md`
- `dpf/PROJECT.md`
- `dpf/PROJECT-STATE.md`
- `dpf/PLANNED.md`
- `dpf/IMPLEMENTED.md`
- ao menos uma Capability, Epic e Feature documentadas
- `TASKS.md` por Feature

Simplificações permitidas:

- sem diretórios técnicos adicionais;
- sem arquivos individuais para Tasks triviais;
- Use Cases e Workflows apenas quando necessários.

### 32.2 Projeto médio

Além do essencial, DEVERIA possuir:

- `ROADMAP.md`
- `RELEASES.md`
- `DECISIONS.md`
- `SYSTEM-DESIGN.md`
- `BUSINESS-RULES.md`
- `TESTS.md`
- registros individuais para Tasks relevantes.

### 32.3 Projeto grande ou crítico

Além do médio, tornam-se OBRIGATÓRIOS:

- `MILESTONES.md`
- catálogo formal de riscos e dívida técnica;
- ADRs individuais para decisões relevantes;
- evidências formais de validação;
- regras e casos de uso estruturados por domínio;
- arquivos individuais de Task para trabalho relevante;
- políticas explícitas de arquivamento e conformidade.

Evolução:

- um projeto DEVE poder migrar de pequeno para médio ou grande sem quebrar IDs, caminhos canônicos ou fontes primárias.

## 33. Adoção em projetos legados

A adoção em legado DEVE ser progressiva.

Sequência mínima recomendada:

1. criar `dpf/PROJECT.md`;
2. criar `dpf/PROJECT-STATE.md` com visão honesta do estado atual;
3. registrar arquitetura vigente em `SYSTEM-DESIGN.md`;
4. registrar regras críticas em `BUSINESS-RULES.md`;
5. documentar Capabilities, Epics e Features em manutenção;
6. registrar decisões vigentes e dívidas relevantes;
7. exigir documentação proporcional a cada nova mudança.

Um projeto legado NÃO DEVE ser bloqueado até que todo o passado seja reconstruído.

## 34. Critérios de conformidade

Categorias de verificação:

- **Conformidade obrigatória**
- **Conformidade recomendada**
- **Alerta**
- **Inconsistência**
- **Erro crítico**

Exemplos de validação futura:

- presença de `dpf/PROJECT.md`;
- presença de `dpf/PROJECT-STATE.md`;
- presença da hierarquia mínima;
- metadados mínimos válidos;
- estados permitidos;
- referências internas válidas;
- inexistência de artefatos arquivados como vigentes;
- rastreabilidade mínima entre Feature, Task, teste e release;
- ausência de links quebrados em índices obrigatórios.

## 35. Regras de consistência

Regras mínimas:

1. uma Task DEVE apontar para uma Feature;
2. uma Feature DEVE apontar para uma Epic;
3. uma Epic DEVE apontar para uma Capability;
4. uma Capability DEVE apontar para o Projeto;
5. Feature com regra DEVE referenciar `BR-*`;
6. Use Case e Workflow relacionados DEVE informar a Feature ou regra associada;
7. mudança arquitetural DEVE referenciar `ADR-*`;
8. Task concluída DEVE possuir evidência proporcional;
9. Feature implementada DEVE possuir Tasks concluídas ou justificativa formal;
10. Release DEVE apontar para itens aprovados;
11. documento substituído DEVE apontar para o substituto;
12. item arquivado NÃO PODE aparecer como vigente;
13. `PROJECT-STATE.md` NÃO PODE contradizer a fonte primária;
14. `IMPLEMENTED.md` NÃO PODE listar item não validado como implementado sem ressalva explícita.

## 36. Matriz de artefatos

| Artefato | Finalidade | Localização | Cardinalidade | Obrigatoriedade | Responsável | Aprovador | Política de arquivamento |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PROJECT.md` | identidade e governança | `dpf/` | 1 | obrigatória | liderança | autoridade do projeto | manter canônico |
| `PROJECT-STATE.md` | estado resumido | `dpf/` | 1 | obrigatória | documentação ou liderança | humano responsável | manter canônico |
| Capability | capacidade duradoura | `dpf/capabilities/` | 1..n | obrigatória quando existir escopo formal | liderança de produto | patrocinador ou liderança | preferir canônico |
| Epic | agrupamento de Features | dentro da Capability | 1..n | obrigatória quando houver decomposição | product owner | liderança | preferir canônico |
| Feature | unidade funcional | dentro da Epic | 1..n | obrigatória | responsável funcional | humano responsável | preferir canônico |
| Task | unidade de execução | `TASKS.md` e opcionalmente `tasks/` | 1..n | obrigatória | executor designado | responsável da Feature | histórico permanente |
| `BUSINESS-RULES.md` | catálogo de regras | `dpf/product/business-rules/` | 1 | recomendada a obrigatória conforme risco | negócio | autoridade de negócio | manter catálogo |
| ADR | decisão arquitetural | `dpf/decisions/` | 0..n | recomendada a obrigatória conforme impacto | arquitetura | humano responsável | nunca apagar |
| Release | pacote liberado | `dpf/releases/` | 0..n | recomendada a obrigatória conforme maturidade | release manager | autorizador de liberação | histórico permanente |
| `RISKS.md` | riscos do projeto | `dpf/validation/` | 1 | recomendada a obrigatória conforme risco | liderança | autoridade competente | manter histórico |
| `TECH-DEBT.md` | dívida técnica | `dpf/validation/` | 1 | recomendada | engenharia | liderança técnica | manter histórico |

## 37. Matriz de rastreabilidade

| Origem | Destino | Relação | Obrigatoriedade |
| --- | --- | --- | --- |
| Capability | Projeto | pertence a | obrigatória |
| Epic | Capability | pertence a | obrigatória |
| Feature | Epic | pertence a | obrigatória |
| Task | Feature | executa parte de | obrigatória |
| Feature | Business Rule | obedece a | obrigatória quando houver regra |
| Feature | Use Case | implementa cenário | recomendada |
| Feature | Workflow | participa de fluxo | recomendada |
| Feature ou Task | ADR | segue decisão | obrigatória quando houver impacto arquitetural |
| Task | alteração técnica | produz | obrigatória |
| Task ou Feature | teste | validada por | obrigatória |
| Release | Feature/Task | inclui | obrigatória |
| Change Log | Release | resume | obrigatória |

## 38. Exemplos

### 38.1 Estrutura mínima de projeto pequeno

```text
agenda-lite/
├── AGENTS.md
├── README.md
├── dpf/
│   ├── PROJECT.md
│   ├── PROJECT-STATE.md
│   ├── PLANNED.md
│   ├── IMPLEMENTED.md
│   └── capabilities/
│       └── CAP-CORE-0001-agendamento/
│           ├── CAPABILITY.md
│           ├── EPICS.md
│           └── epics/
│               └── EPC-CORE-0001-agenda-cliente/
│                   ├── EPIC.md
│                   ├── FEATURES.md
│                   └── features/
│                       └── FEAT-CORE-0001-consultar-horarios/
│                           ├── FEATURE.md
│                           └── TASKS.md
```

### 38.2 Estrutura recomendada de projeto médio

```text
agenda-pro/
├── AGENTS.md
├── README.md
├── dpf/
│   ├── PROJECT.md
│   ├── PROJECT-STATE.md
│   ├── ROADMAP.md
│   ├── RELEASES.md
│   ├── CHANGELOG.md
│   ├── dpf-project.yaml
│   ├── capabilities/
│   ├── product/
│   ├── architecture/
│   ├── decisions/
│   ├── releases/
│   └── validation/
├── src/
└── tests/
```

### 38.3 Estrutura expandida de projeto grande

```text
plataforma-corporativa/
├── AGENTS.md
├── README.md
├── dpf/
│   ├── PROJECT.md
│   ├── PROJECT-STATE.md
│   ├── ROADMAP.md
│   ├── MILESTONES.md
│   ├── RELEASES.md
│   ├── CHANGELOG.md
│   ├── CURRENT-SPRINT.md
│   ├── dpf-project.yaml
│   ├── capabilities/
│   ├── product/
│   ├── architecture/
│   ├── decisions/
│   ├── releases/
│   ├── validation/
│   ├── context/
│   └── archive/
├── src/
├── tests/
├── infra/
└── scripts/
```

### 38.4 Capability com Epics

```text
CAP-CARE-0002-atendimento-digital/
├── CAPABILITY.md
├── EPICS.md
└── epics/
    ├── EPC-CARE-0007-agendamento/
    └── EPC-CARE-0008-confirmacao/
```

### 38.5 Epic com Features

```text
EPC-CARE-0007-agendamento/
├── EPIC.md
├── FEATURES.md
└── features/
    ├── FEAT-CARE-0014-consultar-horarios/
    ├── FEAT-CARE-0015-reservar-horario/
    └── FEAT-CARE-0016-cancelar-reserva/
```

### 38.6 Feature com Tasks

```text
FEAT-CARE-0014-consultar-horarios/
├── FEATURE.md
├── TASKS.md
├── tasks/
│   ├── TASK-CARE-0042-definir-filtro-de-disponibilidade.md
│   └── TASK-CARE-0043-validar-cenarios-de-consulta.md
├── validation/
└── evidence/
```

### 38.7 Architecture Decision

```text
dpf/decisions/ADR-CORE-0011-versionamento-de-contratos.md
```

### 38.8 Release

```text
dpf/releases/REL-CORE-0004-agendamento-publico.md
```

### 38.9 Project State

```text
dpf/PROJECT-STATE.md
```

Seções mínimas recomendadas:

- visão geral;
- release atual;
- foco da semana;
- Capabilities e Epics ativas;
- Features em andamento;
- Tasks bloqueadas;
- decisões recentes;
- riscos e dívida;
- próximos passos;
- leitura obrigatória para agentes.

### 38.10 Artefato cancelado ou substituído

Exemplo:

```text
status: canceled
superseded_by: FEAT-CARE-0021
```

### 38.11 Fluxo de arquivamento

```text
ativo -> concluido -> historico -> archived
```

Com atualização de índices antes da movimentação.

### 38.12 Relação entre regra, caso de uso, feature, task, teste e release

```text
BR-CARE-0003
  -> UC-CARE-0007
    -> FEAT-CARE-0014
      -> TASK-CARE-0042
        -> TEST-CARE-0104
          -> REL-CARE-0004
```

## 39. Árvore oficial de referência

```text
projeto/
├── AGENTS.md
├── README.md
├── dpf/
│   ├── PROJECT.md
│   ├── PROJECT-STATE.md
│   ├── ROADMAP.md
│   ├── MILESTONES.md
│   ├── RELEASES.md
│   ├── CHANGELOG.md
│   ├── PLANNED.md
│   ├── IMPLEMENTED.md
│   ├── CURRENT-SPRINT.md
│   ├── dpf-project.yaml
│   ├── capabilities/
│   │   └── CAP-CORE-0001-plataforma/
│   │       ├── CAPABILITY.md
│   │       ├── EPICS.md
│   │       ├── epics/
│   │       │   └── EPC-CORE-0001-gestao-de-agenda/
│   │       │       ├── EPIC.md
│   │       │       ├── FEATURES.md
│   │       │       └── features/
│   │       │           └── FEAT-CORE-0001-consultar-horarios/
│   │       │               ├── FEATURE.md
│   │       │               ├── TASKS.md
│   │       │               ├── tasks/
│   │       │               ├── validation/
│   │       │               └── evidence/
│   │       └── archive/
│   ├── product/
│   │   ├── PRODUCT-VISION.md
│   │   ├── business-rules/
│   │   ├── use-cases/
│   │   ├── workflows/
│   │   └── BUSINESS-GLOSSARY.md
│   ├── architecture/
│   │   ├── SYSTEM-DESIGN.md
│   │   ├── api/
│   │   ├── data/
│   │   ├── security/
│   │   └── infrastructure/
│   ├── decisions/
│   │   ├── DECISIONS.md
│   │   └── ADR-CORE-0001-....md
│   ├── releases/
│   │   ├── RELEASES.md
│   │   ├── REL-CORE-0001-....md
│   │   └── notes/
│   ├── validation/
│   │   ├── TESTS.md
│   │   ├── RISKS.md
│   │   ├── TECH-DEBT.md
│   │   ├── reviews/
│   │   ├── reports/
│   │   └── evidence/
│   ├── context/
│   └── archive/
├── src/
├── tests/
├── infra/
├── scripts/
└── assets/
```

Explicação:

- `dpf/` concentra o contrato metodológico;
- `capabilities/` materializa a hierarquia principal;
- `product/`, `architecture/`, `decisions/`, `releases/` e `validation/` guardam artefatos transversais;
- implementação e operação continuam fora de `dpf/`, mas relacionadas a ele por referência documental.

## 40. Princípios constitucionais da estrutura

Os princípios constitucionais da estrutura DPF são:

1. `dpf/` é o diretório oficial do framework no projeto.
2. A hierarquia oficial DEVE ser representada fisicamente.
3. A estrutura DEVE funcionar sem código.
4. Artefatos globais e hierárquicos NÃO DEVEM ser confundidos.
5. IDs são estáveis, imutáveis e não reutilizáveis.
6. Estados ficam nos metadados, não nos nomes.
7. Índices apontam para fontes primárias; não as substituem.
8. Arquivamento preserva rastreabilidade.
9. Automação futura DEVE consumir a estrutura sem exigir ferramentas proprietárias.
10. Nenhum agente pode usar a estrutura como justificativa para alterar a metodologia.

## 41. Conclusão

Com esta especificação, o DPF passa a possuir uma planta oficial de organização de projetos.

A Fase 1 definiu os conceitos, princípios e regras normativas.

A Fase 2 definiu os templates oficiais.

A Fase 3 define onde cada artefato existe, como é identificado, como se relaciona, como evolui e como permanece auditável ao longo do ciclo de vida do projeto.

Toda fase futura do DPF DEVE tratar esta estrutura como contrato oficial.
