# EXECUTE-TASK

## Título

Executar Task

## Papel do agente

Backend Agent, Frontend Agent, Mobile Agent, DevOps Agent, Database Agent ou Documentation Agent, conforme a Task

## Objetivo

Executar uma Task aprovada dentro do escopo autorizado, com evidências e documentação sincronizada.

## Contexto esperado

Task válida, Feature relacionada e documentos necessários acessíveis.

## Documentos obrigatórios para leitura

- `PROJECT-STATE.md`
- `FEATURE.md`
- `TASKS.md`
- arquivo individual da Task, quando existir
- `BUSINESS-RULES.md`, quando aplicável
- ADRs relacionadas
- documentos técnicos afetados

## Entradas necessárias

- ID da Task
- ID da Feature
- estado atual
- artefatos permitidos

## Escopo permitido

- somente arquivos e áreas explicitamente autorizados pela Task e pelo contrato de execução

## Restrições

- não implementar outra Task
- não antecipar Feature futura
- não modificar critérios de aceite
- não mascarar testes falhando
- não fazer commit automático
- não fazer push automático

## Procedimento de execução

1. confirmar Task e Feature;
2. inspecionar documentos relacionados;
3. verificar dependências e estado permitido;
4. registrar plano curto de execução;
5. alterar somente o escopo autorizado;
6. executar testes adequados;
7. atualizar status e rastreabilidade;
8. atualizar documentação impactada;
9. emitir relatório com evidências.

## Validações obrigatórias

- DoR atendida
- testes compatíveis com o risco
- documentação sincronizada
- ausência de alteração fora do escopo

## Critérios de conclusão

- objetivo da Task atendido
- critérios relevantes validados
- evidências produzidas
- pendências e falhas reportadas

## Formato do relatório final

- objetivo
- contexto consultado
- plano executado
- arquivos alterados
- testes executados
- resultados
- evidências
- riscos
- limitações
- recomendação de estado

## Política de Git

Não fazer commit ou push sem autorização explícita.

## Tratamento de inconsistências

Parar e escalar para decisão humana em caso de:

- regra ausente
- necessidade de ADR
- conflito documental crítico
- risco de segurança
- risco de perda de dados

## Tratamento de informação ausente

Bloquear execução quando a ausência impedir validação segura do resultado.
