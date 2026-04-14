# AI Resume Screening System with Tracing

An **intelligent, production-ready resume screening system** that uses LLMs to evaluate candidate fit for job roles with explainable AI and full pipeline tracing.

## 🎯 Overview

This project demonstrates advanced **GenAI engineering practices** by building a complete resume screening pipeline that:
- Extracts skills, experience, and qualifications from resumes
- Matches candidate profiles against job requirements
- Scores candidates on a 0-100 scale with weighted breakdown
- Provides explainable reasoning for every decision
- Traces all pipeline steps for debugging and monitoring

**Tech Stack:** Python • LangChain • Groq LLM • LangSmith • LCEL

---

## ✨ Key Features

### 🔍 Intelligent Extraction
- **Skill Extraction**: Python, SQL, ML frameworks, tools, certifications
- **Experience Analysis**: Years of experience, relevant projects, domains
- **Anti-Hallucination**: Explicit constraints to prevent false skill inference

### 📊 Smart Matching & Scoring
- **Requirement Matching**: Compares candidate skills against job requirements
- **Weighted Scoring**: Skills (40%) • Experience (30%) • Domain (20%) • Education (10%)
- **Risk Flagging**: Identifies potential gaps and misalignments

### 💡 Explainable AI
- **Decision Reasoning**: Why each score was assigned
- **Improvement Suggestions**: Actionable feedback for candidates
- **Scoring Breakdown**: Transparent component-wise scoring

### 🔬 Production Monitoring
- **LangSmith Integration**: Full pipeline tracing with step-level visibility
- **Debug Tags**: Special debug runs for incorrect output analysis
- **Hallucination Detection**: Runtime monitoring for LLM reliability

---

## 🚀 Quick Start

### Setup
```bash
# Clone and setup
git clone https://github.com/nandish-tech1/-AI-Resume-Screening-System-with-Tracing.git
cd -AI-Resume-Screening-System-with-Tracing

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

### Configure
Update `.env`:
```dotenv
GROQ_API_KEY=your_groq_key_here
GROQ_MODEL=llama-3.3-70b-versatile
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_key_here
```

### Run
```bash
python main.py
```

---

## 📊 Pipeline Architecture

```
Resume Input → Extraction → Matching → Scoring → Explanation → LangSmith Traces
```

### 4-Stage Pipeline
1. **Extraction**: Skills, tools, experience, education
2. **Matching**: Compare against job requirements
3. **Scoring**: 0-100 fit score with breakdown
4. **Explanation**: Decision + reasoning + suggestions

---

## 📁 Project Structure

```
.
├── main.py                          # Entry point & orchestrator
├── requirements.txt                 # Dependencies
├── .env                             # Configuration
├── README.md                        # This file
├── COMPLIANCE_REPORT.md             # Rule compliance check
├── GITHUB_DESCRIPTION.md            # Full description
│
├── prompts/                         # Prompt templates
│   ├── intent_prompt.py            # Extraction + Matching
│   └── response_prompt.py           # Scoring + Explanation
│
├── chains/                          # LangChain LCEL pipelines
│   ├── intent_chain.py             # Extraction & Matching chains
│   └── response_chain.py            # Scoring & Explanation chains
│
├── utlis/                           # Configuration
│   └── config.py                    # Environment setup
│
└── data/                            # Sample data
    ├── job_descriptions/
    │   └── data_scientist_jd.txt
    └── resumes/
        ├── Ananya_Sharma.txt        # Strong candidate (87/100)
        ├── Priya_Patel.txt          # Average candidate (73/100)
        └── Rajesh_Singh.txt         # Weak candidate (0/100)
```

---

## 💻 Technology Stack

- **Python 3.10+**
- **LangChain 0.3.27** - LLM orchestration
- **Groq** - Free, fast LLM inference
- **LangSmith** - Pipeline tracing & monitoring
- **python-dotenv** - Environment management

---


## 📊 Sample Output

```
========================================================================================
Candidate: Ananya Sharma
Fit Score: 87
Decision: Strong Fit
Top reasons:
  - The candidate's skills and tools match most required skills
  - Has 2.5 years of relevant ML and data science experience
  - Education and certifications align with requirements
========================================================================================

Candidate: Priya Patel
Fit Score: 73
Decision: Moderate Fit

Candidate: Rajesh Singh
Fit Score: 0
Decision: Low Fit

Saved all results to: screening_results.json
Check LangSmith traces for step-level runs and debug tags.
```

---

## 🔬 LangSmith Tracing

All 4 runs are traced with:
- ✅ Step-level visibility (extract → match → score → explain)
- ✅ Contextual tags (candidate name, run type)
- ✅ Debug tags for analysis
- ✅ Real-time monitoring at https://smith.langchain.com

---

## 📚 Learning Outcomes

Build production-grade GenAI systems with:
- LLM-based pipeline design
- LangChain & LCEL mastery
- Prompt engineering best practices
- Anti-hallucination constraints
- LangSmith tracing & debugging
- Explainable AI architecture

---

## 🎓 Use Cases

- **Recruiter Tool**: Automated resume screening
- **Learning Project**: LLM pipelines & LCEL
- **Research**: Hallucination detection
- **Production**: ATS integration, batch processing

---

## 📈 Performance

- **Processing**: ~2-5 seconds per candidate
- **Cost**: Free (Groq free tier)
- **Reliability**: Anti-hallucination + runtime detection

---

## 📝 License

MIT License - Educational and commercial use allowed

---

## 🙏 Credits

Built for **Innomatics Data Science Internship - GenAI Assignment**

**Technologies**: LangChain • Groq • LangSmith

---

## 📖 Documentation

- `README.md` - Quick start & overview (this file)
- `GITHUB_DESCRIPTION.md` - Full project description
- `COMPLIANCE_REPORT.md` - Assignment compliance verification
- Code comments - Implementation details

---

## 🚀 Get Started

1. Clone the repo
2. Configure `.env` with API keys
3. Run `python main.py`
4. Check `screening_results.json` for results
5. View traces at https://smith.langchain.com
6. Extend with your own resumes/jobs

**Happy screening!** 🎯
