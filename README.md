# Smart AI Research Gap Finder

## Overview

Smart AI Research Gap Finder is a Streamlit-based application that helps researchers, students, and academics analyze research papers using Retrieval-Augmented Generation (RAG).

The application allows users to upload multiple PDF research papers and automatically:

- Extract text from PDFs
- Create embeddings
- Build a FAISS vector database
- Perform RAG retrieval
- Generate summaries
- Detect research trends
- Extract limitations and future work
- Identify research gaps
- Generate research proposal ideas
- Chat with uploaded papers

---

## Technology Stack

### LLM
- Groq API
- openai/gpt-oss-20b (via Groq API)

### Embeddings
- sentence-transformers/all-MiniLM-L6-v2

### Vector Database
- FAISS

### Framework
- LangChain

### PDF Processing
- PyMuPDF

### Frontend
- Streamlit

### Development
- Google Colab

---

## Project Structure

research-gap-finder/

- app.py
- orchestrator.py
- rag.py
- ai_analysis.py
- chatbot.py
- requirements.txt
- README.md

---

## Installation

### 1. Clone Repository

```bash
git clone <your-repository-url>
cd research-gap-finder
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variable

Linux/Mac:

```bash
export GROQ_API_KEY="YOUR_API_KEY"
```

Windows CMD:

```cmd
set GROQ_API_KEY=YOUR_API_KEY
```

Windows PowerShell:

```powershell
$env:GROQ_API_KEY="YOUR_API_KEY"
```

---

## Run Locally

```bash
streamlit run app.py
```

---

## Workflow

Upload PDFs
↓
RAG Processing
↓
Embeddings
↓
FAISS Index
↓
Context Retrieval
↓
AI Analysis
↓
Research Gaps
↓
Proposal Generation
↓
Chatbot

---

## Features

- Multi-PDF Upload
- Research Paper Summaries
- Limitation Extraction
- Trend Analysis
- Research Gap Detection
- Proposal Generation
- Research Chatbot
- Streamlit Deployment

---

## Deployment

1. Push project to GitHub.
2. Connect GitHub repository to Streamlit Community Cloud.
3. Add GROQ_API_KEY in Streamlit Secrets.
4. Deploy the application.

---

## License

This project is provided for educational and research purposes.
