# Scripts

Este diretório está reservado para futuras ferramentas e automações do
DoisTech Project Framework.

Na Fase 8, o primeiro software oficial do repositório foi implementado como
pacote Python em `dpf_validator/`, e não neste diretório. A decisão evita
misturar código executável do validador com scripts auxiliares ainda não
padronizados.

Recursos disponíveis a partir da Fase 10:

- `scripts/automation/run_quality_gate.py`: runner local reutilizável para CI/CD e execução manual.

Possíveis recursos futuros:

- inicialização de projetos DPF;
- validação da estrutura de diretórios;
- validação de documentos;
- geração de identificadores;
- verificação de referências;
- atualização de mapas de Features e Tasks;
- preparação de releases;
- auditoria de consistência documental.

## Restrição atual

Scripts auxiliares DEVEM reutilizar a CLI e o validador oficiais.

Scripts não DEVEM duplicar regras documentais já implementadas no núcleo oficial.
