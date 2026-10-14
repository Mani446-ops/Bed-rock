import boto3

from app.v1.config.settings import settings


class BedrockProvider:
    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=settings.aws_region,
        )

    def generate(self, prompt: str) -> str:
        response = self.client.converse(
            modelId=settings.bedrock_model_id,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}],
                }
            ],
            inferenceConfig={
                "maxTokens": 1000,
                "temperature": 0,
            },
        )

        return response["output"]["message"]["content"][0]["text"]