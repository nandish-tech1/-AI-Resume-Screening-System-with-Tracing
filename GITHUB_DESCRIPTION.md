# AI Resume Screening System with LangChain + LangSmith Tracing

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
- **Weighted Scoring**: 
  - Skills & Tools (40%)
  - Experience (30%)
  - Domain Relevance (20%)
  - Education & Certifications (10%)
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

## 🏗️ Architecture

```
Resume Input
    ↓
[STAGE 1] Skill Extraction
    • Extract: skills, tools, experience, education
    • Output: Structured JSON profile
    ↓
[STAGE 2] Matching Logic
    • Compare against job requirements
    • Identify matches, partial matches, gaps
    ↓
[STAGE 3] Scoring
    • Calculate 0-100 fit score
    • Breakdown by component (skills, experience, etc.)
    ↓
[STAGE 4] Explanation
    • Generate decision (Strong/Moderate/Low Fit)
    • Provide reasoning + improvement suggestions
    ↓
Output: Full Results + LangSmith Traces
```

### Modular Design
- **`prompts/`** - Clean, non-hardcoded prompt templates with anti-hallucination rules
- **`chains/`** - LCEL pipelines using `.invoke()` for step-level tracing
- **`utlis/`** - Configuration management and environment setup
- **`data/`** - Sample resumes and job descriptions

---

## 📋 Project Contents

### Sample Candidates
| Candidate | Profile | Expected Score |
|-----------|---------|-----------------|
| **Ananya Sharma** | 2.5 yrs ML/Data Science experience | 85-90 (Strong) |
| **Priya Patel** | 1 yr analytics/basic ML | 70-75 (Moderate) |
| **Rajesh Singh** | BBA/Operations background | 0-5 (Low Fit) |

### Job Description
- **Role**: Data Scientist Intern
- **Required Skills**: Python, SQL, ML, Statistics, Data Visualization
- **Tools**: Pandas, NumPy, Scikit-learn, Jupyter, Git
- **Experience**: 0-3 years (internship/project acceptable)

---

## 🚀 Quick Start

### 1️⃣ Setup
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/ai-resume-screening-system.git
cd ai-resume-screening-system

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Configure
Get free API keys:
- **Groq**: https://console.groq.com (free, instant)
- **LangChain** (optional): https://smith.langchain.com

Update `.env`:
```dotenv
GROQ_API_KEY=gsk_your_key_here
GROQ_MODEL=llama-3.3-70b-versatile

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_your_key_here
LANGCHAIN_PROJECT=resume-screening-system
```

### 3️⃣ Run
```bash
python main.py
```

**Output:**
```
========================================================================================
Candidate: Ananya Sharma
Fit Score: 87
Decision: Strong Fit
Top reasons:
  - The candidate's skills and tools match most of the required skills and tools
  - Has 2.5 years of relevant experience in ML and data science
  - Education and certifications align with requirements
========================================================================================
[...more candidates...]

Saved all results to: screening_results.json
Check LangSmith traces for step-level runs and debug tags.
```

---

## 📊 Results Example

Each candidate receives:
- **Fit Score** (0-100) with weighted breakdown
- **Decision** (Strong Fit / Moderate Fit / Low Fit)
- **Why This Score** - Evidence-based reasoning
- **Improvement Suggestions** - Actionable feedback
- **Debug Flags** - Potential hallucination detection

Full results saved to `screening_results.json` with complete pipeline history.

---

## 🔬 LangSmith Tracing

All pipeline executions are traced with:
- ✅ **4 complete runs** (3 baseline candidates + 1 debug case)
- ✅ **Step-level visibility** (`extract`, `match`, `score`, `explain`)
- ✅ **Contextual tags** (candidate name, run type, step type)
- ✅ **Debug tags** for incorrect output analysis
- ✅ **Real-time monitoring** at https://smith.langchain.com

---

## 💻 Technology Highlights

### LangChain Features Used
- ✅ **PromptTemplate** - Reusable, non-hardcoded prompts
- ✅ **LCEL** - Declarative pipeline composition (`prompt | llm | parser`)
- ✅ **JsonOutputParser** - Structured, type-safe outputs
- ✅ **Runnable.invoke()** - Step-level execution with config/tags

### Anti-Hallucination Design
- **Explicit constraints** in every prompt
- **Few-shot examples** to guide LLM behavior
- **Runtime detection** of hallucinated items
- **Evidence-based** output generation

### Production-Ready
- **No hardcoded outputs** - All scores from LLM
- **No assumptions** - Only resume-present information
- **Modular architecture** - Easy to extend with new stages
- **Error handling** - Configuration validation before execution
- **Logging & tracing** - Full observability

---

## 📚 Learning Outcomes

This project teaches:

1. **LLM-Based Systems Design**
   - Multi-stage pipeline architecture
   - Prompt engineering best practices
   - Anti-hallucination constraints

2. **LangChain Mastery**
   - LCEL for composable chains
   - PromptTemplate for abstraction
   - Output parsers for structured results

3. **Production Practices**
   - LangSmith tracing & debugging
   - Configuration management
   - Explainable AI design

4. **GenAI Engineering**
   - Evaluating LLM reliability
   - Detecting hallucinations
   - Building trustworthy AI systems

---

## 📋 Requirements

- Python 3.10+
- Groq API key (free)
- LangChain API key (optional, for tracing)
- ~500MB disk space (including dependencies)

---

## 📄 Files

```
.
├── main.py                          # Orchestrator & entry point
├── requirements.txt                 # Dependencies
├── .env                             # Configuration (API keys)
├── README.MD                        # Full documentation
├── COMPLIANCE_REPORT.md             # Rule compliance verification
│
├── prompts/
│   ├── intent_prompt.py            # Extraction + Matching prompts
│   └── response_prompt.py           # Scoring + Explanation prompts
│
├── chains/
│   ├── intent_chain.py             # Extraction & Matching chains
│   └── response_chain.py            # Scoring & Explanation chains
│
├── utlis/
│   └── config.py                    # Configuration management
│
└── data/
    ├── job_descriptions/
    │   └── data_scientist_jd.txt    # Sample job description
    └── resumes/
        ├── Ananya_Sharma.txt        # Strong candidate
        ├── Priya_Patel.txt          # Average candidate
        └── Rajesh_Singh.txt         # Weak candidate
```

---

## 🎓 Use Cases

- **Recruiter Tool**: Screen resumes automatically with explainability
- **Learning Project**: Understand LLM pipelines and LCEL
- **Research**: Study hallucination detection in LLMs
- **Production**: Extend with more job roles and resume databases

---

## 📈 Performance

- **Processing Time**: ~2-5 seconds per candidate (Groq is fast!)
- **Cost**: Free (Groq free tier)
- **Accuracy**: Depends on resume quality and job description clarity
- **Reliability**: Anti-hallucination constraints + runtime detection

---

## 🤝 Contributing

Feel free to extend this system:
- Add more evaluation stages (experience level, salary expectations, etc.)
- Support additional resume formats (PDF, DOCX)
- Integrate with ATS systems
- Add batch processing for multiple candidates
- Implement different scoring models

---

## 📝 License

MIT License - Feel free to use for learning, research, and commercial projects.

---

## 🙏 Credits

Built as part of the **Innomatics Data Science Internship - GenAI Assignment**

**Technologies:**
- LangChain for LLM orchestration
- Groq for fast, free LLM inference
- LangSmith for production monitoring

---

## 📞 Contact & Questions

For questions about this project:
1. Check `COMPLIANCE_REPORT.md` for technical details
2. Review `README.MD` for usage & troubleshooting
3. Examine code comments for implementation insights

---

## 🚀 Next Steps

1. **Clone this repository**
2. **Set up your environment** (API keys in `.env`)
3. **Run `python main.py`** to see the pipeline in action
4. **Check LangSmith** for trace visualization
5. **Modify sample resumes** to test with your own candidates
6. **Extend the system** with custom evaluation logic

**Happy screening!** 🎯
