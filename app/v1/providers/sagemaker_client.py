import json
import boto3

from app.v1.config.settings import settings


class SageMakerProvider:
    def __init__(self):
        self.client = boto3.client(
            "sagemaker-runtime",
            region_name=settings.aws_region,
        )

    def predict(self, payload: dict) -> dict:
        endpoint = settings.sagemaker_endpoint_name

        if not endpoint:
            raise RuntimeError(
                "SAGEMAKER_ENDPOINT_NAME has not been configured"
            )

        response = self.client.invoke_endpoint(
            EndpointName=endpoint,
            ContentType="application/json",
            Accept="application/json",
            Body=json.dumps(payload).encode("utf-8"),
        )

        return json.loads(response["Body"].read())