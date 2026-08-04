# AI Agent Integration Guide

## Objetivo

Orientar agentes de IA a usar o DPF com validação, revisão e handoff compatíveis com a automação oficial.

## Fluxo mínimo esperado

Antes de modificar:

1. ler `README.md`, `AGENTS.md` e documentos diretamente relacionados;
2. executar `./dpf validate <projeto>` quando o contexto justificar;
3. identificar erros já existentes antes de alterar o projeto.

Após modificar:

1. executar `./dpf validate <projeto>`;
2. executar testes relevantes;
3. revisar diff e documentos impactados;
4. registrar riscos, limitações e validações executadas.

## Entrega esperada do agente

O agente DEVE informar:

- arquivos alterados;
- comandos executados;
- resultado das validações;
- pendências;
- conflitos documentais detectados.

## Handoff

Em transição entre agentes:

- apontar artefatos lidos;
- apontar artefatos modificados;
- registrar estado atual da validação;
- registrar decisões e suposições ainda abertas.

## Restrições

O agente NÃO DEVE:

- fazer push automaticamente;
- aprovar PR;
- usar segredos;
- publicar release;
- alterar proteção de branch;
- ignorar falhas do quality gate sem registrar o motivo.
