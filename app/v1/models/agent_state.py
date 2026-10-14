from typing import TypedDict


class AgentState(TypedDict, total=False):
    question: str
    evidence: list[dict]
    answer: str
    sources: list[dict]
    use_sagemaker: bool
    error: str