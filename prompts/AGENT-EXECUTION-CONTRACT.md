# Agent Execution Contract

## Finalidade

Autorização formal para uma execução de agente.

## Campos obrigatórios

- `contract_id`
- `prompt_id`
- `agent_profile`
- `activity`
- `project_id`
- `capability_id`
- `epic_id`
- `feature_id`
- `task_id`
- `authorized_context`
- `permitted_artifacts`
- `protected_artifacts`
- `allowed_actions`
- `forbidden_actions`
- `authorized_environments`
- `autonomy_level`
- `stop_conditions`
- `completion_criteria`
- `approver`
- `valid_from`
- `valid_until`
- `result_status`
- `evidence_refs`

## Exemplo não normativo

```yaml
contract_id: AEC-CORE-0001
prompt_id: PRM-IMP-UNI-001
agent_profile: backend-agent
activity: implementar task autorizada
project_id: PRJ-CORE-0001
capability_id: CAP-CORE-0001
epic_id: EPC-CORE-0002
feature_id: FEAT-CORE-0012
task_id: TASK-CORE-0045
autonomy_level: 3
approver: engineering-lead
result_status: pending
```
