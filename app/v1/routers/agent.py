from fastapi import APIRouter, HTTPException

from app.v1.serializers.agent_schema import (
    AgentRequest,
    AgentResponse,
)
from app.v1.services.agent_graph import run_agent


router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/query", response_model=AgentResponse)
def query_agent(request: AgentRequest):
    try:
        result = run_agent(request.question)

        return AgentResponse(
            answer=result.get("answer", ""),
            sources=result.get("sources", []),
        )

    except Exception:
        # Do not expose internal AWS errors or secrets to clients.
        raise HTTPException(
            status_code=502,
            detail="The agent service could not complete the request.",
        )