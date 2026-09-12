import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from orchestrator import ResearchGapFinderOrchestrator

load_dotenv()

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Smart AI Research Gap Finder",
    page_icon="🧠",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* ==================================================
   GLOBAL
================================================== */

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* ==================================================
   HERO SECTION
================================================== */

.hero{
    padding:35px;
    border-radius:25px;
    margin-bottom:25px;

    background:
    linear-gradient(
        135deg,
        #2563eb,
        #7c3aed,
        #9333ea
    );

    color:white;

    box-shadow:
    0 10px 35px rgba(0,0,0,.18);
}

.hero h1{
    font-size:3rem;
    font-weight:800;
    margin-bottom:8px;
}

.hero h4{
    opacity:.95;
}

.hero p{
    line-height:1.8;
    font-size:1.05rem;
}

/* ==================================================
   FEATURE CARDS
================================================== */

.feature-card{

    background:
    rgba(127,127,127,.08);

    border:
    1px solid rgba(127,127,127,.20);

    border-radius:18px;

    padding:22px;

    min-height:150px;

    transition:.3s;
}

.feature-card:hover{

    transform:
    translateY(-4px);

    border-color:#2563eb;
}

.feature-card h4{
    margin-bottom:10px;
}

/* ==================================================
   METRICS
================================================== */

[data-testid="stMetric"]{

    background:
    rgba(127,127,127,.05);

    border:
    1px solid rgba(127,127,127,.18);

    border-radius:18px;

    padding:18px;
}

/* ==================================================
   BUTTONS
================================================== */

.stButton > button{

    width:100%;

    height:56px;

    border-radius:14px;

    font-size:18px;

    font-weight:700;
}

/* ==================================================
   RESULT BOX
================================================== */

.result-box{

    background:
    rgba(127,127,127,.05);

    border:
    1px solid rgba(127,127,127,.20);

    border-radius:18px;

    padding:25px;

    line-height:1.9;

    font-size:1rem;

    color:inherit;

    overflow-wrap:break-word;
}

/* ==================================================
   CHAT
================================================== */

[data-testid="stChatMessage"]{

    border-radius:16px;

    padding:12px;

    border:
    1px solid rgba(127,127,127,.15);
}

/* ==================================================
   TABS
================================================== */

.stTabs [data-baseweb="tab"]{

    height:55px;

    font-weight:700;

    border-radius:12px;
}

/* ==================================================
   FILE UPLOADER
================================================== */

[data-testid="stFileUploader"]{

    border-radius:16px;
}

/* ==================================================
   EXPANDER
================================================== */

.streamlit-expanderHeader{

    font-size:18px;

    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================

if "orchestrator" not in st.session_state:
    try:
        st.session_state.orchestrator = ResearchGapFinderOrchestrator()
    except ValueError as e:
        st.error(
            f"⚠️ Startup error: {e}\n\n"
            "Set the GROQ_API_KEY environment variable (or add it to a "
            ".env file) and reload the app."
        )
        st.stop()

if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None

if "messages" not in st.session_state:
    st.session_state.messages = []

orchestrator = st.session_state.orchestrator

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px;
        border-radius:15px;
        border:1px solid rgba(128,128,128,0.25);
        margin-bottom:15px;
    ">
        <h2 style="margin-bottom:5px;">
            🧠 Smart AI
        </h2>
        <p style="margin-top:0;">
            Research Gap Finder
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.success("🟢 System Ready")

    st.markdown("### 🚀 AI Technology Stack")

    st.markdown("""
    **🤖 LLM Model**  
    GPT-OSS-20B

    **⚡ Inference Engine**  
    Groq API

    **🧩 Framework**  
    LangChain

    **🗄️ Vector Database**  
    FAISS

    **🧠 Embeddings**  
    MiniLM-L6-v2
    """)

    st.divider()

    st.markdown("### ✨ Core Features")

    st.markdown("""
    📑 Smart Research Summaries

    📈 Trend Detection & Insights

    ⚠️ Limitation Extraction

    🎯 Research Gap Discovery

    💡 Proposal Idea Generation

    💬 AI Research Assistant
    """)

    st.divider()

    st.markdown("### 🔄 Research Workflow")

    st.markdown("""
    📂 Upload Research Papers

    ⬇️

    🧠 Generate Embeddings

    ⬇️

    🗄️ Build FAISS Index

    ⬇️

    🔍 Retrieve Relevant Context

    ⬇️

    🤖 AI Analysis Engine

    ⬇️

    🎯 Research Gap Detection

    ⬇️

    💡 Proposal Generation
    """)

    st.divider()

    st.markdown("### 📊 Status")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("AI", "Ready")

    with col2:
        st.metric("RAG", "Active")

    st.divider()

    st.caption(
        "Version 1.0 • Streamlit • LangChain • FAISS • Groq"
    )
# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">
<h1>🧠 Smart AI Research Gap Finder</h1>

<h4>Transform Research Papers into Research Opportunities</h4>

<p>
Upload research papers and automatically generate summaries,
identify trends, extract limitations, discover research gaps,
generate proposal ideas, and chat with your papers using AI.
</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE CARDS
# ==================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
    <h4>📄 Summaries</h4>
    Generate concise research summaries.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
    <h4>🔍 Research Gaps</h4>
    Identify potential research opportunities.
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
    <h4>🤖 Research Chatbot</h4>
    Ask questions about uploaded papers.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_files = st.file_uploader(
    "📂 Upload PDF Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)

# ==================================================
# METRICS
# ==================================================

if uploaded_files:

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Papers Uploaded", len(uploaded_files))
    col2.metric("🧠 AI Engine", "Ready")
    col3.metric("🔍 Gap Finder", "Active")
    col4.metric("🤖 Chatbot", "Online")

# ==================================================
# ANALYSIS
# ==================================================

if st.button("🚀 Analyze Papers", use_container_width=True):

    if not uploaded_files:
        st.warning("Please upload at least one PDF.")

    else:

        pdf_paths = []

        try:

            for uploaded_file in uploaded_files:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp_file:

                    tmp_file.write(uploaded_file.read())
                    pdf_paths.append(tmp_file.name)

            progress = st.progress(0)

            progress.progress(10)
            st.info("📄 Reading PDF files...")

            progress.progress(30)
            st.info("🧠 Generating embeddings...")

            progress.progress(50)
            st.info("📚 Building FAISS vector database...")

            progress.progress(75)
            st.info("🔍 Running AI analysis...")

            results = orchestrator.process_papers(
                pdf_paths
            )

            progress.progress(100)

            if "error" in results:

                st.error(results["error"])

            else:

                st.session_state.analysis_results = results

                st.success(
                    "✅ Analysis Completed Successfully"
                )

        except Exception as e:

            st.error(
                f"Application Error: {e}"
            )

        finally:

            # Clean up the temp PDF files now that processing is done,
            # instead of leaving them on disk indefinitely.
            for path in pdf_paths:
                try:
                    os.remove(path)
                except OSError:
                    pass
# ==================================================
# DISPLAY RESULTS
# ==================================================

if st.session_state.analysis_results:

    results = st.session_state.analysis_results
    st.json(results)
    report = f"""
SMART AI RESEARCH GAP FINDER REPORT

================================================

SUMMARY

{results.get("summary", "")}

================================================

TRENDS

{results.get("trends", "")}

================================================

LIMITATIONS

{results.get("limitations", "")}

================================================

RESEARCH GAPS

{results.get("research_gaps", "")}

================================================

PROPOSAL IDEAS

{results.get("proposal", "")}
"""

    st.download_button(
        label="📥 Download Research Report",
        data=report,
        file_name="research_report.txt",
        mime="text/plain"
    )

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📄 Summary",
            "📈 Trends",
            "⚠️ Limitations",
            "🔍 Research Gaps",
            "💡 Proposals"
        ]
    )

    with tab1:
        st.markdown("### 📄 Research Summary")
        st.info(results.get("summary", "No summary available."))

    with tab2:
        st.markdown("### 📈 Research Trends")
        st.info(results.get("trends", "No trends available."))

    with tab3:
        st.markdown("### ⚠️ Research Limitations")
        st.info(results.get("limitations", "No limitations available."))

    with tab4:
        st.markdown("### 🔍 Potential Research Gaps")
        st.info(results.get("research_gaps", "No research gaps available."))

    with tab5:
        st.markdown("### 💡 Research Proposal Ideas")
        st.info(results.get("proposal", "No proposal ideas available."))
# ==================================================
# CHATBOT
# ==================================================

st.divider()

st.markdown("## 🤖 Research Assistant")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input(
    "Ask a question about your uploaded papers..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    answer = orchestrator.ask_chatbot(
        question
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown(
"""
<center>

🧠 Smart AI Research Gap Finder v1.0

Built with Streamlit • LangChain • FAISS • Groq

From Research Papers to Research Opportunities

</center>
""",
unsafe_allow_html=True
)
