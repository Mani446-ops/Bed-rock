from app.v1.providers.knowledge_base_client import (
    KnowledgeBaseProvider,
)


class RetrievalService:
    def __init__(self):
        self.provider = KnowledgeBaseProvider()

    def search(self, question: str) -> list[dict]:
        return self.provider.retrieve(question)