# ASSESS-EXISTING-PROJECT

## Título

Avaliar projeto existente para adoção do DPF

## Papel do agente

Legacy Analysis Agent, Architect Agent ou Documentation Agent

## Objetivo

Inspecionar um projeto existente, identificar aderência parcial ao DPF e propor adoção progressiva.

## Contexto esperado

Repositório com histórico prévio, documentação parcial ou código sem estrutura DPF.

## Documentos obrigatórios para leitura

- `README.md`
- `AGENTS.md`
- especificações do DPF
- exemplos da Fase 5

## Entradas necessárias

- estado atual do repositório
- objetivo da adoção
- área prioritária

## Escopo permitido

- análise
- relatório
- proposta documental

## Restrições

- não reestruturar sem autorização
- não assumir que o código reflete a regra oficial

## Procedimento de execução

1. mapear documentação existente;
2. mapear contexto funcional e técnico aparente;
3. identificar lacunas críticas;
4. classificar aderência mínima;
5. propor sequência incremental.

## Validações obrigatórias

- presença ou ausência de `Project State`
- presença de Features e Tasks rastreáveis
- divergências entre documentação e implementação

## Critérios de conclusão

- diagnóstico emitido
- riscos e hipóteses separados
- passos de adoção sugeridos

## Formato do relatório final

- estado atual
- aderência
- lacunas
- riscos
- plano incremental

## Política de Git

Somente leitura, salvo autorização explícita para ajustes documentais.

## Tratamento de inconsistências

Marcar como hipótese ou conflito; não reinterpretar silenciosamente.

## Tratamento de informação ausente

Registrar explicitamente como ausência documental ou hipótese de legado.
