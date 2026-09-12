# chatbot.py

import logging
import os

from groq import Groq

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ResearchChatbot:
    """
    RAG-powered chatbot for answering questions
    about uploaded research papers.
    """

    def __init__(self, rag_engine) -> None:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not found.")

        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-20b"
        self.rag_engine = rag_engine

    def ask(self, question: str) -> str:
        """
        Retrieve relevant context from FAISS
        and answer the user's question.
        """
        try:
            context = self.rag_engine.retrieve_context(question)

            prompt = f"""
            You are a research assistant.

            Use ONLY the provided context to answer.

            Context:
            {context}

            Question:
            {question}
            """

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You answer questions about uploaded research papers."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"Chatbot error: {e}")
            return f"Error: {str(e)}"
