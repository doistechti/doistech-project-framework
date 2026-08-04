from __future__ import annotations

from pathlib import Path
from textwrap import dedent


TEMPLATES_ROOT = Path(__file__).resolve().parent.parent / "templates"


def _read_template_block(relative_path: str) -> str:
    content = (TEMPLATES_ROOT / relative_path).read_text(encoding="utf-8")
    marker = "```md\n"
    start = content.find(marker)
    if start == -1:
        raise ValueError(f"Template sem bloco markdown utilizável: {relative_path}")
    start += len(marker)
    end = content.find("\n```", start)
    if end == -1:
        raise ValueError(f"Template sem fechamento de bloco markdown: {relative_path}")
    return content[start:end].strip() + "\n"


def _render(relative_path: str, replacements: dict[str, str]) -> str:
    rendered = _read_template_block(relative_path)
    for source, target in replacements.items():
        rendered = rendered.replace(source, target)
    return rendered


def root_readme(project_name: str) -> str:
    return dedent(
        f"""\
        # {project_name}

        Projeto estruturado com o DoisTech Project Framework.

        ## Leitura inicial

        - `AGENTS.md`
        - `dpf/PROJECT.md`
        - `dpf/PROJECT-STATE.md`
        """
    )


def root_agents() -> str:
    return dedent(
        """\
        # AGENTS.md

        ## Leitura obrigatória

        1. `README.md`
        2. `dpf/PROJECT.md`
        3. `dpf/PROJECT-STATE.md`
        4. artefatos diretamente relacionados à mudança

        ## Regras

        - não sobrescrever arquivos silenciosamente;
        - limitar alterações ao escopo solicitado;
        - preservar rastreabilidade;
        - validar o resultado antes de concluir a tarefa.
        """
    )


def root_gitignore() -> str:
    return dedent(
        """\
        .DS_Store
        Thumbs.db
        .idea/
        .vscode/
        *.log
        .env
        .env.*
        __pycache__/
        *.pyc
        build/
        dist/
        .cache/
        """
    )


def project_doc(project_id: str, project_name: str, owner: str, today: str) -> str:
    context = project_id.split("-", 2)[1]
    return _render(
        "project/PROJECT-TEMPLATE.md",
        {
            "PRJ-<CONTEXT>-<NNNN>": project_id,
            "<PROJECT NAME>": project_name,
            "<PROJECT TYPE>": "software-project",
            "<PROJECT CONTEXT>": context,
            "<OWNER>": owner,
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": today,
            "CAP-<CONTEXT>-<NNNN>": f"CAP-{context}-0001",
            "EPC-<CONTEXT>-<NNNN>": f"EPC-{context}-0001",
            "FEAT-<CONTEXT>-<NNNN>": f"FEAT-{context}-0001",
            "REL-<CONTEXT>-<NNNN>": f"REL-{context}-0001",
            "<EXECUTIVE SUMMARY>": "Projeto inicializado pela CLI oficial do DPF.",
            "<OBJECTIVE 1>": "estabelecer a base documental inicial do projeto;",
            "<OBJECTIVE 2>": "preparar o backlog rastreável do primeiro incremento;",
            "<IN-SCOPE ITEM 1>": "documentação inicial do projeto;",
            "<IN-SCOPE ITEM 2>": "estrutura metodológica e primeiros artefatos;",
            "<OUT-OF-SCOPE ITEM 1>": "decisões tecnológicas ainda não aprovadas;",
            "<OUT-OF-SCOPE ITEM 2>": "entregas de implementação não planejadas;",
            "<STAKEHOLDER 1>": owner,
            "<STAKEHOLDER 2>": "pending",
            "<CURRENT PROJECT STATE>": "Projeto inicializado e aguardando definição das primeiras Capabilities e Features.",
            "<RISK 1>": "escopo inicial ainda incompleto;",
            "<RISK 2>": "decisões arquiteturais ainda pendentes;",
            "<REFERENCE 1>": "`dpf/PROJECT-STATE.md`",
            "<REFERENCE 2>": "`dpf/product/PRODUCT-VISION.md`",
        },
    )


def project_state_doc(context: str, project_name: str, today: str) -> str:
    return _render(
        "project/PROJECT-STATE-TEMPLATE.md",
        {
            "DOC-<CONTEXT>-STATE-<NNNN>": f"DOC-{context}-STATE-0001",
            "<PROJECT NAME>": project_name,
            "<OWNER>": "documentation-owner",
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": today,
            "FEAT-<CONTEXT>-<NNNN>": f"FEAT-{context}-0001",
            "REL-<CONTEXT>-<NNNN>": f"REL-{context}-0001",
            "CAP-<CONTEXT>-<NNNN>": f"CAP-{context}-0001",
            "TASK-<CONTEXT>-<NNNN>": f"TASK-{context}-0001",
            "ADR-<CONTEXT>-<NNNN>": f"ADR-{context}-0001",
            "RISK-<CONTEXT>-<NNNN>": f"RISK-{context}-0001",
            "<GENERAL STATE>": "Projeto inicializado e aguardando definição das primeiras Capabilities e Features.",
            "<STATUS>": "draft",
            "<SUMMARY>": "primeiros riscos ainda não detalhados",
            "<slug>": "pending-decision",
        },
    )


def product_vision_doc(project_name: str, context: str = "GEN") -> str:
    return _render(
        "product/PRODUCT-VISION-TEMPLATE.md",
        {
            "DOC-<CONTEXT>-VISION-<NNNN>": f"DOC-{context}-VISION-0001",
            "<PROJECT NAME>": project_name,
            "<OWNER>": "product-owner",
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": "TBD-DATE",
            "FEAT-<CONTEXT>-<NNNN>": f"FEAT-{context}-0001",
            "<PRODUCT VISION>": f"Definir a visão do produto {project_name}.",
            "<PRODUCT OBJECTIVE>": "Definir.",
            "<PROBLEM TO SOLVE>": "Definir.",
            "<AUDIENCE 1>": "Definir.",
            "<AUDIENCE 2>": "Definir.",
            "<VALUE PROPOSITION>": "Definir.",
            "<NON-GOAL 1>": "Definir.",
            "<NON-GOAL 2>": "Definir.",
        },
    )


def system_design_doc(context: str = "GEN") -> str:
    return _render(
        "architecture/SYSTEM-DESIGN-TEMPLATE.md",
        {
            "<STRUCTURE ITEM 1>": "Definir.",
            "<STRUCTURE ITEM 2>": "Definir.",
            "<BOUNDARY 1>": "Não assumir tecnologia até decisão formal.",
            "<BOUNDARY 2>": "Preservar independência tecnológica.",
            "ADR-<CONTEXT>-<NNNN>": f"ADR-{context}-0001",
            "<IMPLEMENTATION OR DESIGN NOTE>": "Arquitetura ainda não detalhada.",
        },
    )


def planned_doc() -> str:
    return "# PLANNED.md\n\nNenhum item planejado registrado.\n"


def implemented_doc() -> str:
    return "# IMPLEMENTED.md\n\nNenhum item implementado registrado.\n"


def changelog_doc() -> str:
    return "# CHANGELOG.md\n\n## Não publicado\n\n### Adicionado\n\n- estrutura inicial do projeto DPF.\n"


def releases_index_doc(context: str = "GEN") -> str:
    return _render(
        "releases/RELEASES-INDEX-TEMPLATE.md",
        {
            "<RELEASE INDEX ENTRY>": "Nenhuma release registrada.",
        },
    )


def decisions_index_doc() -> str:
    return "# DECISIONS.md\n\nNenhuma decisão registrada.\n"


def agent_context_doc() -> str:
    return _read_template_block("context/AGENT-CONTEXT-TEMPLATE.md")


def tests_doc() -> str:
    return "# TESTS.md\n\nEstratégia de testes ainda não detalhada.\n"


def capability_doc(cap_id: str, title: str, today: str) -> str:
    return dedent(
        f"""\
        ---
        id: {cap_id}
        title: {title}
        type: capability
        status: active
        version: 1.0
        owner: pending
        author: dpf-cli
        approver: pending
        created_at: {today}
        updated_at: {today}
        ---

        # CAPABILITY.md

        ## Objetivo

        Definir.
        """
    )


def epics_index_doc() -> str:
    return "# EPICS.md\n\nNenhuma Epic registrada.\n"


def epic_doc(epic_id: str, title: str, capability_id: str, today: str) -> str:
    return dedent(
        f"""\
        ---
        id: {epic_id}
        title: {title}
        type: epic
        status: active
        version: 1.0
        owner: pending
        author: dpf-cli
        approver: pending
        created_at: {today}
        updated_at: {today}
        parent: {capability_id}
        ---

        # EPIC.md

        ## Resultado esperado

        Definir.
        """
    )


def features_index_doc() -> str:
    return "# FEATURES.md\n\nNenhuma Feature registrada.\n"


def feature_doc(feature_id: str, title: str, epic_id: str, today: str) -> str:
    context = feature_id.split("-", 2)[1]
    return _render(
        "features/FEATURE-TEMPLATE.md",
        {
            "FEAT-<CONTEXT>-<NNNN>": feature_id,
            "<FEATURE TITLE>": title,
            "<OWNER>": "pending",
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": today,
            "EPC-<CONTEXT>-<NNNN>": epic_id,
            "TASK-<CONTEXT>-<NNNN>": f"TASK-{context}-0001",
            "ADR-<CONTEXT>-<NNNN>": f"ADR-{context}-0001",
            "REL-<CONTEXT>-<NNNN>": f"REL-{context}-0001",
            "BR-<CONTEXT>-<NNNN>": f"BR-{context}-0001",
            "<FEATURE SUMMARY>": title,
            "<FEATURE OBJECTIVE>": title,
            "<PROBLEM AND VALUE>": "Definir problema e valor da Feature.",
            "<IN-SCOPE ITEM 1>": "Definir.",
            "<IN-SCOPE ITEM 2>": "Definir.",
            "<OUT-OF-SCOPE ITEM 1>": "Definir.",
            "<OUT-OF-SCOPE ITEM 2>": "Definir.",
            "AC-<CONTEXT>-0001": f"AC-{context}-0001",
            "AC-<CONTEXT>-0002": f"AC-{context}-0002",
            "<ACCEPTANCE CRITERION 1>": "definir.",
            "<ACCEPTANCE CRITERION 2>": "definir.",
        },
    )


def tasks_index_doc() -> str:
    return dedent(
        """\
        # TASKS.md

        | ID | Objetivo | Estado | Evidência |
        | --- | --- | --- | --- |
        """
    )


def task_doc(task_id: str, title: str, feature_id: str, today: str, dependencies: list[str]) -> str:
    context = task_id.split("-", 2)[1]
    dependency_block = "\n".join(f"  - {item}" for item in dependencies) if dependencies else "  - none"
    return _render(
        "tasks/TASK-TEMPLATE.md",
        {
            "TASK-<CONTEXT>-<NNNN>": task_id,
            "<TASK TITLE>": title,
            "<OWNER>": "pending",
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": today,
            "FEAT-<CONTEXT>-<NNNN>": feature_id,
            "AC-<CONTEXT>-0001": f"AC-{context}-0001",
            "dependencies:\n  - TASK-<CONTEXT>-<NNNN>\n": f"dependencies:\n{dependency_block}\n",
            "<TASK OBJECTIVE>": title,
            "<TASK SCOPE>": "Definir.",
            "<EXPECTED RESULT>": "Definir resultado verificável.",
            "<OUT-OF-SCOPE NOTE>": "Definir.",
            "<ALLOWED AREA 1>": "Definir.",
            "<ALLOWED AREA 2>": "Definir.",
            "<VALIDATION 1>": "registrar evidência documental quando aplicável;",
            "<VALIDATION 2>": "validar artefatos alterados;",
            "<DONE CRITERION 1>": "definir resultado verificável;",
            "<DONE CRITERION 2>": "registrar evidência documental quando aplicável.",
        },
    )


def decision_doc(decision_id: str, title: str, today: str, related: list[str]) -> str:
    context = decision_id.split("-", 2)[1]
    related_block = "\n".join(f"  - {item}" for item in related) if related else f"  - FEAT-{context}-0001"
    return _render(
        "decisions/ADR-TEMPLATE.md",
        {
            "ADR-<CONTEXT>-<NNNN>": decision_id,
            "<DECISION TITLE>": title,
            "type: architecture-decision": "type: decision",
            "<OWNER>": "architecture-owner",
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": today,
            "related:\n  - FEAT-<CONTEXT>-<NNNN>\n": f"related:\n{related_block}\n",
            "<CONTEXT>": "Definir.",
            "<PROBLEM>": "Definir.",
            "<DECISION>": "Definir.",
            "<CONSEQUENCE 1>": "definir impactos esperados.",
            "<CONSEQUENCE 2>": "definir riscos e trade-offs.",
        },
    )


def release_doc(release_id: str, title: str, today: str, feature_ids: list[str], version: str) -> str:
    context = release_id.split("-", 2)[1]
    related_block = "\n".join(f"  - {item}" for item in feature_ids) if feature_ids else "  - none"
    item_block = "\n".join(f"- `{item}`" for item in feature_ids) if feature_ids else "- nenhum item informado"
    return _render(
        "releases/RELEASE-TEMPLATE.md",
        {
            "REL-<CONTEXT>-<NNNN>": release_id,
            "<RELEASE TITLE>": title,
            "<RELEASE VERSION>": version,
            "<OWNER>": "release-owner",
            "<AUTHOR>": "dpf-cli",
            "<APPROVER>": "pending",
            "YYYY-MM-DD": today,
            "related:\n  - FEAT-<CONTEXT>-<NNNN>\n": f"related:\n{related_block}\n",
            "## Objetivo\n\n<RELEASE OBJECTIVE>": f"## Objetivo\n\n{title}",
            "## Itens incluídos\n\n- `FEAT-<CONTEXT>-<NNNN>`": f"## Itens incluídos\n\n{item_block}",
            "VAL-<CONTEXT>-<NNNN>": f"VAL-{context}-0001",
            "<RISK 1>": "Definir.",
            "<RISK 2>": "Definir.",
            "<RELEASE RESULT>": "Release preparada pela CLI oficial do DPF.",
        },
    )
