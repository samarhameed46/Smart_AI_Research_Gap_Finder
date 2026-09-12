# orchestrator.py

import logging
from typing import Dict, List

from rag import RAGEngine
from ai_analysis import AIAnalysis
from chatbot import ResearchChatbot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ResearchGapFinderOrchestrator:
    """
    Central controller for the application.

    Responsibilities:
    - Validate inputs
    - Run RAG pipeline
    - Run AI analysis
    - Initialize chatbot
    - Return results
    """

    def __init__(self) -> None:
        self.rag_engine = RAGEngine()
        self.ai_analysis = AIAnalysis()
        self.chatbot = None

    def process_papers(self, pdf_paths: List[str]) -> Dict[str, str]:
        """
        Complete workflow:

        PDFs
          ↓
        RAG
          ↓
        Analysis
          ↓
        Results
        """

        try:
            if not pdf_paths:
                raise ValueError("No PDF files were provided.")

            self.rag_engine.process_pdfs(pdf_paths)

            # Use as much of the processed document text as will fit
            # in a prompt, rather than a single top-5 similarity
            # search, so the analysis sees the full papers instead of
            # a handful of matching chunks.
            context = self.rag_engine.get_full_context()

            results = self.ai_analysis.run_full_analysis(context)

            self.chatbot = ResearchChatbot(self.rag_engine)

            logger.info("Analysis completed successfully.")

            return results

        except Exception as e:
            logger.error(f"Workflow error: {e}")

            return {
                "error": str(e)
            }

    def ask_chatbot(self, question: str) -> str:
        """
        Ask questions about uploaded papers.
        """

        try:
            if self.chatbot is None:
                return (
                    "Please upload and process papers first."
                )

            return self.chatbot.ask(question)

        except Exception as e:
            logger.error(f"Chatbot workflow error: {e}")
            return f"Error: {str(e)}"
