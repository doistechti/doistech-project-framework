# DPF Templates Specification v1.0

**Status:** Oficial  
**Framework:** DoisTech Project Framework (DPF)  
**Versão:** 1.0  
**Data:** 2026-08-04  
**Classificação:** Especificação normativa da biblioteca de templates

> Este documento transforma a DPF Specification v1.0 em uma biblioteca normativa de templates. Não altera a metodologia, seus princípios ou a hierarquia Projeto > Capability > Epic > Feature > Task.

## 1. Objetivo e escopo

Esta especificação define o conteúdo, a governança, o ciclo de vida, as relações e as regras de consumo por agentes de IA de todos os templates oficiais do DPF. Ela é independente de linguagem, framework, infraestrutura, arquitetura ou fornecedor.

### 1.1 Fora de escopo

Não fazem parte desta fase: código, CLI, dashboard, plugins, agentes executáveis, estrutura física definitiva de diretórios ou exemplos de projetos.

## 2. Fundamentos normativos

- **Specification First**
- **Documentation as Source of Truth**
- **Context Driven Development**
- **AI Native**
- **Modularidade**
- **Evolução Incremental**

### 2.1 Hierarquia oficial

`Projeto > Capability > Epic > Feature > Task`

Cada nível deve possuir identidade própria, rastreabilidade ascendente e descendente e estado verificável. Task entrega parte de uma Feature; Feature realiza parte de uma Epic; Epic contribui para uma Capability; Capability expressa uma capacidade duradoura do Projeto.

### 2.2 Palavras normativas

- **DEVE / OBRIGATÓRIO:** requisito incontornável.
- **NÃO DEVE / PROIBIDO:** prática vedada.
- **DEVERIA / RECOMENDADO:** prática esperada, salvo justificativa registrada.
- **PODE / OPCIONAL:** escolha permitida.

## 3. Padrões globais de escrita

### 3.1 Títulos

- Título H1: nome oficial do artefato ou instância.
- H2: seções normativas principais.
- H3: subseções.
- Não saltar níveis.
- Títulos devem ser substantivos, objetivos e sem pontuação final.

### 3.2 IDs

Formato geral: `<TIPO>-<CONTEXTO>-<NNNN>`. Tipos mínimos: `PRJ`, `CAP`, `EPC`, `FEAT`, `TASK`, `BR`, `REQ`, `AC`, `ADR`, `RISK`, `ISSUE`, `DEBT`, `REL`, `MILE`. IDs são imutáveis, únicos no projeto, não reutilizáveis e não carregam estado.

### 3.3 Nomenclatura

Usar nomes estáveis, linguagem do domínio e singular para conceitos unitários. Abreviações devem existir no glossário. Nomes técnicos não substituem termos de negócio.

### 3.4 Tabelas

Toda tabela deve possuir cabeçalho, uma finalidade única, colunas estáveis e IDs nas linhas quando houver itens rastreáveis. Células vazias devem usar `N/A`, `Não definido` ou justificativa equivalente.

### 3.5 Diagramas e fluxos

Diagramas devem possuir título, objetivo, legenda, fronteiras, direção de leitura e versão textual equivalente. Fluxos devem identificar início, fim, participantes, decisões, exceções e resultados. O diagrama complementa, mas não substitui, a especificação textual.

### 3.6 Exemplos

Exemplos devem ser marcados como `Exemplo não normativo`, usar dados fictícios e nunca introduzir regra ausente na parte normativa.

### 3.7 Requisitos

Formato recomendado: `REQ-<CONTEXTO>-NNNN — O sistema DEVE <comportamento observável> <condição/limite>`. Cada requisito deve ter origem, prioridade, critérios de aceite e relações.

### 3.8 Regras de negócio

Formato: `BR-<CONTEXTO>-NNNN — <nome>`. Deve conter declaração normativa, condição, resultado, exceções, fonte, vigência e rastreabilidade. Não deve conter detalhes de implementação.

### 3.9 Critérios de aceite

Formato preferencial: `Dado / Quando / Então`, complementado por limites mensuráveis. Cada critério recebe ID `AC-<CONTEXTO>-NNNN` e deve ser verificável.

### 3.10 Metadados mínimos

Todo documento deve declarar: ID, título, status, versão, responsável, aprovador, data de criação, última atualização e documentos relacionados.

## 4. Regras transversais dos templates

- Cada informação normativa deve possuir uma única fonte primária. Outros documentos referenciam, não copiam.
- Mudanças relevantes devem atualizar histórico e documentos dependentes.
- Conteúdo desconhecido deve ser marcado; não pode ser inventado.
- Informações temporárias devem indicar validade.
- Documentos substituídos devem apontar para o sucessor.
- Agentes de IA não podem alterar escopo, regra, decisão ou aceite sem autorização e registro.
- Duplicidades de nomes são resolvidas pelo contexto documental, nunca por fusão implícita.

## 5. Catálogo normativo de templates


## 5.1 Governança

### `PROJECT.md`

**Objetivo.** Estabelecer a identidade, os limites, a governança e o ponto de entrada documental do projeto.

**Responsáveis.**
- Cria: Líder do projeto ou Product Owner.
- Altera: Liderança designada e mantenedores.
- Aprova: Patrocinador ou autoridade de governança.
- Consulta: Toda a equipe e agentes autorizados.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Resumo executivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Visão e objetivos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Fora de escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Stakeholders** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Governança** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Hierarquia DPF** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Princípios e restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Mapa documental** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Estado atual** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Riscos principais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para estabelecer a identidade, os limites, a governança e o ponto de entrada documental do projeto.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Governança.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `ROADMAP.md`

**Objetivo.** Registrar a direção temporal do produto e a sequência planejada de resultados, sem substituir o planejamento detalhado.

**Responsáveis.**
- Cria: Líder do projeto ou Product Owner.
- Altera: Liderança designada e mantenedores.
- Aprova: Patrocinador ou autoridade de governança.
- Consulta: Toda a equipe e agentes autorizados.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Horizonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Temas estratégicos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Resultados planejados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Sequenciamento** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Hipóteses** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Critérios de revisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar a direção temporal do produto e a sequência planejada de resultados, sem substituir o planejamento detalhado.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Governança.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `MILESTONES.md`

**Objetivo.** Definir marcos verificáveis que agrupam entregas e evidenciam avanço relevante.

**Responsáveis.**
- Cria: Líder do projeto ou Product Owner.
- Altera: Liderança designada e mantenedores.
- Aprova: Patrocinador ou autoridade de governança.
- Consulta: Toda a equipe e agentes autorizados.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Marcos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Critérios de conclusão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Entregas associadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Status** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir marcos verificáveis que agrupam entregas e evidenciam avanço relevante.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Governança.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `RELEASES.md`

**Objetivo.** Planejar, registrar e auditar versões liberadas ou candidatas à liberação.

**Responsáveis.**
- Cria: Líder do projeto ou Product Owner.
- Altera: Liderança designada e mantenedores.
- Aprova: Patrocinador ou autoridade de governança.
- Consulta: Toda a equipe e agentes autorizados.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Política de releases** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Calendário** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Conteúdo por release** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Critérios de entrada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Critérios de saída** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Plano de rollback** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Aprovações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para planejar, registrar e auditar versões liberadas ou candidatas à liberação.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Governança.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `PROJECT-STATUS.md`

**Objetivo.** Oferecer uma visão executiva, atual e verificável da saúde do projeto.

**Responsáveis.**
- Cria: Líder do projeto ou Product Owner.
- Altera: Liderança designada e mantenedores.
- Aprova: Patrocinador ou autoridade de governança.
- Consulta: Toda a equipe e agentes autorizados.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Resumo executivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Semáforo geral** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Progresso por nível** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Entregas recentes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Próximos passos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Bloqueios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Decisões pendentes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Métricas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para oferecer uma visão executiva, atual e verificável da saúde do projeto.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Governança.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.2 Produto

### `PRODUCT-VISION.md`

**Objetivo.** Explicar o problema, o público, a proposta de valor e a direção do produto.

**Responsáveis.**
- Cria: Product Owner ou responsável de produto.
- Altera: Produto, negócio e analistas autorizados.
- Aprova: Product Owner e stakeholders designados.
- Consulta: Equipe, arquitetura, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Problema** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Público-alvo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Proposta de valor** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Visão futura** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Diferenciais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Princípios do produto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Hipóteses** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para explicar o problema, o público, a proposta de valor e a direção do produto.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Produto.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `OBJECTIVES.md`

**Objetivo.** Converter a visão em objetivos mensuráveis e priorizados.

**Responsáveis.**
- Cria: Product Owner ou responsável de produto.
- Altera: Produto, negócio e analistas autorizados.
- Aprova: Product Owner e stakeholders designados.
- Consulta: Equipe, arquitetura, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Objetivos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Resultados-chave** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Prioridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Prazo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Medição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Status** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para converter a visão em objetivos mensuráveis e priorizados.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Produto.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `PERSONAS.md`

**Objetivo.** Representar grupos de usuários e atores relevantes com necessidades, contextos e limitações.

**Responsáveis.**
- Cria: Product Owner ou responsável de produto.
- Altera: Produto, negócio e analistas autorizados.
- Aprova: Product Owner e stakeholders designados.
- Consulta: Equipe, arquitetura, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Persona** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Contexto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Objetivos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Necessidades** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Dores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Comportamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Limitações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Jornada relacionada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para representar grupos de usuários e atores relevantes com necessidades, contextos e limitações.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Produto.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `SUCCESS-METRICS.md`

**Objetivo.** Definir como sucesso, adoção, qualidade e impacto serão medidos.

**Responsáveis.**
- Cria: Product Owner ou responsável de produto.
- Altera: Produto, negócio e analistas autorizados.
- Aprova: Product Owner e stakeholders designados.
- Consulta: Equipe, arquitetura, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Modelo de medição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Métricas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Fórmula** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Fonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Linha de base** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Meta** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Periodicidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Limitações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir como sucesso, adoção, qualidade e impacto serão medidos.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Produto.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `OUT-OF-SCOPE.md`

**Objetivo.** Tornar explícito o que não pertence ao escopo atual e evitar expansão indevida.

**Responsáveis.**
- Cria: Product Owner ou responsável de produto.
- Altera: Produto, negócio e analistas autorizados.
- Aprova: Product Owner e stakeholders designados.
- Consulta: Equipe, arquitetura, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Itens excluídos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Justificativa** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Horizonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Condições de reavaliação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Impactos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para tornar explícito o que não pertence ao escopo atual e evitar expansão indevida.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Produto.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `RISKS.md`

**Objetivo.** Identificar, avaliar, tratar e acompanhar riscos do produto e do projeto.

**Responsáveis.**
- Cria: Product Owner ou responsável de produto.
- Altera: Produto, negócio e analistas autorizados.
- Aprova: Product Owner e stakeholders designados.
- Consulta: Equipe, arquitetura, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Escala** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Registro de riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Probabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Impacto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Exposição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Mitigação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Contingência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Gatilhos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Status** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para identificar, avaliar, tratar e acompanhar riscos do produto e do projeto.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Produto.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.3 Negócio

### `BUSINESS-RULES.md`

**Objetivo.** Centralizar regras de negócio normativas, rastreáveis e independentes da implementação.

**Responsáveis.**
- Cria: Analista de negócio ou especialista de domínio.
- Altera: Negócio e produto autorizados.
- Aprova: Responsável de negócio.
- Consulta: Produto, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Convenções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Catálogo de regras** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Condições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Ações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Exceções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Prioridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Fonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Validade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Rastreabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para centralizar regras de negócio normativas, rastreáveis e independentes da implementação.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Negócio.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `USE-CASES.md`

**Objetivo.** Descrever interações entre atores e o sistema para alcançar resultados de negócio.

**Responsáveis.**
- Cria: Analista de negócio ou especialista de domínio.
- Altera: Negócio e produto autorizados.
- Aprova: Responsável de negócio.
- Consulta: Produto, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Atores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Casos de uso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Gatilho** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Pré-condições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Fluxo principal** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Alternativas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Exceções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Pós-condições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Regras** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Critérios de sucesso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para descrever interações entre atores e o sistema para alcançar resultados de negócio.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Negócio.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `PROCESS-FLOWS.md`

**Objetivo.** Documentar fluxos ponta a ponta, decisões, exceções e responsabilidades.

**Responsáveis.**
- Cria: Analista de negócio ou especialista de domínio.
- Altera: Negócio e produto autorizados.
- Aprova: Responsável de negócio.
- Consulta: Produto, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Notação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Participantes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Entradas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Fluxos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Pontos de decisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Exceções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Saídas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **SLA** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Controles** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para documentar fluxos ponta a ponta, decisões, exceções e responsabilidades.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Negócio.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `BUSINESS-GLOSSARY.md`

**Objetivo.** Manter vocabulário oficial e reduzir ambiguidades semânticas.

**Responsáveis.**
- Cria: Analista de negócio ou especialista de domínio.
- Altera: Negócio e produto autorizados.
- Aprova: Responsável de negócio.
- Consulta: Produto, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Termos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Definição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Sinônimos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Termos proibidos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Contexto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Fonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para manter vocabulário oficial e reduzir ambiguidades semânticas.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Negócio.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `BUSINESS-DECISIONS.md`

**Objetivo.** Registrar decisões de negócio, justificativas, impactos e responsáveis.

**Responsáveis.**
- Cria: Analista de negócio ou especialista de domínio.
- Altera: Negócio e produto autorizados.
- Aprova: Responsável de negócio.
- Consulta: Produto, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: na inicialização do projeto.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Registro de decisões** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Contexto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Decisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Justificativa** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Impactos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Data de vigência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Revisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar decisões de negócio, justificativas, impactos e responsáveis.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Negócio.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.4 Arquitetura

### `SYSTEM-DESIGN.md`

**Objetivo.** Descrever o desenho técnico completo, restrições, qualidades e principais escolhas do sistema.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Contexto do sistema** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Requisitos arquiteturais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Visões arquiteturais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Fluxos críticos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Integrações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Segurança** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Qualidades** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Falhas e resiliência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Operação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Trade-offs** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para descrever o desenho técnico completo, restrições, qualidades e principais escolhas do sistema.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `DOMAIN-MODEL.md`

**Objetivo.** Representar conceitos, relações, invariantes e fronteiras do domínio.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Fronteiras** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Subdomínios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Entidades** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Objetos de valor** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Agregados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Serviços de domínio** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Eventos de domínio** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Invariantes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Glossário associado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para representar conceitos, relações, invariantes e fronteiras do domínio.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `COMPONENTS.md`

**Objetivo.** Catalogar componentes, responsabilidades, interfaces e dependências.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Mapa de componentes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Responsabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Interfaces** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Entradas e saídas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Estado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Dados possuídos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Falhas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Observabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para catalogar componentes, responsabilidades, interfaces e dependências.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `INTEGRATIONS.md`

**Objetivo.** Definir integrações externas e internas, contratos, responsabilidades e falhas esperadas.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Catálogo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Proprietários** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Contrato** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Autenticação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Fluxo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Disponibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Timeout e retry** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Idempotência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Falhas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **SLA** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir integrações externas e internas, contratos, responsabilidades e falhas esperadas.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `SECURITY.md`

**Objetivo.** Registrar requisitos, controles, ameaças, responsabilidades e decisões de segurança.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Modelo de ameaças** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Ativos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Identidade e acesso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Proteção de dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Segredos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Auditoria** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Vulnerabilidades** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Resposta a incidentes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Conformidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Riscos residuais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar requisitos, controles, ameaças, responsabilidades e decisões de segurança.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `ADR.md`

**Objetivo.** Formalizar uma decisão arquitetural individual e seu contexto.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Título** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Status** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Contexto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Problema de decisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Forças e restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Opções consideradas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Decisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Justificativa** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Consequências positivas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Consequências negativas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Plano de adoção** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Alternativas rejeitadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para formalizar uma decisão arquitetural individual e seu contexto.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `ARCHITECTURE-OVERVIEW.md`

**Objetivo.** Fornecer leitura rápida e navegável da arquitetura vigente.

**Responsáveis.**
- Cria: Arquiteto ou responsável técnico.
- Altera: Arquitetura e líderes técnicos.
- Aprova: Autoridade técnica definida.
- Consulta: Desenvolvimento, operações, segurança e agentes.

**Momento de utilização.**
- Criar: quando a arquitetura relevante começa a ser definida.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Contexto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Diagrama de contexto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Containers ou subsistemas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Fluxos principais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Integrações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Segurança** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Operação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Decisões principais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Links aprofundados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para fornecer leitura rápida e navegável da arquitetura vigente.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Arquitetura.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.5 Capability

### `CAPABILITY.md`

**Objetivo.** Definir uma capacidade de negócio duradoura que organiza epics relacionados.

**Responsáveis.**
- Cria: Product Owner ou arquiteto de produto.
- Altera: Responsável da capability.
- Aprova: Governança de produto.
- Consulta: Epics, features, equipe e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Capability.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Nome e definição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Resultado de negócio** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Fora de escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Atores e stakeholders** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Indicadores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Epics relacionadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Regras e restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Estado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Rastreabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir uma capacidade de negócio duradoura que organiza epics relacionados.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Capability.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.6 Epic

### `EPIC.md`

**Objetivo.** Agrupar features que realizam um resultado amplo e coerente.

**Responsáveis.**
- Cria: Product Owner.
- Altera: Produto e responsável da epic.
- Aprova: Product Owner.
- Consulta: Features, equipe e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Epic.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Resumo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Capability relacionada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Problema e resultado esperado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Fora de escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Features planejadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Métricas de sucesso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Critérios de conclusão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Estado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Rastreabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para agrupar features que realizam um resultado amplo e coerente.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Epic.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.7 Feature

### `FEATURE.md`

**Objetivo.** Especificar uma entrega funcional verificável, com valor, regras, contratos e aceite.

**Responsáveis.**
- Cria: Product Owner ou analista.
- Altera: Produto, negócio e responsáveis técnicos.
- Aprova: Product Owner e aprovadores aplicáveis.
- Consulta: Tasks, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Feature.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Resumo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Problema e valor** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Fora de escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Atores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Pré-condições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Fluxo principal** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Fluxos alternativos e exceções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Regras de negócio** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Requisitos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Critérios de aceite** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Impactos em API** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Impactos em dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Segurança e privacidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Testes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Plano de entrega** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Rastreabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
23. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
24. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para especificar uma entrega funcional verificável, com valor, regras, contratos e aceite.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Feature.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `API.md`

**Objetivo.** Descrever os impactos e contratos de api específicos de uma feature.

**Responsáveis.**
- Cria: Product Owner ou analista.
- Altera: Produto, negócio e responsáveis técnicos.
- Aprova: Product Owner e aprovadores aplicáveis.
- Consulta: Tasks, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Feature.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Operações afetadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Contratos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Entradas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Saídas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Erros** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Autorização** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Compatibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Exemplos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Testes de contrato** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para descrever os impactos e contratos de API específicos de uma feature.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Feature.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `DATABASE.md`

**Objetivo.** Documentar o modelo de dados aplicável ao seu contexto documental.

**Responsáveis.**
- Cria: Product Owner ou analista.
- Altera: Produto, negócio e responsáveis técnicos.
- Aprova: Product Owner e aprovadores aplicáveis.
- Consulta: Tasks, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Feature.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Contexto de dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Entidades ou estruturas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Campos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Índices** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Integridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Privacidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Migrações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Compatibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Rastreabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para documentar o modelo de dados aplicável ao seu contexto documental.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Feature.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `TESTS.md`

**Objetivo.** Definir os testes necessários para comprovar uma feature.

**Responsáveis.**
- Cria: Product Owner ou analista.
- Altera: Produto, negócio e responsáveis técnicos.
- Aprova: Product Owner e aprovadores aplicáveis.
- Consulta: Tasks, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Feature.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Objetivos de teste** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Cenários** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Níveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Dados de teste** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Automação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Critérios de passagem** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Cobertura** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Riscos residuais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir os testes necessários para comprovar uma feature.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Feature.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `CHANGELOG.md`

**Objetivo.** Registrar alterações relevantes no contexto em que o arquivo está localizado.

**Responsáveis.**
- Cria: Product Owner ou analista.
- Altera: Produto, negócio e responsáveis técnicos.
- Aprova: Product Owner e aprovadores aplicáveis.
- Consulta: Tasks, desenvolvimento, QA e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Feature.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Política de registro** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Alterações adicionadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Alterações modificadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Correções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Remoções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Deprecações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Impactos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar alterações relevantes no contexto em que o arquivo está localizado.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Feature.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.8 Task

### `TASK.md`

**Objetivo.** Definir uma unidade executável de trabalho vinculada a uma feature.

**Responsáveis.**
- Cria: Responsável pela execução.
- Altera: Executor e revisores autorizados.
- Aprova: Revisor ou líder definido.
- Consulta: Executores, revisores e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Task.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Resultado esperado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Feature relacionada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Pré-condições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Passos de execução** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Arquivos ou componentes afetados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Validações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Bloqueios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Definition of Ready** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Definition of Done** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir uma unidade executável de trabalho vinculada a uma feature.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Task.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `IMPLEMENTATION.md`

**Objetivo.** Registrar o plano e o resultado técnico da implementação de uma task.

**Responsáveis.**
- Cria: Responsável pela execução.
- Altera: Executor e revisores autorizados.
- Aprova: Revisor ou líder definido.
- Consulta: Executores, revisores e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Task.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Contexto técnico** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Plano** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Abordagem escolhida** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Componentes afetados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Mudanças realizadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Decisões locais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Validações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Desvios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Pendências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Rollback** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar o plano e o resultado técnico da implementação de uma task.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Task.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `CODE-REVIEW.md`

**Objetivo.** Documentar critérios, achados e conclusão da revisão de código de uma task.

**Responsáveis.**
- Cria: Responsável pela execução.
- Altera: Executor e revisores autorizados.
- Aprova: Revisor ou líder definido.
- Consulta: Executores, revisores e agentes.

**Momento de utilização.**
- Criar: antes de iniciar trabalho no nível Task.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Escopo da revisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Critérios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Revisores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Achados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Severidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Correções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Riscos aceitos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Aprovação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para documentar critérios, achados e conclusão da revisão de código de uma task.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Task.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.9 APIs

### `API-SPECIFICATION.md`

**Objetivo.** Manter o contrato global das apis expostas ou consumidas pelo sistema.

**Responsáveis.**
- Cria: Arquiteto de API ou responsável técnico.
- Altera: Times proprietários dos contratos.
- Aprova: Autoridade técnica.
- Consulta: Consumidores, implementadores, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a apis.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Princípios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Catálogo de APIs** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Recursos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Operações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Schemas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Erros** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Segurança** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Paginação e filtros** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Idempotência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Limites** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Exemplos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Compatibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para manter o contrato global das APIs expostas ou consumidas pelo sistema.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de APIs.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `ERRORS.md`

**Objetivo.** Padronizar erros, códigos, mensagens, causas e tratamento.

**Responsáveis.**
- Cria: Arquiteto de API ou responsável técnico.
- Altera: Times proprietários dos contratos.
- Aprova: Autoridade técnica.
- Consulta: Consumidores, implementadores, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a apis.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Modelo de erro** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Catálogo de códigos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Semântica HTTP ou protocolo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Mensagens** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Detalhes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Correlação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Retentativa** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Exposição segura** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Observabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para padronizar erros, códigos, mensagens, causas e tratamento.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de APIs.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `EVENTS.md`

**Objetivo.** Definir eventos, semântica, payloads, produtores, consumidores e garantias.

**Responsáveis.**
- Cria: Arquiteto de API ou responsável técnico.
- Altera: Times proprietários dos contratos.
- Aprova: Autoridade técnica.
- Consulta: Consumidores, implementadores, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a apis.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Convenções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Catálogo de eventos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Envelope** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Payload** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Produtor** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Consumidores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Ordenação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Entrega** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Idempotência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Retenção** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Evolução** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Erros** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir eventos, semântica, payloads, produtores, consumidores e garantias.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de APIs.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `WEBHOOKS.md`

**Objetivo.** Definir callbacks http, segurança, entrega, repetição e observabilidade.

**Responsáveis.**
- Cria: Arquiteto de API ou responsável técnico.
- Altera: Times proprietários dos contratos.
- Aprova: Autoridade técnica.
- Consulta: Consumidores, implementadores, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a apis.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Catálogo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Endpoint receptor** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Eventos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Payload** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Assinatura** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Entrega** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Retry** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Idempotência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Timeout** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Resposta esperada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Desativação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir callbacks HTTP, segurança, entrega, repetição e observabilidade.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de APIs.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `AUTHENTICATION.md`

**Objetivo.** Definir mecanismos e fluxos de autenticação e gestão de identidade.

**Responsáveis.**
- Cria: Arquiteto de API ou responsável técnico.
- Altera: Times proprietários dos contratos.
- Aprova: Autoridade técnica.
- Consulta: Consumidores, implementadores, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a apis.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Atores** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Mecanismos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Fluxos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Credenciais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Sessões ou tokens** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Expiração** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Revogação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Recuperação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **MFA** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Erros** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Auditoria** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir mecanismos e fluxos de autenticação e gestão de identidade.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de APIs.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `VERSIONING.md`

**Objetivo.** Estabelecer política de versão, compatibilidade, depreciação e evolução de contratos.

**Responsáveis.**
- Cria: Arquiteto de API ou responsável técnico.
- Altera: Times proprietários dos contratos.
- Aprova: Autoridade técnica.
- Consulta: Consumidores, implementadores, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a apis.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Objetos versionados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Esquema de versão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Compatibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Mudanças incompatíveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Depreciação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Migração** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Comunicação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Suporte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para estabelecer política de versão, compatibilidade, depreciação e evolução de contratos.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de APIs.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.10 Banco

### `DATABASE.md`

**Objetivo.** Documentar o modelo de dados aplicável ao seu contexto documental.

**Responsáveis.**
- Cria: Responsável por dados.
- Altera: Engenharia de dados e times proprietários.
- Aprova: Autoridade técnica de dados.
- Consulta: Desenvolvimento, operações, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a banco.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Contexto de dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Entidades ou estruturas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Campos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Índices** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Integridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Privacidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Migrações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Compatibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Rastreabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para documentar o modelo de dados aplicável ao seu contexto documental.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Banco.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `MIGRATIONS.md`

**Objetivo.** Planejar e registrar mudanças de esquema ou dados com execução e reversão controladas.

**Responsáveis.**
- Cria: Responsável por dados.
- Altera: Engenharia de dados e times proprietários.
- Aprova: Autoridade técnica de dados.
- Consulta: Desenvolvimento, operações, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a banco.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Pré-condições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Mudanças** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Transformação de dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Ordem** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Validação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Rollback** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Janela** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para planejar e registrar mudanças de esquema ou dados com execução e reversão controladas.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Banco.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `NAMING-CONVENTIONS.md`

**Objetivo.** Padronizar nomes de artefatos de dados e reduzir inconsistências.

**Responsáveis.**
- Cria: Responsável por dados.
- Altera: Engenharia de dados e times proprietários.
- Aprova: Autoridade técnica de dados.
- Consulta: Desenvolvimento, operações, QA e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a banco.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Princípios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Entidades** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Tabelas ou coleções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Campos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Chaves** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Índices** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Restrições** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Migrações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Objetos auxiliares** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Exceções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para padronizar nomes de artefatos de dados e reduzir inconsistências.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Banco.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.11 Testes

### `TEST-PLAN.md`

**Objetivo.** Planejar o esforço de teste de um projeto, release ou marco.

**Responsáveis.**
- Cria: Responsável de qualidade.
- Altera: QA, produto e técnicos autorizados.
- Aprova: Liderança de qualidade ou produto.
- Consulta: Equipe e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a testes.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Objeto do teste** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Fora de escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Itens de teste** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Abordagem** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Ambientes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Cronograma** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Critérios de entrada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Critérios de saída** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Relatórios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
22. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
23. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para planejar o esforço de teste de um projeto, release ou marco.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Testes.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `TEST-STRATEGY.md`

**Objetivo.** Definir princípios, níveis, técnicas, responsabilidades e automação de testes.

**Responsáveis.**
- Cria: Responsável de qualidade.
- Altera: QA, produto e técnicos autorizados.
- Aprova: Liderança de qualidade ou produto.
- Consulta: Equipe e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a testes.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Princípios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Pirâmide ou distribuição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Níveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Técnicas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Automação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Dados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Ambientes** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Não funcionais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Gestão de defeitos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Métricas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Governança** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir princípios, níveis, técnicas, responsabilidades e automação de testes.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Testes.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `ACCEPTANCE-CRITERIA.md`

**Objetivo.** Padronizar critérios observáveis que determinam aceitação.

**Responsáveis.**
- Cria: Responsável de qualidade.
- Altera: QA, produto e técnicos autorizados.
- Aprova: Liderança de qualidade ou produto.
- Consulta: Equipe e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a testes.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Convenções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Critérios funcionais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Critérios não funcionais** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Cenários** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Responsável pela aceitação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Exceções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para padronizar critérios observáveis que determinam aceitação.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Testes.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.12 Deploy

### `DEPLOYMENT.md`

**Objetivo.** Definir procedimento de entrega, promoção, rollback e validação.

**Responsáveis.**
- Cria: Responsável de plataforma ou operações.
- Altera: Operações e times proprietários.
- Aprova: Autoridade de release/operação.
- Consulta: Desenvolvimento, suporte e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a deploy.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Pré-requisitos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Artefatos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Sequência** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Configuração** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Validação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Rollback** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Comunicação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir procedimento de entrega, promoção, rollback e validação.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Deploy.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `ENVIRONMENTS.md`

**Objetivo.** Documentar ambientes, finalidades, restrições, acessos e paridade.

**Responsáveis.**
- Cria: Responsável de plataforma ou operações.
- Altera: Operações e times proprietários.
- Aprova: Autoridade de release/operação.
- Consulta: Desenvolvimento, suporte e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a deploy.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Catálogo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Finalidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Proprietário** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Dados permitidos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Acessos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Configuração** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Paridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Disponibilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Retenção** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para documentar ambientes, finalidades, restrições, acessos e paridade.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Deploy.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `CI-CD.md`

**Objetivo.** Descrever o fluxo automatizado de integração, validação e entrega.

**Responsáveis.**
- Cria: Responsável de plataforma ou operações.
- Altera: Operações e times proprietários.
- Aprova: Autoridade de release/operação.
- Consulta: Desenvolvimento, suporte e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a deploy.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Objetivos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Gatilhos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Etapas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Qualidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Artefatos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Promoção** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Aprovações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Segredos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Rollback** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observabilidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para descrever o fluxo automatizado de integração, validação e entrega.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Deploy.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `MONITORING.md`

**Objetivo.** Definir sinais, métricas, alertas e respostas operacionais.

**Responsáveis.**
- Cria: Responsável de plataforma ou operações.
- Altera: Operações e times proprietários.
- Aprova: Autoridade de release/operação.
- Consulta: Desenvolvimento, suporte e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a deploy.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Serviços monitorados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **SLIs** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **SLOs** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Métricas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Alertas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Limiares** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Runbooks** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Escalonamento** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Revisão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir sinais, métricas, alertas e respostas operacionais.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Deploy.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `OBSERVABILITY.md`

**Objetivo.** Definir como logs, métricas, traces e contexto permitem compreender o sistema.

**Responsáveis.**
- Cria: Responsável de plataforma ou operações.
- Altera: Operações e times proprietários.
- Aprova: Autoridade de release/operação.
- Consulta: Desenvolvimento, suporte e agentes.

**Momento de utilização.**
- Criar: antes da primeira decisão ou entrega relacionada a deploy.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Princípios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Logs** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Métricas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Traces** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Correlação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Contexto de negócio** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Dashboards** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Retenção** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Acesso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Custos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Diagnóstico** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
21. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para definir como logs, métricas, traces e contexto permitem compreender o sistema.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Deploy.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.


## 5.13 Project State

### `CURRENT-SPRINT.md`

**Objetivo.** Representar o compromisso operacional do ciclo atual.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Identificação do ciclo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Itens comprometidos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Capacidade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Riscos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Bloqueios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Progresso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Mudanças** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Critério de encerramento** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para representar o compromisso operacional do ciclo atual.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `IMPLEMENTED.md`

**Objetivo.** Manter índice verificável do que está concluído e disponível.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Itens concluídos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Versão ou release** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Data** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Evidências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Documentação relacionada** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Restrições conhecidas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para manter índice verificável do que está concluído e disponível.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `IN-PROGRESS.md`

**Objetivo.** Manter índice do trabalho iniciado e ainda não concluído.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Itens em andamento** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Início** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Progresso** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Próximo passo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Bloqueios** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Previsão** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para manter índice do trabalho iniciado e ainda não concluído.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `PLANNED.md`

**Objetivo.** Manter índice priorizado do trabalho aprovado, mas ainda não iniciado.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Itens planejados** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Prioridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Justificativa** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Condição de início** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Horizonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para manter índice priorizado do trabalho aprovado, mas ainda não iniciado.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `KNOWN-ISSUES.md`

**Objetivo.** Registrar problemas conhecidos, impacto, contorno e plano de resolução.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Descrição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Impacto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Ambiente** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Reprodução** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Contorno** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Causa conhecida** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Plano** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Status** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar problemas conhecidos, impacto, contorno e plano de resolução.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `TECH-DEBT.md`

**Objetivo.** Registrar dívida técnica deliberada ou identificada, impacto e estratégia de pagamento.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Descrição** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Origem** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Impacto** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Risco** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Custo estimado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Estratégia** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Prioridade** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Critério de quitação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
19. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
20. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar dívida técnica deliberada ou identificada, impacto e estratégia de pagamento.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `DECISIONS.md`

**Objetivo.** Manter índice consolidado de decisões vigentes e seus documentos de origem.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Índice de decisões** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Tipo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Documento fonte** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Status** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Data** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Responsável** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Escopo afetado** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para manter índice consolidado de decisões vigentes e seus documentos de origem.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

### `CHANGELOG.md`

**Objetivo.** Registrar alterações relevantes no contexto em que o arquivo está localizado.

**Responsáveis.**
- Cria: Líder do ciclo ou mantenedor do estado.
- Altera: Responsáveis pelos itens e governança.
- Aprova: Liderança definida.
- Consulta: Toda a equipe e agentes.

**Momento de utilização.**
- Criar: quando houver o primeiro item a registrar no estado correspondente.
- Atualizar: sempre que uma decisão, escopo, estado, contrato, risco ou evidência nele representado mudar.
- Encerrar: não é apagado; torna-se histórico, arquivado ou substituído com indicação explícita de status e referência ao sucessor.

**Estrutura oficial.**

1. **Identificação** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
2. **Objetivo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
3. **Escopo** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
4. **Responsáveis** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
5. **Dependências** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
6. **Relacionamentos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
7. **Política de registro** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
8. **Alterações adicionadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
9. **Alterações modificadas** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
10. **Correções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
11. **Remoções** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
12. **Deprecações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
13. **Impactos** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
14. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
15. **Histórico de alterações** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
16. **Checklist** — Obrigatória. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
17. **Observações** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.
18. **Referências** — Opcional quando não houver conteúdo aplicável. Registra o conteúdo correspondente ao título com linguagem verificável e referências por ID.

**Regras específicas.**
- Pode conter somente informação necessária para registrar alterações relevantes no contexto em que o arquivo está localizado.
- Nunca deve conter credenciais, segredos, dados pessoais desnecessários, decisões sem responsável, estado não verificável ou conteúdo contraditório com a fonte primária.
- Deve usar IDs oficiais, links relativos ou referências estáveis e histórico de alteração.
- Não deve reproduzir integralmente conteúdo pertencente a outro documento; deve referenciá-lo.

**Relações.**
- Alimentado por documentos imediatamente superiores na hierarquia, decisões vigentes, fontes de negócio e evidências aplicáveis ao contexto de Project State.
- Alimenta documentos de níveis inferiores, estado do projeto, planejamento, implementação, testes, release e auditoria quando aplicável.

**Consumo por IA.**
- Ler antes de planejar, gerar ou revisar qualquer artefato que dependa do seu conteúdo.
- Atualizar apenas quando a tarefa autorizar mudança documental e houver evidência ou decisão rastreável.
- Ignorar somente quando estiver explicitamente fora do escopo da tarefa, substituído, arquivado ou marcado como não aplicável.
- Em conflito, interromper alteração automática, identificar as fontes conflitantes e priorizar a fonte normativa de nível superior ou a decisão mais recente formalmente aprovada.

## 6. Checklists oficiais

### 6.1 Criar Projeto

- [ ] Definir ID e nome do projeto
- [ ] Criar PROJECT.md
- [ ] Registrar visão, objetivos, escopo e fora de escopo
- [ ] Definir responsáveis e aprovadores
- [ ] Criar governança, produto, negócio e arquitetura mínimos
- [ ] Estabelecer mapa documental
- [ ] Inicializar Project State
- [ ] Registrar riscos iniciais
- [ ] Validar hierarquia e IDs
- [ ] Aprovar baseline documental

### 6.2 Criar Capability

- [ ] Confirmar vínculo com o projeto
- [ ] Atribuir ID CAP
- [ ] Definir resultado de negócio duradouro
- [ ] Delimitar escopo e fora de escopo
- [ ] Definir métricas
- [ ] Mapear stakeholders e dependências
- [ ] Registrar riscos
- [ ] Relacionar epics
- [ ] Validar ausência de solução técnica indevida
- [ ] Aprovar capability

### 6.3 Criar Epic

- [ ] Confirmar Capability pai
- [ ] Atribuir ID EPC
- [ ] Definir resultado amplo
- [ ] Delimitar escopo
- [ ] Identificar features iniciais
- [ ] Definir métricas e conclusão
- [ ] Registrar dependências e riscos
- [ ] Atualizar roadmap e estado
- [ ] Aprovar epic

### 6.4 Criar Feature

- [ ] Confirmar Epic pai
- [ ] Atribuir ID FEAT
- [ ] Definir problema, valor e escopo
- [ ] Vincular regras e requisitos
- [ ] Definir critérios de aceite
- [ ] Analisar API, dados, segurança e testes
- [ ] Registrar dependências e riscos
- [ ] Criar arquivos complementares aplicáveis
- [ ] Validar Definition of Ready
- [ ] Atualizar estado

### 6.5 Criar Task

- [ ] Confirmar Feature pai
- [ ] Atribuir ID TASK
- [ ] Definir resultado executável
- [ ] Delimitar escopo técnico
- [ ] Listar dependências e pré-condições
- [ ] Definir validações e evidências
- [ ] Verificar Definition of Ready
- [ ] Atribuir responsável
- [ ] Atualizar CURRENT-SPRINT ou PLANNED

### 6.6 Finalizar Release

- [ ] Confirmar conteúdo da release
- [ ] Validar critérios de saída
- [ ] Executar testes e registrar evidências
- [ ] Revisar segurança e migrações
- [ ] Validar deployment e rollback
- [ ] Atualizar RELEASES.md e CHANGELOG.md
- [ ] Atualizar IMPLEMENTED.md
- [ ] Registrar issues e dívidas residuais
- [ ] Obter aprovações
- [ ] Comunicar versão e impactos

### 6.7 Encerrar Sprint

- [ ] Reconciliar itens comprometidos
- [ ] Mover concluídos para IMPLEMENTED
- [ ] Manter incompletos em IN-PROGRESS ou replanejar
- [ ] Registrar bloqueios e desvios
- [ ] Atualizar métricas e status
- [ ] Registrar decisões
- [ ] Revisar dívida técnica
- [ ] Fechar CURRENT-SPRINT
- [ ] Criar baseline do próximo ciclo quando aprovado

### 6.8 Arquivar Projeto

- [ ] Confirmar decisão de encerramento
- [ ] Registrar status final
- [ ] Consolidar releases e entregas
- [ ] Encerrar ou transferir riscos e issues
- [ ] Documentar operação, retenção e responsabilidades remanescentes
- [ ] Marcar documentos como arquivados
- [ ] Preservar histórico e rastreabilidade
- [ ] Remover segredos e acessos indevidos
- [ ] Criar referência ao sucessor quando houver
- [ ] Aprovar arquivamento

## 7. Governança da biblioteca

A biblioteca é versionada como especificação. Mudanças incompatíveis exigem nova versão principal; adições compatíveis, versão secundária; correções editoriais, versão de correção. Cada alteração deve registrar motivação, impacto, migração e aprovação.

## 8. Definition of Ready e Definition of Done documentais

**DoR documental:** identidade definida; nível pai conhecido; objetivo e escopo claros; dependências identificadas; fontes disponíveis; responsável atribuído; conflitos resolvidos ou explicitados.

**DoD documental:** seções obrigatórias preenchidas; IDs válidos; relações atualizadas; ausência de duplicidade normativa; critérios verificáveis; histórico atualizado; revisão humana ou autoridade designada concluída; consumo por IA testável.

## 9. Histórico de alterações

| Versão | Data | Alteração | Responsável | Aprovação |
|---|---|---|---|---|
| 1.0 | 2026-08-04 | Emissão inicial da biblioteca oficial de templates do DPF | Arquitetura de Documentação DPF | Pendente de ratificação formal |

## 10. Checklist de conformidade desta especificação

- [x] Mantém a metodologia da Fase 1.
- [x] Mantém a hierarquia Projeto > Capability > Epic > Feature > Task.
- [x] É independente de tecnologia.
- [x] Define todos os templates obrigatórios.
- [x] Define objetivo, responsáveis, ciclo de vida, estrutura, regras, relações e consumo por IA.
- [x] Define padrões de escrita e checklists oficiais.
- [x] Não implementa ferramentas, código, CLI, dashboard ou plugins.
