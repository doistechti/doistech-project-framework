# Biblioteca Oficial de Prompts Operacionais do DPF

## Finalidade

Esta biblioteca reúne os prompts operacionais oficiais do DPF para uso controlado por agentes de IA em projetos aderentes ao framework.

## Categorias

- `project-initialization/`
- `product-discovery/`
- `architecture/`
- `feature-planning/`
- `task-planning/`
- `task-execution/`
- `code-review/`
- `validation/`
- `bug-fixing/`
- `documentation/`
- `change-management/`
- `release/`
- `maintenance/`
- `audit/`

## Ordem recomendada

1. inicialização ou avaliação do projeto
2. visão e arquitetura
3. planejamento de Feature
4. decomposição em Tasks
5. execução
6. revisão
7. validação
8. documentação
9. release
10. manutenção ou auditoria

## Níveis de autonomia

- `Nível A — Análise`
- `Nível B — Proposta`
- `Nível C — Execução controlada`
- `Nível D — Execução com Git autorizado`

Nenhum prompt presume autorização de nível D.

## Entradas esperadas

- `Project State`
- Task, quando houver alteração
- Feature relacionada
- regras de negócio
- decisões arquiteturais
- artefatos técnicos ou documentais relevantes

## Uso no Codex

1. localizar o prompt mais próximo da atividade;
2. confirmar contexto documental;
3. aplicar o prompt em conjunto com `PROMPT-BASE.md`;
4. respeitar o escopo e a política de Git;
5. produzir relatório final com evidências.

## Uso em outras ferramentas

Os prompts podem ser reutilizados em qualquer ferramenta de IA desde que:

- o conteúdo normativo seja preservado;
- a política de Git seja respeitada;
- a ferramenta não introduza autoridade implícita;
- o contexto do projeto DPF seja efetivamente fornecido.

## Adaptação

Adaptações locais PODEM ajustar forma e extensão, mas NÃO PODEM remover:

- leitura obrigatória;
- escopo;
- restrições;
- validações;
- critérios de conclusão;
- política de Git;
- tratamento de inconsistências.

## Riscos

- contexto incompleto;
- execução fora da Task;
- conflito entre documentação e implementação;
- refatoração oportunista;
- testes insuficientes;
- atualização documental incompleta.

## Exemplos de uso

- iniciar um projeto DPF novo;
- avaliar um projeto existente;
- planejar uma Feature;
- executar uma Task;
- revisar uma alteração;
- preparar uma Release;
- retomar trabalho interrompido;
- auditar conformidade DPF.
