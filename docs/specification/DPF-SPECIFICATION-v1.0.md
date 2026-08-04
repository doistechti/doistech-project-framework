# DPF Specification v1.0

## DoisTech Project Framework

**Status:** Especificação Oficial
**Versão:** 1.0
**Classificação:** Documento Normativo
**Organização mantenedora:** DoisTech
**Escopo:** Engenharia de software orientada à colaboração entre humanos e agentes de Inteligência Artificial

---

## 1. Introdução

O **DoisTech Project Framework**, identificado pela sigla **DPF**, é uma metodologia de engenharia de software criada para organizar projetos desenvolvidos conjuntamente por profissionais humanos e agentes de Inteligência Artificial.

O DPF estabelece princípios, conceitos, responsabilidades, artefatos, estados, fluxos de trabalho e mecanismos de governança aplicáveis ao ciclo completo de desenvolvimento de software.

Sua finalidade é garantir que agentes de IA possam participar de projetos de software de maneira:

* controlada;
* previsível;
* rastreável;
* contextualizada;
* auditável;
* incremental;
* alinhada às decisões humanas;
* compatível com diferentes tecnologias e arquiteturas.

O DPF não determina uma linguagem de programação, framework, banco de dados, plataforma de infraestrutura ou arquitetura específica.

O DPF também não substitui metodologias como Scrum, Kanban, Domain-Driven Design, Clean Architecture, Extreme Programming, RUP ou CMMI.

Seu propósito é complementar essas abordagens com uma camada metodológica especialmente projetada para projetos em que agentes de IA participam da análise, documentação, planejamento, implementação, testes, revisão, implantação ou manutenção do software.

---

## 2. Natureza normativa

Este documento constitui a referência oficial do DPF.

Todas as futuras definições relacionadas a:

* templates;
* estruturas de projeto;
* agentes;
* prompts;
* ferramentas;
* CLI;
* dashboards;
* integrações;
* plugins;
* automações;
* processos de auditoria;
* mecanismos de conformidade;

deverão ser derivadas desta especificação.

Nenhum artefato posterior poderá contradizer os princípios definidos neste documento sem que esta especificação seja formalmente revisada.

### 2.1 Termos normativos

Os seguintes termos possuem significado obrigatório:

**DEVE**
Indica uma obrigação necessária para conformidade com o DPF.

**NÃO DEVE**
Indica uma proibição.

**DEVERIA**
Indica uma recomendação forte que somente pode ser ignorada mediante justificativa registrada.

**PODE**
Indica uma opção permitida.

**HUMANO RESPONSÁVEL**
Pessoa com autoridade formal para tomar decisões, aprovar mudanças e assumir responsabilidade pelo resultado.

**AGENTE**
Sistema de Inteligência Artificial autorizado a realizar uma atividade delimitada no projeto.

---

## 3. Problema que o DPF resolve

Metodologias tradicionais foram projetadas considerando que a maior parte da interpretação e da implementação seria realizada por pessoas.

Agentes de IA apresentam características diferentes:

* executam rapidamente grandes volumes de trabalho;
* dependem fortemente da qualidade do contexto recebido;
* podem preencher lacunas de informação com inferências indevidas;
* podem produzir soluções tecnicamente válidas, mas desalinhadas ao produto;
* podem alterar partes não solicitadas;
* podem perder decisões tomadas em interações anteriores;
* podem implementar uma funcionalidade sem compreender seus impactos;
* podem gerar divergência entre código, documentação e arquitetura;
* podem repetir soluções já rejeitadas;
* podem introduzir comportamentos não autorizados.

O DPF responde a esses riscos transformando a documentação, o contexto e a governança em elementos centrais do desenvolvimento.

O framework parte do princípio de que uma IA não deve receber apenas uma solicitação de implementação.

Ela deve receber uma unidade de trabalho formal, contextualizada, limitada, verificável e relacionada ao estado atual do projeto.

---

## 4. Objetivos do DPF

O DPF possui os seguintes objetivos:

1. Tornar a especificação anterior à implementação.
2. Transformar a documentação na principal fonte de contexto do projeto.
3. Organizar o produto em unidades de trabalho hierárquicas.
4. Limitar formalmente o escopo de atuação dos agentes.
5. Preservar decisões de produto, negócio e arquitetura.
6. Garantir rastreabilidade entre necessidade, especificação, implementação, teste e release.
7. Manter uma representação atualizada do estado do projeto.
8. Facilitar a transferência de contexto entre pessoas e agentes.
9. Reduzir implementações baseadas em suposições.
10. Permitir evolução incremental e controlada.
11. Promover revisão humana nos pontos de decisão.
12. Estabelecer critérios objetivos de início e conclusão do trabalho.
13. Permitir auditoria das ações realizadas por agentes.
14. Padronizar a comunicação entre análise, desenvolvimento, testes e operação.
15. Manter o framework independente de tecnologia.

---

## 5. Não objetivos

O DPF não possui como objetivo:

* substituir a gestão estratégica da organização;
* eliminar a responsabilidade humana;
* permitir desenvolvimento completamente autônomo e sem supervisão;
* definir uma arquitetura obrigatória;
* definir uma linguagem de programação;
* definir uma ferramenta obrigatória;
* substituir processos jurídicos, regulatórios ou de segurança;
* transformar toda solicitação em implementação automática;
* permitir que agentes criem regras de negócio sem autorização;
* permitir que agentes alterem decisões arquiteturais por conveniência;
* centralizar todo o projeto em um único documento;
* exigir a mesma profundidade documental para projetos de portes diferentes.

---

# PARTE I — PRINCÍPIOS FUNDAMENTAIS

## 6. Specification First

Todo trabalho de desenvolvimento DEVE nascer de uma especificação.

A especificação DEVE existir antes da implementação.

O código é considerado uma consequência da especificação, e não sua origem.

Uma implementação iniciada sem contexto, critérios e escopo formalmente definidos é considerada não conforme com o DPF.

### 6.1 Aplicação

Antes de uma Task entrar em implementação, devem estar definidos, no mínimo:

* objetivo;
* contexto;
* escopo;
* resultado esperado;
* critérios de aceitação;
* dependências;
* restrições;
* artefatos afetados;
* forma de validação.

### 6.2 Exceções

Atividades exploratórias podem ocorrer antes de uma especificação completa, desde que sejam formalmente classificadas como:

* investigação;
* experimento;
* prova de conceito;
* diagnóstico;
* descoberta técnica.

Essas atividades NÃO DEVEM ser tratadas como implementação definitiva.

---

## 7. Documentation as Source of Truth

A documentação oficial representa a intenção válida do projeto.

Quando houver divergência entre documentação e implementação, a divergência DEVE ser investigada.

Até que a documentação seja formalmente revisada, ela permanece como referência oficial da intenção do projeto.

Isso não significa que uma documentação incorreta deva ser aplicada de maneira cega.

Significa que nenhum agente ou desenvolvedor possui autorização para reinterpretar silenciosamente a intenção registrada.

A divergência deve resultar em uma das seguintes ações:

1. correção da implementação;
2. revisão aprovada da documentação;
3. registro formal de exceção;
4. criação de uma Architecture Decision;
5. suspensão da Task até decisão humana.

---

## 8. Context Driven Development

Nenhuma implementação deve ocorrer isoladamente.

Antes de atuar, o executor DEVE compreender o contexto necessário para a atividade.

Esse contexto pode incluir:

* visão do produto;
* problema de negócio;
* usuários envolvidos;
* Capability relacionada;
* Epic relacionada;
* Feature relacionada;
* regras de negócio;
* casos de uso;
* arquitetura vigente;
* decisões arquiteturais;
* contratos de integração;
* modelo de dados;
* requisitos de segurança;
* critérios de aceite;
* estado atual do projeto;
* limitações conhecidas.

O contexto fornecido deve ser proporcional ao trabalho.

O DPF não exige que um agente leia toda a documentação do projeto para executar qualquer Task.

O framework exige que ele consulte todo o contexto relevante para aquela Task.

---

## 9. AI Native

O DPF é projetado para que sua documentação seja compreendida tanto por humanos quanto por agentes de IA.

Os artefatos devem ser:

* claros;
* explícitos;
* objetivos;
* estáveis;
* versionáveis;
* navegáveis;
* semanticamente consistentes;
* divididos por responsabilidade;
* livres de contradições;
* rastreáveis.

Termos diferentes NÃO DEVEM ser usados para representar o mesmo conceito sem justificativa.

Um mesmo termo NÃO DEVE representar conceitos diferentes.

Informações críticas NÃO DEVEM depender exclusivamente de conversas informais ou da memória de um agente.

---

## 10. Modularidade

O projeto DEVE ser dividido em unidades menores, relacionadas e identificáveis.

A modularidade deve existir tanto no produto quanto no trabalho.

O DPF organiza o produto por meio da hierarquia:

**Projeto → Capability → Epic → Feature → Task**

Cada nível possui objetivo, escopo e responsabilidade próprios.

Uma unidade não deve acumular responsabilidades pertencentes a diferentes níveis.

---

## 11. Evolução Incremental

O produto deve evoluir por incrementos verificáveis.

O DPF rejeita a construção de grandes blocos monolíticos sem validações intermediárias.

Cada incremento deveria:

* entregar valor;
* reduzir incerteza;
* validar uma hipótese;
* completar uma parte utilizável;
* preparar uma capacidade futura;
* melhorar qualidade, segurança ou operação.

A evolução incremental não significa fragmentação artificial.

Tasks e Features devem ser pequenas o suficiente para controle, mas completas o suficiente para produzir um resultado verificável.

---

## 12. Human Accountability

A responsabilidade final pelo produto permanece humana.

Agentes podem:

* analisar;
* sugerir;
* documentar;
* implementar;
* revisar;
* testar;
* comparar;
* diagnosticar;
* automatizar.

Entretanto, decisões de negócio, produto, arquitetura, segurança e liberação devem possuir um responsável humano identificável.

A IA não é considerada autoridade organizacional.

---

## 13. Least Necessary Change

Uma Task DEVE produzir apenas as alterações necessárias para cumprir seu objetivo.

O executor NÃO DEVE:

* refatorar áreas não relacionadas;
* alterar padrões globais sem autorização;
* adicionar funcionalidades não solicitadas;
* trocar tecnologias por preferência própria;
* modificar contratos externos sem aprovação;
* corrigir problemas adjacentes sem registrá-los.

Problemas encontrados fora do escopo devem ser registrados separadamente.

---

## 14. Traceability by Design

Todo elemento de implementação deve ser rastreável até uma necessidade formal.

Idealmente, deve ser possível percorrer a cadeia:

**Projeto → Capability → Epic → Feature → Task → Alteração → Teste → Release**

A rastreabilidade permite compreender:

* por que algo existe;
* quem autorizou;
* quando foi implementado;
* qual regra atende;
* como foi validado;
* em qual release foi disponibilizado;
* quais decisões influenciaram sua construção.

---

# PARTE II — MODELO HIERÁRQUICO DO DPF

## 15. Hierarquia oficial

A hierarquia oficial do DPF é:

**Projeto**

↓

**Capability**

↓

**Epic**

↓

**Feature**

↓

**Task**

Essa hierarquia representa a decomposição progressiva da visão estratégica até uma unidade executável.

Cada elemento DEVE possuir um identificador único dentro de seu contexto.

---

## 16. Projeto

### 16.1 Definição

Projeto é a unidade de mais alto nível do DPF.

Representa um produto, sistema, serviço, plataforma, componente estratégico ou iniciativa de software com identidade, propósito e governança próprios.

### 16.2 Objetivo

O Projeto estabelece:

* visão;
* problema principal;
* público;
* limites;
* objetivos;
* princípios;
* responsáveis;
* arquitetura de alto nível;
* ciclo de vida;
* critérios de sucesso.

### 16.3 Responsabilidade

O Projeto é responsável por reunir todas as Capabilities e demais artefatos necessários à construção e evolução do produto.

### 16.4 Escopo

O escopo de um Projeto deve ser suficientemente coeso para possuir:

* uma visão comum;
* uma governança comum;
* um roadmap relacionado;
* uma identidade reconhecível;
* um estado gerenciável.

### 16.5 Relacionamento

Um Projeto contém uma ou mais Capabilities.

Uma Capability DEVE pertencer a um Projeto principal.

Um Projeto pode se relacionar com outros projetos por integrações, dependências ou ecossistemas, mas não deve incorporar informalmente o escopo de outro Projeto.

### 16.6 Critérios

Um Projeto deve possuir:

* objetivo explícito;
* patrocinador ou responsável;
* usuários ou beneficiários identificados;
* visão de produto;
* escopo inicial;
* critérios de sucesso;
* estado formal;
* documentação oficial.

### 16.7 Exemplo

Um sistema de gestão de agendas para organizações pode constituir um Projeto.

Dentro dele podem existir Capabilities de:

* gestão de usuários;
* gestão de agendas;
* notificações;
* pagamentos;
* relatórios.

---

## 17. Capability

### 17.1 Definição

Capability é uma capacidade relevante que o Projeto precisa oferecer para cumprir sua visão.

Representa “o que o produto é capaz de fazer” em nível amplo.

Uma Capability é estável e orientada ao domínio ou à operação do produto.

### 17.2 Objetivo

A Capability organiza grandes áreas de valor e responsabilidade do sistema.

### 17.3 Responsabilidade

A Capability agrupa Epics que, em conjunto, materializam uma capacidade do produto.

### 17.4 Escopo

Uma Capability deve possuir escopo suficientemente amplo para comportar diferentes evoluções, mas suficientemente específico para representar uma capacidade reconhecível.

### 17.5 Relacionamento

* Uma Capability pertence a um Projeto.
* Uma Capability contém uma ou mais Epics.
* Uma Capability pode depender de outras Capabilities.
* Dependências devem ser explícitas.
* Uma Capability não deve ser confundida com módulo técnico.

Uma Capability pode atravessar diferentes componentes técnicos.

### 17.6 Critérios

Uma Capability deve:

* expressar uma capacidade de negócio, produto ou operação;
* possuir objetivo duradouro;
* ser compreensível sem depender da implementação;
* ser decomponível em Epics;
* possuir limites claros;
* permitir avaliação de maturidade ou evolução.

### 17.7 Exemplo

**Capability: Gestão de Agendamentos**

Pode conter Epics como:

* criação e manutenção de agendas;
* disponibilidade de profissionais;
* reserva de horários;
* cancelamento e reagendamento;
* bloqueio de períodos.

---

## 18. Epic

### 18.1 Definição

Epic é uma iniciativa de grande porte dentro de uma Capability.

Representa um resultado relevante que exige múltiplas Features para ser concluído.

### 18.2 Objetivo

A Epic transforma uma Capability ampla em um objetivo de entrega gerenciável.

### 18.3 Responsabilidade

A Epic agrupa Features relacionadas que, juntas, produzem um resultado funcional ou estratégico.

### 18.4 Escopo

Uma Epic deve ser maior que uma Feature e menor que uma Capability.

Ela pode atravessar:

* backend;
* frontend;
* mobile;
* infraestrutura;
* dados;
* segurança;
* integrações;
* documentação.

### 18.5 Relacionamento

* Uma Epic pertence a uma Capability.
* Uma Epic contém uma ou mais Features.
* Uma Epic pode depender de outras Epics.
* Uma Epic pode atravessar mais de uma Release.
* Uma Epic não precisa ser concluída em uma Sprint.

### 18.6 Critérios

Uma Epic deve:

* possuir resultado esperado;
* representar valor identificável;
* permitir decomposição em Features independentes;
* possuir critérios de conclusão;
* possuir dependências conhecidas;
* ter responsável humano.

### 18.7 Exemplo

Dentro da Capability Gestão de Agendamentos:

**Epic: Reserva de horários pelos clientes**

Pode conter:

* consulta de horários disponíveis;
* seleção de serviço;
* confirmação da reserva;
* cancelamento;
* reagendamento;
* envio de confirmação.

---

## 19. Feature

### 19.1 Definição

Feature é uma funcionalidade coerente, utilizável e verificável que entrega uma parte identificável de valor.

A Feature define o comportamento esperado pelo ponto de vista do usuário, negócio ou sistema consumidor.

### 19.2 Objetivo

A Feature transforma uma Epic em uma entrega funcional delimitada.

### 19.3 Responsabilidade

A Feature deve especificar:

* problema resolvido;
* comportamento;
* usuários ou atores;
* fluxo principal;
* variações;
* regras aplicáveis;
* critérios de aceitação;
* impactos;
* restrições.

### 19.4 Escopo

Uma Feature pode exigir diversas Tasks.

Ela pode envolver diferentes especialidades, desde que o resultado final permaneça coeso.

### 19.5 Relacionamento

* Uma Feature pertence a uma Epic.
* Uma Feature contém uma ou mais Tasks.
* Uma Feature pode depender de outras Features.
* Uma Feature pode ser planejada para uma Release.
* Uma Feature deveria ser pequena o suficiente para validação independente.

### 19.6 Critérios

Uma Feature deve:

* entregar valor observável;
* possuir escopo delimitado;
* possuir critérios de aceitação testáveis;
* respeitar regras de negócio existentes;
* identificar impactos técnicos;
* ser decomponível em Tasks;
* possuir estado controlado.

### 19.7 Exemplo

**Feature: Consultar horários disponíveis**

A funcionalidade permite que um cliente consulte os horários disponíveis de um profissional para determinado serviço e período.

---

## 20. Task

### 20.1 Definição

Task é a menor unidade oficial de execução do DPF.

Ela descreve um trabalho específico, delimitado, verificável e atribuível a um humano ou agente.

### 20.2 Objetivo

A Task converte a especificação da Feature em uma ação concreta.

### 20.3 Responsabilidade

Uma Task deve informar com clareza:

* o que deve ser feito;
* por que deve ser feito;
* onde a alteração é permitida;
* quais comportamentos devem ser preservados;
* quais critérios indicam conclusão;
* quais testes devem ser realizados;
* quais documentos devem ser atualizados.

### 20.4 Escopo

Uma Task deve possuir escopo pequeno e controlável.

Ela não deve exigir decisões estratégicas durante sua execução.

Caso uma decisão relevante seja necessária, a Task deve ser suspensa ou redirecionada para análise.

### 20.5 Relacionamento

* Uma Task pertence normalmente a uma Feature.
* Uma Task pode atender manutenção, dívida técnica, segurança ou operação.
* Quando não estiver ligada a uma Feature, deve possuir justificativa e rastreabilidade equivalentes.
* Uma Task pode possuir subtarefas operacionais, mas estas não substituem a Task como unidade formal.

### 20.6 Critérios

Uma Task deve:

* possuir resultado objetivo;
* ser executável por um responsável definido;
* conter contexto suficiente;
* possuir critérios de aceitação;
* possuir limites explícitos;
* identificar dependências;
* atender à Definition of Ready antes da execução;
* atender à Definition of Done antes da conclusão.

### 20.7 Exemplo

Para a Feature “Consultar horários disponíveis”:

* implementar serviço de consulta de disponibilidade;
* expor contrato de consulta;
* criar interface de seleção de data;
* adicionar testes para conflitos de horário;
* documentar regras de disponibilidade.

---

## 21. Diferença entre Feature e Task

A Feature representa **o comportamento ou valor que será entregue**.

A Task representa **o trabalho necessário para produzir esse comportamento ou valor**.

Uma Task não deve ser descrita como Feature apenas porque contém uma implementação relevante.

Exemplo:

**Feature:** Permitir que o cliente reagende um atendimento.

**Tasks:**

* implementar regra de elegibilidade para reagendamento;
* criar operação de reagendamento;
* atualizar interface;
* enviar notificação;
* criar testes;
* atualizar documentação.

Uma Feature pode gerar diversas Tasks.

Uma Task individual normalmente não representa toda a experiência funcional.

---

# PARTE III — CONCEITOS OFICIAIS

## 22. Release

Release é um conjunto versionado de alterações aprovado para disponibilização em determinado ambiente ou público.

Uma Release pode incluir:

* Features;
* correções;
* melhorias;
* mudanças técnicas;
* atualizações de segurança;
* atualizações documentais;
* alterações operacionais.

Toda Release deve possuir:

* identificação;
* versão;
* escopo;
* conteúdo;
* dependências;
* riscos conhecidos;
* critérios de liberação;
* evidências de validação;
* plano de implantação;
* plano de reversão, quando aplicável;
* registro no Change Log.

Uma Release não é sinônimo de Sprint.

---

## 23. Sprint

Sprint é uma janela de trabalho com duração definida, utilizada para organizar a execução de um conjunto de itens.

O DPF permite Sprints, mas não as torna obrigatórias.

Projetos que utilizam fluxo contínuo podem operar sem Sprint.

Quando adotada, uma Sprint deve possuir:

* objetivo;
* início;
* fim;
* itens comprometidos;
* responsáveis;
* critérios de encerramento;
* resultado registrado.

Uma Sprint organiza trabalho.

Ela não altera a hierarquia Projeto → Capability → Epic → Feature → Task.

---

## 24. Milestone

Milestone é um ponto relevante de progresso ou decisão no ciclo de vida do Projeto.

Pode representar:

* conclusão de uma fase;
* validação de uma hipótese;
* entrega de MVP;
* disponibilidade pública;
* migração;
* aprovação regulatória;
* estabilização operacional;
* encerramento de uma Epic estratégica.

Um Milestone pode incluir múltiplas Releases e não precisa corresponder a uma data exata durante sua concepção inicial.

---

## 25. Roadmap

Roadmap é a representação da evolução planejada do Projeto ao longo do tempo.

O Roadmap deve comunicar:

* direção;
* prioridades;
* Capabilities;
* Epics;
* Milestones;
* dependências;
* horizonte de planejamento;
* incertezas.

O Roadmap não deve ser tratado como promessa imutável.

Alterações no Roadmap devem ser registradas quando afetarem compromissos relevantes.

---

## 26. Agent

Agent é um sistema de IA autorizado a desempenhar um papel especializado dentro dos limites do DPF.

Um Agent deve possuir:

* identidade funcional;
* responsabilidade;
* escopo;
* entradas esperadas;
* saídas permitidas;
* restrições;
* permissões;
* critérios de encerramento;
* regras de escalonamento humano.

Um Agent não recebe autoridade implícita por sua capacidade técnica.

A autoridade depende do papel atribuído e do contexto fornecido.

---

## 27. Prompt

Prompt é uma instrução estruturada utilizada para orientar a atuação de um Agent.

No DPF, o Prompt não é uma mensagem informal isolada.

Ele representa um contrato operacional contendo, conforme o caso:

* papel;
* objetivo;
* contexto;
* escopo;
* entradas;
* restrições;
* resultado esperado;
* critérios de qualidade;
* ações proibidas;
* formato de saída;
* referências documentais;
* condição de parada.

Prompts oficiais devem ser versionados.

---

## 28. Architecture Decision

Architecture Decision é o registro formal de uma decisão arquitetural relevante.

Deve ser criado quando uma escolha:

* afeta múltiplas Features;
* altera estrutura do sistema;
* introduz ou remove uma tecnologia relevante;
* modifica contratos;
* afeta segurança;
* afeta escalabilidade;
* cria dependência importante;
* estabelece um padrão;
* substitui uma decisão anterior.

Uma Architecture Decision deve apresentar:

* contexto;
* problema;
* opções consideradas;
* decisão;
* justificativa;
* consequências;
* riscos;
* status;
* responsáveis;
* relação com decisões anteriores.

Agents podem propor Architecture Decisions, mas não devem aprová-las autonomamente.

---

## 29. Project State

Project State é a representação oficial, resumida e atualizada da situação do Projeto.

Ele informa o que o Projeto é, onde se encontra, o que está em andamento, o que foi concluído e quais decisões ou bloqueios afetam sua continuidade.

O Project State é detalhado na Parte IV desta especificação.

---

## 30. Business Rule

Business Rule é uma condição, restrição, cálculo, permissão, proibição ou política que governa o comportamento do produto.

Uma Business Rule deve ser:

* explícita;
* identificável;
* testável;
* rastreável;
* independente da forma de implementação.

Exemplos:

* um usuário não pode reservar dois horários conflitantes;
* um cancelamento só pode ocorrer até determinado prazo;
* um desconto depende de uma condição de elegibilidade.

Agents NÃO DEVEM inventar Business Rules.

Lacunas devem ser encaminhadas ao responsável humano.

---

## 31. Use Case

Use Case descreve uma interação entre um ator e o sistema para atingir um objetivo.

Deve conter, quando aplicável:

* ator;
* objetivo;
* pré-condições;
* gatilho;
* fluxo principal;
* fluxos alternativos;
* exceções;
* pós-condições;
* regras aplicáveis.

Um Use Case pode fundamentar uma ou mais Features.

---

## 32. Workflow

Workflow é uma sequência de estados, decisões, ações e transições relacionadas a um processo.

Pode representar:

* fluxo de negócio;
* fluxo operacional;
* fluxo de desenvolvimento;
* fluxo de aprovação;
* fluxo de implantação.

Um Workflow deve tornar explícitos:

* ponto de início;
* participantes;
* estados;
* transições;
* condições;
* exceções;
* término.

---

## 33. Template

Template é uma estrutura padronizada para criação de um artefato do DPF.

Templates serão definidos em fases posteriores.

Todo Template futuro deve:

* refletir esta especificação;
* preservar o significado dos conceitos;
* reduzir ambiguidade;
* facilitar consumo humano e por IA;
* permitir versionamento;
* evitar campos sem finalidade metodológica.

---

## 34. Checklist

Checklist é uma lista objetiva de verificações necessárias para garantir que uma atividade ou artefato atende a critérios definidos.

Checklists podem existir para:

* análise;
* arquitetura;
* segurança;
* implementação;
* revisão;
* testes;
* release;
* documentação;
* implantação.

O preenchimento mecânico de um Checklist não substitui julgamento profissional.

---

## 35. Definition of Ready

Definition of Ready, ou DoR, é o conjunto mínimo de condições para que um item possa entrar em execução.

Uma Feature ou Task está Ready quando possui contexto suficiente para ser executada sem depender de decisões fundamentais ainda não tomadas.

Uma Task pronta deve possuir, no mínimo:

* objetivo;
* vínculo hierárquico;
* escopo;
* critérios de aceitação;
* dependências conhecidas;
* regras relacionadas;
* restrições;
* forma de validação;
* responsável;
* ausência de bloqueios críticos.

Caso a execução revele lacunas fundamentais, o estado Ready pode ser revogado.

---

## 36. Definition of Done

Definition of Done, ou DoD, é o conjunto mínimo de condições para que um item seja considerado concluído.

Uma Task não está Done apenas porque o código foi escrito.

A conclusão pode exigir:

* implementação completa;
* critérios de aceitação atendidos;
* testes executados;
* revisão concluída;
* documentação atualizada;
* ausência de falhas críticas;
* rastreabilidade preservada;
* impactos avaliados;
* aprovação necessária obtida;
* Project State atualizado;
* Change Log atualizado, quando aplicável.

A Definition of Done pode possuir critérios adicionais conforme o tipo de projeto.

---

## 37. Technical Debt

Technical Debt é uma condição técnica conhecida que reduz qualidade, segurança, manutenibilidade, confiabilidade, desempenho ou capacidade de evolução do sistema.

Toda dívida técnica relevante deve ser registrada.

O registro deve informar:

* origem;
* impacto;
* risco;
* área afetada;
* motivo de aceitação;
* ação recomendada;
* prioridade;
* responsável;
* prazo ou gatilho de revisão, quando aplicável.

Agents não devem ocultar dívida técnica para concluir uma Task.

---

## 38. Change Log

Change Log é o registro cronológico de mudanças relevantes do Projeto.

Deve permitir compreender:

* o que mudou;
* quando mudou;
* por que mudou;
* quem autorizou;
* quais itens foram afetados;
* em qual versão ou Release ocorreu.

O Change Log não substitui o histórico do controle de versão.

Ele registra mudanças relevantes para compreensão do produto.

---

## 39. Versionamento

Versionamento é o processo de atribuir identificadores às evoluções de documentos, especificações, decisões, contratos, componentes ou Releases.

O DPF exige versionamento para artefatos cuja mudança possa afetar interpretação, implementação ou compatibilidade.

Uma mudança de versão deve refletir o impacto da alteração.

O modelo específico de versionamento poderá variar, mas deve distinguir pelo menos:

* correções sem alteração de significado;
* mudanças compatíveis;
* mudanças incompatíveis ou estruturais.

Alterações documentais relevantes devem possuir histórico.

---

# PARTE IV — PROJECT STATE

## 40. Definição do Project State

Project State é o mecanismo oficial de continuidade contextual do DPF.

Ele fornece uma visão confiável e atual do Projeto para humanos e Agents.

Seu objetivo é reduzir a dependência de:

* memória individual;
* histórico de conversas;
* conhecimento informal;
* leitura integral do repositório;
* interpretação isolada do código.

O Project State não substitui os documentos detalhados.

Ele funciona como mapa de navegação e síntese operacional.

---

## 41. Objetivos do Project State

O Project State deve permitir que um novo participante compreenda rapidamente:

* qual é o Projeto;
* qual problema ele resolve;
* qual versão está vigente;
* quais Capabilities existem;
* quais Epics estão ativas;
* quais Features estão planejadas;
* quais Features estão implementadas;
* quais Tasks estão em andamento;
* quais decisões são vigentes;
* quais bloqueios existem;
* quais riscos estão abertos;
* quais dívidas técnicas são relevantes;
* qual é a próxima prioridade;
* qual Release está em preparação;
* quais documentos devem ser consultados.

---

## 42. Funcionamento

O Project State deve consolidar informações provenientes dos artefatos oficiais.

Ele deve atuar como índice e resumo, não como cópia integral de toda a documentação.

As informações do Project State devem apontar para suas fontes detalhadas.

Exemplo de relacionamento conceitual:

* visão do produto aponta para o documento de visão;
* regras apontam para o catálogo de regras;
* decisões apontam para registros arquiteturais;
* Features apontam para suas especificações;
* Tasks apontam para seu controle de execução;
* Releases apontam para seus registros;
* riscos apontam para seus responsáveis.

---

## 43. Responsabilidade

Todo Projeto deve possuir um responsável pelo Project State.

Essa responsabilidade pode ser atribuída a:

* líder técnico;
* arquiteto;
* product owner;
* gestor do Projeto;
* Documentation Agent sob supervisão humana.

A responsabilidade final permanece humana.

---

## 44. Atualização

O Project State DEVE ser atualizado quando ocorrer uma mudança relevante, incluindo:

* criação ou encerramento de Capability;
* criação ou conclusão de Epic;
* mudança de estado de Feature;
* início ou conclusão de Task relevante;
* aprovação de Architecture Decision;
* identificação de bloqueio;
* alteração de prioridade;
* preparação ou publicação de Release;
* identificação de risco crítico;
* criação de dívida técnica relevante;
* mudança do Roadmap;
* alteração de regra de negócio.

Atualizações deveriam ocorrer no mesmo fluxo que gera a mudança.

Não devem ser deixadas indefinidamente para uma etapa futura.

---

## 45. Estados mínimos

O Project State deve permitir distinguir, no mínimo:

* planejado;
* pronto para execução;
* em andamento;
* bloqueado;
* em revisão;
* em validação;
* concluído;
* cancelado;
* substituído;
* implantado.

Um Projeto pode adicionar estados, desde que não altere o significado dos estados básicos sem documentação.

---

## 46. Documentos relacionados

O Project State se relaciona especialmente com:

* PROJECT.md;
* PRODUCT-VISION.md;
* ROADMAP.md;
* PLANNED.md;
* IMPLEMENTED.md;
* CURRENT-SPRINT.md;
* DECISIONS.md;
* CHANGELOG.md;
* registros de Features;
* registros de Tasks;
* registros de Releases;
* registro de dívidas técnicas;
* catálogo de riscos.

Os nomes concretos podem evoluir em versões futuras da implementação do framework, mas as responsabilidades documentais devem ser preservadas.

---

# PARTE V — AGENTES ESPECIALIZADOS

## 47. Modelo geral de Agent

Todo Agent deve operar segundo um contrato de atuação.

Esse contrato deve definir:

* papel;
* objetivo;
* autoridade;
* entradas;
* saídas;
* limites;
* documentos obrigatórios;
* artefatos que pode alterar;
* artefatos que não pode alterar;
* condições de parada;
* necessidade de aprovação;
* forma de registrar sua atuação.

Agents não devem assumir permissões não declaradas.

---

## 48. Architect Agent

### Responsabilidades

* analisar impactos arquiteturais;
* propor opções de solução;
* identificar dependências;
* verificar aderência à arquitetura vigente;
* produzir propostas de Architecture Decision;
* revisar mudanças estruturais;
* detectar violações de padrões aprovados.

### Entradas

* visão do Projeto;
* System Design;
* Architecture Decisions vigentes;
* requisitos não funcionais;
* Feature ou problema técnico;
* restrições;
* integrações existentes.

### Saídas

* análise arquitetural;
* opções;
* riscos;
* impactos;
* recomendação;
* proposta de Architecture Decision;
* parecer de conformidade.

### Limites

O Architect Agent NÃO DEVE:

* aprovar sozinho uma decisão arquitetural;
* substituir uma decisão vigente sem autorização;
* escolher tecnologia apenas por preferência;
* alterar regra de negócio;
* implementar mudanças fora da Task.

---

## 49. Business Analyst Agent

### Responsabilidades

* organizar requisitos;
* identificar atores;
* descrever Use Cases;
* mapear Workflows;
* identificar ambiguidades;
* relacionar Business Rules;
* decompor necessidades em Features;
* preparar critérios de aceitação.

### Entradas

* visão do produto;
* solicitação do negócio;
* entrevistas;
* regras existentes;
* processos atuais;
* limitações;
* feedback de usuários.

### Saídas

* análise de requisitos;
* Use Cases;
* Workflows;
* critérios de aceitação;
* propostas de Feature;
* perguntas pendentes;
* mapa de regras relacionadas.

### Limites

O Business Analyst Agent NÃO DEVE:

* inventar regras;
* definir política comercial;
* presumir comportamento sem evidência;
* aprovar requisitos;
* transformar hipótese em regra oficial.

---

## 50. Backend Agent

### Responsabilidades

* implementar Tasks de backend;
* preservar contratos;
* aplicar regras especificadas;
* criar ou atualizar testes;
* tratar erros;
* manter rastreabilidade;
* informar impactos identificados.

### Entradas

* Task aprovada;
* Feature;
* regras de negócio;
* arquitetura;
* contratos;
* modelo de dados;
* padrões do Projeto;
* critérios de aceitação.

### Saídas

* alteração implementada;
* testes;
* relatório de execução;
* documentação técnica atualizada;
* riscos ou limitações encontradas.

### Limites

O Backend Agent NÃO DEVE:

* alterar contratos sem autorização;
* criar regras;
* mudar arquitetura;
* alterar componentes não relacionados;
* realizar migrações destrutivas sem aprovação;
* ignorar requisitos de segurança.

---

## 51. Frontend Agent

### Responsabilidades

* implementar interfaces;
* integrar contratos aprovados;
* aplicar fluxos e estados definidos;
* garantir validações;
* manter acessibilidade conforme requisitos;
* criar ou atualizar testes;
* preservar padrões visuais.

### Entradas

* Task;
* Feature;
* Workflow;
* design;
* contratos;
* regras;
* estados;
* critérios de aceitação;
* padrões do Projeto.

### Saídas

* interface implementada;
* testes;
* documentação;
* evidências de comportamento;
* registro de limitações.

### Limites

O Frontend Agent NÃO DEVE:

* alterar regras de negócio;
* redefinir fluxos;
* criar endpoints fictícios como solução definitiva;
* mudar identidade visual sem autorização;
* alterar contratos unilateralmente.

---

## 52. Mobile Agent

### Responsabilidades

* implementar experiências mobile;
* observar restrições da plataforma;
* integrar contratos;
* tratar permissões e estados;
* validar comportamento offline, quando aplicável;
* produzir testes e documentação.

### Entradas

* Task;
* Feature;
* fluxos;
* contratos;
* requisitos de plataforma;
* regras;
* critérios de aceite.

### Saídas

* implementação mobile;
* testes;
* documentação;
* requisitos de publicação;
* riscos de plataforma.

### Limites

O Mobile Agent NÃO DEVE:

* alterar escopo da Feature;
* adicionar permissões desnecessárias;
* definir política de distribuição;
* ignorar requisitos de privacidade;
* mudar contratos sem aprovação.

---

## 53. DevOps Agent

### Responsabilidades

* automatizar infraestrutura;
* configurar pipelines;
* preparar ambientes;
* implementar observabilidade;
* apoiar implantação e reversão;
* analisar confiabilidade;
* documentar operação.

### Entradas

* arquitetura;
* requisitos de ambiente;
* requisitos de segurança;
* plano de Release;
* padrões operacionais;
* Task aprovada.

### Saídas

* configuração operacional;
* pipeline;
* documentação de implantação;
* evidências;
* plano de rollback;
* análise de riscos.

### Limites

O DevOps Agent NÃO DEVE:

* implantar em produção sem autorização;
* remover dados ou recursos sem aprovação;
* expor segredos;
* alterar topologia crítica sem decisão;
* reduzir controles para acelerar entrega.

---

## 54. QA Agent

### Responsabilidades

* derivar cenários de teste;
* verificar critérios de aceitação;
* executar validações;
* identificar regressões;
* avaliar casos extremos;
* produzir evidências;
* recomendar aprovação ou reprovação.

### Entradas

* Feature;
* Task;
* Business Rules;
* Use Cases;
* critérios de aceitação;
* implementação;
* plano de testes.

### Saídas

* casos de teste;
* resultados;
* defeitos;
* evidências;
* cobertura avaliada;
* parecer de qualidade.

### Limites

O QA Agent NÃO DEVE:

* alterar requisitos para fazer o teste passar;
* encerrar defeito sem evidência;
* aprovar comportamento divergente;
* corrigir implementação silenciosamente quando seu papel for apenas validar.

---

## 55. Documentation Agent

### Responsabilidades

* manter documentação consistente;
* atualizar o Project State;
* registrar alterações;
* identificar divergências;
* organizar referências;
* verificar terminologia;
* preservar rastreabilidade.

### Entradas

* artefatos alterados;
* resultados de Tasks;
* Architecture Decisions;
* Releases;
* evidências;
* estado anterior.

### Saídas

* documentação atualizada;
* Project State atualizado;
* Change Log;
* links de rastreabilidade;
* relatório de inconsistências.

### Limites

O Documentation Agent NÃO DEVE:

* mudar significado de regras;
* aprovar decisões;
* ocultar divergências;
* reescrever especificações para justificar código incorreto;
* transformar hipótese em decisão oficial.

---

## 56. Security Agent

### Responsabilidades

* avaliar ameaças;
* revisar controles;
* identificar vulnerabilidades;
* verificar exposição de dados;
* analisar autenticação e autorização;
* recomendar mitigação;
* revisar mudanças sensíveis.

### Entradas

* arquitetura;
* Feature;
* Task;
* modelo de dados;
* fluxos;
* contratos;
* requisitos regulatórios;
* implementação.

### Saídas

* análise de segurança;
* riscos;
* severidade;
* recomendações;
* critérios de correção;
* parecer de segurança.

### Limites

O Security Agent NÃO DEVE:

* executar ações destrutivas fora de ambiente autorizado;
* expor dados reais;
* modificar política de segurança unilateralmente;
* aceitar risco em nome da organização.

---

## 57. Database Agent

### Responsabilidades

* analisar modelos de dados;
* propor estruturas;
* avaliar integridade;
* revisar consultas;
* planejar migrações;
* verificar desempenho;
* proteger consistência e rastreabilidade.

### Entradas

* modelo de domínio;
* regras;
* arquitetura;
* Task;
* contratos;
* requisitos de retenção;
* requisitos de desempenho.

### Saídas

* proposta de modelo;
* alteração controlada;
* plano de migração;
* análise de impacto;
* testes;
* documentação.

### Limites

O Database Agent NÃO DEVE:

* executar operação destrutiva sem autorização;
* remover dados para resolver inconsistências;
* alterar significado de campos;
* criar regra de negócio implícita no banco sem especificação;
* modificar produção autonomamente.

---

## 58. Interação entre Agents

Agents devem colaborar por meio de artefatos formais.

Uma saída relevante de um Agent deve ser consumível por outro Agent sem depender exclusivamente da conversa original.

Exemplo:

1. Business Analyst Agent organiza a Feature.
2. Architect Agent analisa impactos.
3. Humano aprova as decisões.
4. Backend, Frontend ou Mobile Agents executam Tasks.
5. QA Agent valida.
6. Security Agent revisa aspectos sensíveis.
7. Documentation Agent atualiza o estado.
8. Humano autoriza Release.

Um Agent não deve sobrescrever silenciosamente o trabalho de outro.

Conflitos devem ser registrados e escalados.

---

# PARTE VI — PROMPTS OFICIAIS

## 59. Natureza dos prompts oficiais

Prompts oficiais são mecanismos padronizados de instrução.

Cada categoria de Prompt deve possuir finalidade, entradas mínimas, restrições e resultado esperado.

Os Prompts não substituem a documentação.

Eles conectam a documentação a uma atividade específica.

---

## 60. Prompt para criar Capability

Finalidade:

* transformar uma necessidade ampla do Projeto em uma capacidade organizada;
* definir limites;
* relacionar valor, objetivos e dependências;
* evitar que funcionalidades isoladas sejam criadas sem contexto estratégico.

O resultado deve ser uma proposta de Capability para aprovação humana.

---

## 61. Prompt para criar Epic

Finalidade:

* decompor uma Capability em uma iniciativa relevante;
* estabelecer resultado, escopo e critérios de conclusão;
* preparar posterior decomposição em Features.

O Agent deve preservar os limites da Capability.

---

## 62. Prompt para criar Feature

Finalidade:

* transformar uma necessidade funcional em comportamento verificável;
* identificar atores, regras, fluxos, exceções e critérios de aceitação;
* preparar a criação de Tasks.

O Agent deve destacar dúvidas em vez de inventar respostas.

---

## 63. Prompt para criar Task

Finalidade:

* transformar uma Feature em uma unidade executável;
* limitar alterações;
* definir entradas, saídas, testes e critérios;
* indicar documentos afetados.

Uma Task criada por Agent deve ser revisada quando envolver impacto relevante.

---

## 64. Prompt para revisar código

Finalidade:

* comparar implementação com Task, Feature, arquitetura, regras e padrões;
* identificar defeitos, riscos, regressões e mudanças indevidas;
* verificar se a alteração permaneceu dentro do escopo.

A revisão não deve se limitar a estilo.

---

## 65. Prompt para refatorar

Finalidade:

* melhorar estrutura interna sem alterar comportamento não autorizado;
* definir limites precisos;
* preservar contratos;
* exigir testes;
* registrar impacto.

Refatorações amplas não devem ser executadas como consequência informal de outra Task.

---

## 66. Prompt para gerar testes

Finalidade:

* derivar testes dos critérios de aceitação, regras, fluxos e riscos;
* cobrir caminho principal, exceções e limites;
* evitar testes desconectados do comportamento esperado.

O Agent não deve adaptar requisitos para facilitar os testes.

---

## 67. Prompt para atualizar documentação

Finalidade:

* sincronizar os artefatos oficiais após uma mudança aprovada;
* atualizar Project State, Change Log e documentos afetados;
* preservar histórico;
* detectar divergências.

A documentação não deve ser alterada apenas para legitimar uma implementação divergente.

---

## 68. Prompt para preparar Release

Finalidade:

* consolidar itens;
* verificar critérios de liberação;
* avaliar riscos;
* confirmar testes;
* preparar implantação;
* organizar reversão;
* atualizar registros.

O Prompt de Release deve exigir autorização humana antes de produção.

---

## 69. Categorias adicionais

O DPF pode futuramente padronizar Prompts para:

* análise de impacto;
* descoberta;
* modelagem de regra;
* criação de Use Case;
* criação de Workflow;
* análise de segurança;
* revisão arquitetural;
* migração;
* correção de defeito;
* diagnóstico;
* auditoria documental;
* geração de Release Notes;
* atualização de Project State;
* análise de dívida técnica.

Toda nova categoria deve respeitar esta especificação.

---

# PARTE VII — DOCUMENTAÇÃO OFICIAL

## 70. Princípios documentais

A documentação oficial deve:

* possuir responsabilidade definida;
* evitar duplicação desnecessária;
* indicar sua versão;
* indicar seu estado;
* possuir responsável;
* ser atualizável;
* ser rastreável;
* relacionar artefatos associados;
* separar fato, decisão, hipótese e proposta.

Documentos não devem acumular responsabilidades incompatíveis.

---

## 71. PROJECT.md

Representa a identidade principal do Projeto.

Deve explicar:

* nome;
* propósito;
* problema;
* contexto;
* escopo;
* limites;
* responsáveis;
* usuários;
* visão resumida;
* Capabilities;
* estado;
* referências principais.

É a porta de entrada para compreensão do Projeto.

---

## 72. PRODUCT-VISION.md

Registra a visão do produto.

Deve apresentar:

* problema;
* público;
* proposta de valor;
* objetivos;
* diferenciais;
* resultados esperados;
* critérios de sucesso;
* princípios do produto;
* hipóteses relevantes;
* itens fora do escopo.

---

## 73. BUSINESS-RULES.md

É o catálogo oficial de Business Rules.

Cada regra deve possuir:

* identificação;
* descrição;
* origem;
* estado;
* responsável;
* condições;
* exceções;
* artefatos relacionados;
* histórico de mudança.

Regras obsoletas devem ser preservadas no histórico, mas marcadas como não vigentes.

---

## 74. SYSTEM-DESIGN.md

Descreve o desenho técnico vigente do sistema.

Deve cobrir, conforme aplicável:

* visão arquitetural;
* componentes;
* responsabilidades;
* fronteiras;
* fluxos;
* integrações;
* requisitos não funcionais;
* restrições;
* segurança;
* observabilidade;
* escalabilidade;
* decisões relacionadas.

Não deve substituir as Architecture Decisions.

---

## 75. FEATURE.md

Representa a especificação de uma Feature.

Deve apresentar:

* identificação;
* Epic;
* objetivo;
* valor;
* atores;
* comportamento;
* fluxo principal;
* alternativas;
* regras;
* critérios de aceitação;
* dependências;
* impactos;
* riscos;
* estado;
* Tasks relacionadas.

Cada Feature deve possuir uma referência oficial inequívoca.

---

## 76. TASKS.md

Representa o controle das Tasks de uma Feature, Epic, Sprint ou unidade definida.

Deve permitir compreender:

* Task;
* objetivo;
* responsável;
* estado;
* dependências;
* prioridade;
* critérios;
* resultado;
* evidências;
* vínculo hierárquico.

Em projetos maiores, as Tasks podem ser distribuídas em registros individuais, desde que a visão consolidada seja preservada.

---

## 77. API.md

Registra contratos e comportamentos de interfaces de integração.

Pode abranger:

* operações;
* entradas;
* saídas;
* autenticação;
* autorização;
* erros;
* versionamento;
* compatibilidade;
* limites;
* eventos;
* exemplos conceituais;
* dependências.

Mudanças incompatíveis devem ser explicitamente identificadas.

---

## 78. DATABASE.md

Registra o modelo de dados relevante.

Deve explicar:

* entidades;
* relacionamentos;
* responsabilidades;
* integridade;
* restrições;
* ciclo de vida dos dados;
* retenção;
* privacidade;
* migrações relevantes;
* decisões relacionadas.

Não deve ser apenas uma reprodução automática do esquema.

---

## 79. TESTS.md

Define a estratégia de testes.

Pode incluir:

* níveis de teste;
* responsabilidades;
* ambientes;
* dados;
* critérios de cobertura;
* critérios de aprovação;
* riscos;
* automação;
* regressão;
* evidências;
* tratamento de falhas.

---

## 80. CHANGELOG.md

Registra as mudanças relevantes ao longo das versões e Releases.

Deve distinguir:

* adições;
* alterações;
* correções;
* remoções;
* mudanças incompatíveis;
* segurança;
* documentação.

---

## 81. IMPLEMENTED.md

Apresenta os elementos implementados e sua situação.

Deve permitir localizar:

* Capabilities disponíveis;
* Epics concluídas;
* Features implementadas;
* Releases associadas;
* limitações;
* pendências conhecidas.

Não deve declarar como implementado algo ainda não validado conforme a Definition of Done.

---

## 82. PLANNED.md

Apresenta elementos formalmente planejados, mas ainda não implementados.

Deve distinguir:

* ideia;
* candidato;
* priorizado;
* Ready;
* programado;
* bloqueado.

A presença de um item em PLANNED não representa garantia de entrega.

---

## 83. CURRENT-SPRINT.md

Quando o Projeto utilizar Sprint, este documento representa o compromisso e o estado da Sprint atual.

Deve conter:

* objetivo;
* período;
* itens;
* responsáveis;
* dependências;
* bloqueios;
* alterações de escopo;
* resultado.

Projetos sem Sprint podem não utilizar este documento.

---

## 84. DECISIONS.md

Funciona como índice das Architecture Decisions e de outras decisões relevantes.

Deve apresentar:

* identificação;
* título;
* status;
* data;
* responsável;
* escopo;
* decisão substituída, quando houver;
* artefatos afetados.

Decisões complexas devem possuir registros detalhados próprios.

---

## 85. ROADMAP.md

Representa a evolução planejada do Projeto.

Deve priorizar resultados, Capabilities, Epics e Milestones.

Não deve ser reduzido a uma lista de Tasks.

---

## 86. Documentos complementares

Projetos podem adotar documentos adicionais, como:

* SECURITY.md;
* DEPLOYMENT.md;
* OPERATIONS.md;
* INTEGRATIONS.md;
* RISKS.md;
* TECHNICAL-DEBT.md;
* RELEASES.md;
* USE-CASES.md;
* WORKFLOWS.md;
* GLOSSARY.md;
* COMPLIANCE.md;
* OBSERVABILITY.md;
* MIGRATIONS.md.

A adoção depende do porte, risco e natureza do Projeto.

---

# PARTE VIII — WORKFLOW OFICIAL

## 87. Fluxo principal

O fluxo oficial do DPF é:

**Ideia**

↓

**Projeto**

↓

**Capability**

↓

**Epic**

↓

**Feature**

↓

**Task**

↓

**Implementação**

↓

**Review**

↓

**Testes**

↓

**Release**

↓

**Produção**

Cada etapa reduz incerteza e aumenta o nível de compromisso.

---

## 88. Ideia

Uma Ideia representa uma possibilidade ainda não comprometida.

Ela pode originar-se de:

* usuário;
* negócio;
* operação;
* inovação;
* problema técnico;
* requisito regulatório;
* oportunidade;
* feedback.

Uma Ideia não autoriza implementação.

Primeiro deve ser analisada, rejeitada, mantida em descoberta ou transformada em um elemento formal.

---

## 89. Projeto

Quando uma iniciativa possui visão, responsabilidade e continuidade próprias, ela pode ser formalizada como Projeto.

A criação de Projeto exige aprovação humana.

---

## 90. Capability

A visão do Projeto é decomposta em Capabilities.

Nesta etapa devem ser definidos:

* capacidade esperada;
* valor;
* limites;
* dependências;
* relação com objetivos.

---

## 91. Epic

Uma Capability é dividida em Epics.

A Epic deve estabelecer um resultado relevante e critérios de conclusão.

Ela não deve ser apenas um agrupamento arbitrário.

---

## 92. Feature

A Epic é decomposta em Features.

Nesta etapa deve ocorrer a especificação funcional suficiente para validação e posterior execução.

Uma Feature não deve avançar enquanto possuir dúvidas críticas sobre comportamento ou regra.

---

## 93. Task

A Feature é decomposta em Tasks.

Cada Task deve ser atribuível, testável e limitada.

Antes da execução, deve atender à Definition of Ready.

---

## 94. Implementação

A implementação deve seguir a Task aprovada.

O executor deve:

1. carregar o contexto necessário;
2. verificar restrições;
3. identificar artefatos permitidos;
4. executar apenas o escopo;
5. testar progressivamente;
6. registrar divergências;
7. interromper diante de decisão não autorizada;
8. atualizar evidências.

---

## 95. Review

Review é a verificação independente da alteração.

Deve avaliar:

* aderência à Task;
* atendimento da Feature;
* respeito às Business Rules;
* conformidade arquitetural;
* qualidade;
* segurança;
* impacto;
* testes;
* ausência de alterações indevidas;
* documentação.

Review pode ser realizada por humano, Agent ou ambos.

Alterações críticas devem possuir revisão humana.

---

## 96. Testes

Os testes devem comprovar que o comportamento esperado foi atendido e que comportamentos existentes não foram indevidamente quebrados.

A estratégia deve considerar:

* fluxo principal;
* exceções;
* limites;
* regressão;
* segurança;
* integração;
* desempenho, quando relevante;
* experiência do usuário.

---

## 97. Release

Itens aprovados são agrupados em Release.

Antes da liberação devem ser verificados:

* conteúdo;
* compatibilidade;
* riscos;
* evidências;
* documentação;
* migrações;
* observabilidade;
* implantação;
* reversão;
* comunicação.

---

## 98. Produção

Produção representa a disponibilização real do incremento.

A implantação deve ser:

* autorizada;
* observável;
* rastreável;
* reversível quando aplicável;
* registrada.

Após a implantação, o estado dos itens deve ser atualizado.

Incidentes ou divergências devem alimentar novas Tasks, Features, dívidas ou decisões.

---

## 99. Fluxos de retorno

O workflow não é estritamente linear.

Um item pode retornar quando:

* requisitos estão incompletos;
* critérios falham;
* review identifica problema;
* testes falham;
* risco é descoberto;
* decisão se torna necessária;
* dependência muda;
* produção apresenta incidente.

Retornos devem ser registrados.

---

# PARTE IX — GOVERNANÇA

## 100. Princípio de governança

Todo artefato deve possuir:

* autor;
* responsável;
* aprovador, quando necessário;
* histórico;
* estado;
* escopo de alteração.

A governança deve separar:

* criação;
* análise;
* aprovação;
* execução;
* revisão;
* liberação.

---

## 101. Criação de artefatos

Humans e Agents podem criar propostas.

A criação por Agent não equivale a aprovação.

Artefatos que contenham decisões de negócio, arquitetura, segurança, prioridade ou liberação devem possuir aprovação humana.

---

## 102. Aprovação

A aprovação deve ser realizada por pessoa com autoridade adequada ao tipo de artefato.

Exemplos:

* visão: responsável pelo produto;
* regra de negócio: responsável pelo negócio;
* decisão arquitetural: responsável técnico;
* controle de segurança: responsável de segurança ou técnico autorizado;
* Release: responsável pela liberação;
* mudança de prioridade: responsável por produto ou gestão.

---

## 103. Alteração

Nenhum artefato aprovado deve ser alterado silenciosamente.

A alteração deve:

* preservar histórico;
* indicar autor;
* indicar motivo;
* avaliar impacto;
* atualizar versão;
* obter nova aprovação quando modificar significado.

Agents podem preparar alterações, mas não devem assumir aprovação implícita.

---

## 104. Implementação

A implementação pode ser realizada por:

* desenvolvedor humano;
* Agent especializado;
* combinação de ambos.

O executor deve trabalhar dentro da Task.

Quando o executor humano utilizar um Agent auxiliar, as mesmas regras de escopo permanecem aplicáveis.

---

## 105. Revisão

A revisão deve ser realizada por responsável diferente do executor sempre que o risco justificar.

Pode envolver:

* revisão técnica;
* revisão funcional;
* revisão de segurança;
* revisão de dados;
* revisão de experiência;
* revisão documental.

---

## 106. Matriz conceitual de responsabilidade

### Projeto e visão

* Criação: humano ou Agent sob orientação.
* Aprovação: humano responsável pelo produto.
* Alteração: mediante análise e aprovação.
* Implementação: não aplicável diretamente.
* Revisão: produto, arquitetura e stakeholders.

### Capability

* Criação: produto, análise ou Agent.
* Aprovação: responsável pelo produto.
* Alteração: produto.
* Implementação: por meio de Epics e Features.
* Revisão: negócio e arquitetura.

### Epic

* Criação: produto, análise ou Agent.
* Aprovação: produto.
* Alteração: produto.
* Implementação: por meio de Features.
* Revisão: negócio, técnica e gestão.

### Feature

* Criação: análise, produto ou Agent.
* Aprovação: produto ou responsável funcional.
* Alteração: controlada.
* Implementação: por Tasks.
* Revisão: funcional, técnica e qualidade.

### Task

* Criação: liderança, desenvolvedor ou Agent.
* Aprovação: responsável técnico ou gestor do fluxo.
* Alteração: antes ou durante execução, com registro.
* Implementação: humano ou Agent.
* Revisão: técnico, QA ou especialista.

### Architecture Decision

* Criação: arquiteto, técnico ou Agent como proposta.
* Aprovação: humano responsável pela arquitetura.
* Alteração: nova decisão ou substituição formal.
* Implementação: por Tasks.
* Revisão: arquitetura, segurança e operação.

### Release

* Criação: equipe técnica, gestão ou Agent.
* Aprovação: humano autorizado.
* Implementação: automação, DevOps ou equipe.
* Revisão: técnica, QA, segurança e operação.

---

# PARTE X — REGRAS DE ATUAÇÃO DA IA

## 107. Princípio de não criação de regra

Uma IA NÃO DEVE criar Business Rules.

Quando uma regra estiver ausente, ambígua ou contraditória, o Agent deve:

1. identificar a lacuna;
2. explicar o impacto;
3. apresentar perguntas;
4. aguardar decisão;
5. registrar a resposta aprovada.

O Agent pode propor opções, mas deve marcá-las como propostas.

---

## 108. Princípio de não invenção arquitetural

Uma IA NÃO DEVE inventar arquitetura quando já existir uma arquitetura vigente.

Quando a arquitetura não estiver definida, o Agent pode produzir alternativas e análise.

A seleção exige decisão humana.

---

## 109. Princípio de preservação de decisões

Uma IA NÃO DEVE modificar, ignorar ou contornar uma Architecture Decision vigente.

Caso considere a decisão inadequada, deve:

* registrar a preocupação;
* apresentar evidências;
* propor revisão;
* aguardar aprovação.

---

## 110. Princípio de escopo da Task

Toda implementação de IA deve ocorrer dentro do escopo de uma Task.

A Task deve declarar:

* objetivo;
* áreas permitidas;
* comportamentos preservados;
* critérios;
* restrições;
* condição de conclusão.

O Agent deve interromper a execução quando o resultado depender de alteração fora do escopo.

---

## 111. Princípio de consulta contextual

Antes de implementar, a IA deve consultar os documentos relevantes.

A consulta mínima depende da Task, mas pode incluir:

* Project State;
* Feature;
* Business Rules;
* Architecture Decisions;
* System Design;
* contratos;
* dados;
* testes;
* padrões;
* histórico relacionado.

---

## 112. Princípio de transparência

Agents devem informar:

* o que alteraram;
* quais documentos utilizaram;
* quais suposições foram evitadas;
* quais testes executaram;
* quais limitações encontraram;
* quais riscos permaneceram;
* quais pontos exigem decisão humana.

---

## 113. Princípio de interrupção segura

Um Agent deve parar ou limitar sua atuação quando:

* faltarem regras essenciais;
* houver conflito documental;
* uma decisão arquitetural for necessária;
* o escopo estiver indefinido;
* a ação puder causar perda de dados;
* forem exigidas credenciais não autorizadas;
* houver risco de segurança;
* a ação envolver produção sem aprovação;
* os critérios de aceitação forem impossíveis de verificar.

---

## 114. Ações proibidas para Agents

Agents NÃO DEVEM:

* inventar requisito;
* criar regra como fato;
* ampliar escopo;
* alterar arquitetura por conveniência;
* modificar produção sem autorização;
* ocultar falhas;
* declarar teste não executado como aprovado;
* remover evidências;
* alterar documentação para encobrir divergência;
* incluir tecnologia não aprovada;
* expor credenciais;
* eliminar dados sem autorização;
* ignorar dependências;
* concluir item sem atender à Definition of Done;
* assumir papel humano de aprovação.

---

# PARTE XI — ESTADOS E CONTROLE DE EXECUÇÃO

## 115. Estados de uma Capability

Uma Capability pode possuir estados como:

* proposta;
* aprovada;
* planejada;
* em evolução;
* parcialmente disponível;
* disponível;
* suspensa;
* descontinuada.

---

## 116. Estados de uma Epic

Uma Epic pode possuir estados como:

* proposta;
* descoberta;
* planejada;
* pronta;
* em andamento;
* bloqueada;
* em validação;
* concluída;
* cancelada.

---

## 117. Estados de uma Feature

Uma Feature pode possuir estados como:

* ideia;
* análise;
* especificação;
* aguardando aprovação;
* planejada;
* Ready;
* em implementação;
* em review;
* em testes;
* aprovada;
* incluída em Release;
* implantada;
* bloqueada;
* cancelada;
* substituída.

---

## 118. Estados de uma Task

Uma Task pode possuir estados como:

* proposta;
* pendente de refinamento;
* Ready;
* atribuída;
* em andamento;
* bloqueada;
* em review;
* em correção;
* em testes;
* Done;
* cancelada.

As transições devem refletir acontecimentos reais.

---

# PARTE XII — QUALIDADE E CONFORMIDADE

## 119. Conformidade com o DPF

Um Projeto é considerado aderente ao DPF quando:

* utiliza a hierarquia oficial;
* mantém documentação como referência;
* possui Project State;
* limita a atuação de Agents;
* registra regras;
* registra decisões;
* utiliza Tasks para execução;
* aplica Definition of Ready;
* aplica Definition of Done;
* preserva rastreabilidade;
* possui governança humana;
* registra mudanças relevantes.

---

## 120. Níveis de adoção

O DPF poderá, em versão futura, definir níveis formais de maturidade.

Até que isso ocorra, recomenda-se distinguir:

### Adoção essencial

* Projeto;
* Features;
* Tasks;
* regras;
* decisões;
* Project State;
* DoR;
* DoD;
* Change Log.

### Adoção intermediária

* Capabilities;
* Epics;
* Roadmap;
* agentes especializados;
* estratégia de testes;
* documentação arquitetural;
* Releases formais.

### Adoção avançada

* auditoria automatizada;
* governança completa de Agents;
* métricas;
* rastreabilidade integral;
* controles de segurança;
* conformidade documental automatizada;
* políticas de execução por risco.

Esses níveis são orientativos nesta versão.

---

## 121. Proporcionalidade

A profundidade documental deve ser proporcional a:

* risco;
* complexidade;
* duração;
* número de participantes;
* criticidade;
* impacto financeiro;
* sensibilidade dos dados;
* dependências externas;
* requisitos regulatórios;
* quantidade de Agents.

Um micro-SaaS não precisa produzir o mesmo volume documental de uma plataforma crítica.

Entretanto, ambos devem preservar os princípios fundamentais.

---

## 122. Métricas recomendadas

Projetos podem medir:

* percentual de Tasks com contexto completo;
* percentual de Features rastreáveis;
* divergências entre código e documentação;
* alterações fora de escopo;
* retrabalho causado por ambiguidade;
* Tasks bloqueadas por ausência de decisão;
* defeitos encontrados em review;
* defeitos encontrados em produção;
* atualizações pendentes no Project State;
* dívida técnica criada por Release;
* tempo entre mudança e atualização documental;
* intervenções humanas necessárias em execução de Agents.

As métricas devem apoiar melhoria, não produzir burocracia artificial.

---

# PARTE XIII — MUDANÇA E EVOLUÇÃO DO FRAMEWORK

## 123. Evolução da especificação

O DPF deve evoluir de maneira controlada.

Alterações nesta especificação devem:

* possuir justificativa;
* identificar problema;
* avaliar compatibilidade;
* indicar impacto;
* preservar histórico;
* receber aprovação da governança da DoisTech;
* resultar em nova versão.

---

## 124. Compatibilidade

Mudanças que alterem o significado de conceitos fundamentais devem gerar nova versão principal.

Mudanças que adicionem detalhes compatíveis podem gerar versão secundária.

Correções editoriais podem gerar versão de correção.

---

## 125. Extensões

Organizações ou projetos podem criar extensões do DPF.

Uma extensão:

* não deve contradizer os princípios fundamentais;
* deve identificar claramente o que adiciona;
* não deve redefinir termos oficiais;
* deve preservar a hierarquia;
* deve registrar suas regras adicionais;
* deve informar compatibilidade com a versão do DPF.

---

# PARTE XIV — PRINCÍPIOS CONSTITUCIONAIS

## 126. Constituição do DPF

Os seguintes princípios possuem caráter constitucional:

1. O desenvolvimento nasce da especificação.
2. A documentação representa a intenção oficial do Projeto.
3. O contexto precede a execução.
4. Toda implementação ocorre dentro de escopo definido.
5. A IA não cria regras de negócio.
6. A IA não possui autoridade implícita.
7. Decisões arquiteturais exigem governança.
8. O Projeto é dividido em unidades hierárquicas.
9. Toda mudança relevante deve ser rastreável.
10. A responsabilidade final permanece humana.
11. Agentes devem operar por papéis especializados.
12. Nenhum item está concluído sem atender à Definition of Done.
13. Nenhum item deve iniciar sem atender à Definition of Ready.
14. A documentação deve evoluir junto com o produto.
15. O Project State deve representar a realidade atual.
16. Divergências devem ser expostas, nunca ocultadas.
17. Mudanças devem ser proporcionais ao escopo da Task.
18. A execução deve ser incremental e verificável.
19. O framework deve permanecer independente de tecnologia.
20. Ferramentas futuras devem obedecer a esta especificação.

---

# PARTE XV — MODELO OPERACIONAL RESUMIDO

## 127. Antes do desenvolvimento

Antes da implementação:

* a necessidade é analisada;
* a hierarquia é identificada;
* regras são localizadas;
* contexto é reunido;
* decisões são verificadas;
* a Feature é especificada;
* Tasks são criadas;
* a DoR é validada;
* o executor é definido.

---

## 128. Durante o desenvolvimento

Durante a implementação:

* o executor atua apenas na Task;
* decisões vigentes são preservadas;
* alterações desnecessárias são evitadas;
* testes são realizados;
* riscos são registrados;
* dúvidas são escaladas;
* evidências são produzidas.

---

## 129. Depois do desenvolvimento

Após a implementação:

* ocorre review;
* testes são concluídos;
* critérios são verificados;
* documentação é atualizada;
* Project State é atualizado;
* Change Log é atualizado;
* a DoD é validada;
* o item pode compor uma Release.

---

# PARTE XVI — EXEMPLO CONCEITUAL COMPLETO

## 130. Projeto

**Projeto:** Plataforma de Gestão de Serviços

Objetivo: permitir que organizações administrem seus serviços, clientes, agendas e comunicações.

---

## 131. Capability

**Capability:** Gestão de Agendamentos

Responsabilidade: permitir criação, consulta, reserva, alteração e cancelamento de horários.

---

## 132. Epic

**Epic:** Autoagendamento pelo cliente

Resultado esperado: clientes conseguem reservar horários sem intervenção manual da organização.

---

## 133. Feature

**Feature:** Consulta de horários disponíveis

Comportamento esperado: o cliente informa serviço, profissional e período e recebe apenas horários válidos.

---

## 134. Business Rules relacionadas

* horários ocupados não podem ser exibidos;
* bloqueios de agenda devem ser respeitados;
* a duração do serviço deve ser considerada;
* horários fora do expediente não podem ser reservados;
* o fuso horário configurado deve ser respeitado.

Essas regras devem ser definidas pelo negócio, não pelo Agent.

---

## 135. Tasks

* implementar cálculo de disponibilidade;
* disponibilizar operação de consulta;
* criar interface de seleção;
* tratar ausência de horários;
* criar testes das regras;
* atualizar documentação;
* validar segurança e desempenho.

Cada Task possui escopo, responsável e critérios próprios.

---

## 136. Execução por Agents

* Business Analyst Agent organiza fluxos e critérios.
* Architect Agent verifica impacto.
* Humano aprova regras e decisões.
* Backend Agent implementa a consulta.
* Frontend Agent implementa a interface.
* QA Agent valida cenários.
* Security Agent verifica exposição de dados.
* Documentation Agent atualiza os registros.
* Humano autoriza a Release.

Esse exemplo demonstra que o DPF organiza a colaboração sem transferir autoridade decisória para a IA.

---

# PARTE XVII — CRITÉRIOS DE VALIDADE DOS ARTEFATOS

## 137. Artefato válido

Um artefato oficial é considerado válido quando:

* possui propósito claro;
* utiliza terminologia oficial;
* possui responsável;
* possui estado;
* possui versão quando necessário;
* está relacionado à hierarquia;
* não contradiz uma decisão vigente;
* distingue fatos de propostas;
* pode ser compreendido sem depender de memória informal;
* foi aprovado quando exigido.

---

## 138. Artefato inválido

Um artefato deve ser revisado quando:

* possui escopo ambíguo;
* mistura Feature e Task;
* contém regra inventada;
* contradiz documentação vigente;
* não identifica responsável;
* não possui critérios;
* depende de contexto ausente;
* declara conclusão sem evidência;
* usa termos inconsistentes;
* foi alterado sem histórico.

---

# PARTE XVIII — DISPOSIÇÕES FINAIS

## 139. Independência tecnológica

Nenhuma regra desta especificação exige:

* Java;
* JavaScript;
* Python;
* banco relacional;
* microsserviços;
* monólito;
* cloud;
* container;
* ferramenta de gestão específica;
* fornecedor específico de IA.

O DPF regula o processo de engenharia, não a tecnologia escolhida.

---

## 140. Aplicabilidade

O DPF pode ser aplicado a:

* APIs;
* sistemas corporativos;
* aplicativos mobile;
* PWAs;
* plataformas SaaS;
* microsserviços;
* monólitos;
* integrações;
* automações;
* produtos internos;
* produtos comerciais;
* sistemas legados;
* novos produtos;
* modernizações;
* provas de conceito controladas.

---

## 141. Autoridade desta especificação

A DPF Specification v1.0 constitui a base normativa para as fases seguintes do framework.

As próximas fases poderão materializar:

* templates;
* estruturas documentais;
* convenções de identificação;
* biblioteca de prompts;
* definição operacional dos Agents;
* CLI;
* dashboard;
* plugins;
* automações;
* validadores;
* mecanismos de auditoria;
* integração com ferramentas de desenvolvimento.

Essas implementações devem refletir esta especificação e não redefini-la silenciosamente.

---

## 142. Declaração final

O DoisTech Project Framework estabelece que a velocidade proporcionada por agentes de Inteligência Artificial somente produz valor sustentável quando acompanhada de contexto, especificação, limites, rastreabilidade e governança.

No DPF, a IA não substitui a engenharia de software.

A IA amplia a capacidade de execução de uma engenharia organizada.

A especificação define a intenção.

A documentação preserva o contexto.

A hierarquia organiza o produto.

A Task limita a execução.

Os testes verificam o resultado.

A governança preserva a responsabilidade.

O Project State mantém a continuidade.

Esses elementos constituem a base oficial do DoisTech Project Framework.

---

**Fim da DPF Specification v1.0**
