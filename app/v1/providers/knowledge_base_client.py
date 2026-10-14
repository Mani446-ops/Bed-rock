import boto3

from app.v1.config.settings import settings


class KnowledgeBaseProvider:
    def __init__(self):
        self.client = boto3.client(
            "bedrock-agent-runtime",
            region_name=settings.aws_region,
        )

    def retrieve(self, question: str) -> list[dict]:
        if not settings.bedrock_kb_id:
            raise RuntimeError(
                "BEDROCK_KB_ID has not been configured"
            )

        response = self.client.retrieve(
            knowledgeBaseId=settings.bedrock_kb_id,
            retrievalQuery={"text": question},
            retrievalConfiguration={
                "vectorSearchConfiguration": {
                    "numberOfResults": 5
                }
            },
        )

        results = []

        for item in response.get("retrievalResults", []):
            content = item.get("content", {})
            location = item.get("location", {})

            results.append({
                "text": content.get("text", ""),
                "score": item.get("score"),
                "location": location,
            })

        return results