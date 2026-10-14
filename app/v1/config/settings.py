from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Banking Agentic AI"
    app_env: str = "local"

    aws_region: str = "us-east-1"

    bedrock_model_id: str = "amazon.nova-pro-v1:0"
    bedrock_kb_id: str = ""
    sagemaker_endpoint_name: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()