# INIT-DPF-PROJECT

## Título

Inicializar projeto DPF

## Papel do agente

Business Analyst Agent ou Documentation Agent

## Objetivo

Criar a estrutura documental inicial de um projeto aderente ao DPF sem implementar produto.

## Contexto esperado

Projeto novo ou repositório sem estrutura DPF formal.

## Documentos obrigatórios para leitura

- `README.md`
- `AGENTS.md`
- `docs/specification/DPF-SPECIFICATION-v1.0.md`
- `docs/architecture/DPF-PROJECT-STRUCTURE.md`
- `docs/specification/DPF-AGENT-AND-PROMPT-SPECIFICATION-v1.0.md`

## Entradas necessárias

- nome do projeto
- objetivo inicial
- perfil de porte
- escopo inicial

## Escopo permitido

- estrutura documental
- manifesto do projeto
- artefatos iniciais do diretório `dpf/`

## Restrições

- não implementar código
- não escolher tecnologia sem decisão formal
- não criar regra de negócio nova

## Procedimento de execução

1. inspecionar o repositório atual;
2. verificar se já existe estrutura DPF;
3. criar ou completar `dpf/` conforme especificação;
4. registrar estado inicial e documentos de entrada;
5. apontar ausências e dependências.

## Validações obrigatórias

- presença de `PROJECT.md`
- presença de `PROJECT-STATE.md`
- coerência do `dpf-project.yaml`

## Critérios de conclusão

- estrutura inicial criada ou proposta
- contexto inicial registrado
- riscos e ausências informados

## Formato do relatório final

- artefatos criados
- artefatos não criados e motivo
- lacunas
- recomendação de próximos passos

## Política de Git

Não fazer commit nem push sem autorização explícita.

## Tratamento de inconsistências

Registrar divergências entre estrutura real e estrutura DPF esperada.

## Tratamento de informação ausente

Declarar ausências e impedir inferências normativas não autorizadas.
