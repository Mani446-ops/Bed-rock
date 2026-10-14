from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    aws_region: str = "us-east-1"
    s3_bucket: str
    s3_prefix: str = "banking-policies/"
    bedrock_kb_id: str
    bedrock_model_id: str

    app_env: str = "local"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()