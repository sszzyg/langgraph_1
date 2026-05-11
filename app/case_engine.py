from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Dict, List


ROOT_DIR = Path(__file__).resolve().parent.parent
PROTOCOL_GLOB = "MinerU_markdown_euro_ncap_protocol*.md"


@dataclass
class Section:
    title: str
    content: str


CASE_CHECKLISTS: Dict[str, List[str]] = {
    "ccr": [
        "scenario_definition",
        "impact_location",
        "target_definition",
        "vut_profile",
        "speed_parameters",
        "execution_conditions",
        "assessment_criteria",
        "scoring_rules",
        "applicability_or_robustness",
    ],
    "car_to_car_oncoming": [
        "scenario_definition",
        "impact_location",
        "speed_parameters",
        "test_procedure",
        "assessment_criteria",
        "scoring_rules",
    ],
    "lane_departure": [
        "system_definition",
        "lane_edge_or_dtle",
        "test_conditions",
        "execution_conditions",
        "assessment_criteria",
        "scoring_rules",
    ],
}


SLOT_TERMS: Dict[str, List[str]] = {
    "scenario_definition": ["scenario", "test scenario", "定义", "definitions"],
    "impact_location": ["impact location", "overlap", "impact"],
    "target_definition": ["target", "gvt", "emt", "virtual box"],
    "vut_profile": ["vut profile", "vut", "vehicle under test"],
    "speed_parameters": ["speed", "velocity", "km/h", "ttc"],
    "execution_conditions": ["test execution", "test conditions", "track", "procedure"],
    "assessment_criteria": ["assessment", "criteria", "general requirements"],
    "scoring_rules": ["scoring", "score"],
    "applicability_or_robustness": ["applicability", "robustness", "layer"],
    "test_procedure": ["test procedure", "verification", "test conduct"],
    "system_definition": ["elk", "lka", "ldw", "definition"],
    "lane_edge_or_dtle": ["lane edge", "dtle"],
}


def _find_protocol_file() -> Path | None:
    files = sorted(ROOT_DIR.glob(PROTOCOL_GLOB))
    return files[0] if files else None


def _load_sections() -> List[Section]:
    protocol_file = _find_protocol_file()
    if protocol_file is None:
        return []

    text = protocol_file.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    sections: List[Section] = []
    current_title = "ROOT"
    current_lines: List[str] = []

    heading_pattern = re.compile(r"^#\s+(.+)$")
    for line in lines:
        match = heading_pattern.match(line.strip())
        if match:
            if current_lines:
                sections.append(Section(title=current_title, content="\n".join(current_lines)))
            current_title = match.group(1).strip()
            current_lines = []
            continue
        current_lines.append(line)

    if current_lines:
        sections.append(Section(title=current_title, content="\n".join(current_lines)))
    return sections


def detect_case_id(query: str) -> str:
    q = query.lower()
    if "ccr" in q or "car-to-car rear" in q or "rear" in q:
        return "ccr"
    if "oncoming" in q:
        return "car_to_car_oncoming"
    if "lane departure" in q or "ldw" in q or "lka" in q or "elk" in q:
        return "lane_departure"
    return "ccr"


def _search_evidence(sections: List[Section], terms: List[str], max_hits: int = 2) -> List[dict]:
    scored: List[tuple[int, Section]] = []
    lowered_terms = [t.lower() for t in terms]

    for sec in sections:
        source = f"{sec.title}\n{sec.content[:2200]}".lower()
        score = sum(1 for t in lowered_terms if t and t in source)
        if score > 0:
            scored.append((score, sec))

    scored.sort(key=lambda x: x[0], reverse=True)
    hits = scored[:max_hits]

    evidence = []
    for score, sec in hits:
        excerpt = sec.content.strip().replace("\n", " ")
        if len(excerpt) > 260:
            excerpt = excerpt[:260] + "..."
        evidence.append(
            {
                "section": sec.title,
                "score": score,
                "excerpt": excerpt,
            }
        )
    return evidence


def build_case_checklist_report(query: str) -> dict:
    sections = _load_sections()
    case_id = detect_case_id(query)
    slots = CASE_CHECKLISTS.get(case_id, CASE_CHECKLISTS["ccr"])

    filled_count = 0
    slot_results = []

    for slot in slots:
        terms = SLOT_TERMS.get(slot, [slot.replace("_", " ")])
        evidence = _search_evidence(sections, terms)
        status = "filled" if evidence else "missing"
        if status == "filled":
            filled_count += 1
        slot_results.append(
            {
                "slot": slot,
                "status": status,
                "evidence": evidence,
            }
        )

    total = len(slots) if slots else 1
    coverage = filled_count / total

    return {
        "case_id": case_id,
        "coverage": round(coverage, 3),
        "slots": slot_results,
    }


def render_case_report_text(report: dict) -> str:
    lines = [
        f"Case: {report.get('case_id', 'unknown')}",
        f"Coverage: {report.get('coverage', 0)}",
        "Checklist:",
    ]

    for item in report.get("slots", []):
        slot = item.get("slot", "unknown_slot")
        status = item.get("status", "missing")
        lines.append(f"- {slot}: {status}")
        for ev in item.get("evidence", []):
            section = ev.get("section", "unknown_section")
            excerpt = ev.get("excerpt", "")
            lines.append(f"  * [{section}] {excerpt}")

    if report.get("coverage", 0) < 0.9:
        lines.append("Gap note: checklist coverage is below 0.9, recommend another retrieval pass.")

    return "\n".join(lines)
