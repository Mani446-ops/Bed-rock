from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=2000,
    )


class AgentResponse(BaseModel):
    answer: str
    sources: list[dict] = Field(default_factory=list)