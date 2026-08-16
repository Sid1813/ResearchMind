# 🧠 ResearchMind

### Autonomous Multi-Agent Research Platform

ResearchMind is an AI-powered multi-agent research platform that transforms a broad research question into a structured, evidence-grounded research report.

The system uses specialized AI agents to plan research, retrieve web evidence, synthesize findings, generate a report, optionally critique the result, and export the final report as a PDF.

Built with **Python, Google Gemini, Tavily, Streamlit, Pydantic, and ReportLab**.

---

# 📸 Demo

## Main Interface

![ResearchMind Main Interface](docs/screenshots/Main%20Interface.png)

The main interface allows users to enter a research topic and generate an end-to-end research report.

## Research Plan

![Research Plan](docs/screenshots/Research%20Plan.png)

The Planner Agent breaks the research topic into six focused research tasks.

## Final Research Report

![Final Research Report](docs/screenshots/Final%20Research%20Report.png)

The Writer Agent synthesizes the collected evidence into a structured research report containing an executive summary, detailed analysis, key takeaways, and conclusion.

---

# 🚀 Features

- 🧠 **AI Research Planning** — Breaks a broad topic into six focused research tasks.
- 🔍 **Web Research** — Uses Tavily to retrieve relevant web evidence.
- 🤖 **Multi-Agent Architecture** — Separate Planner, Researcher, Writer, and Critic agents.
- ✍️ **AI Report Generation** — Synthesizes research evidence into a structured report.
- 🧐 **Optional AI Critic** — Evaluates the generated report and provides a quality score, strengths, weaknesses, and improvements.
- 📚 **Source Tracking** — Displays the sources associated with each research task.
- 📄 **PDF Export** — Generates a downloadable PDF version of the final report.
- 📦 **Structured Output** — Uses Pydantic schemas to validate structured LLM responses.
- 🔐 **Environment-Based Secrets** — API keys are loaded through environment variables rather than hardcoded.
- 💰 **Free-Tier Friendly** — The Critic Agent can be disabled to reduce Gemini API usage.

---

# 🏗️ Architecture

ResearchMind follows a modular multi-agent architecture:

```text
                         ┌─────────────────┐
                         │   User Topic    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Planner Agent  │
                         │                 │
                         │ Creates 6 Tasks │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │     Research Agents      │
                    │                          │
                    │ Task → Tavily Search     │
                    │       → Gemini Analysis  │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                         ┌─────────────────┐
                         │  Writer Agent   │
                         │                 │
                         │ Evidence →      │
                         │ Final Report    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Optional Critic │
                         │                 │
                         │ Score + Review  │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Research Report │
                         │                 │
                         │ PDF Export      │
                         └─────────────────┘
```

## Current Execution Model

The current version executes research tasks **sequentially**.

This was an intentional design choice because Gemini's free-tier request-per-minute limits can be exceeded when multiple research agents make API calls simultaneously.

The architecture is modular enough that the research stage can be changed to concurrent execution when higher API limits are available.

---

# 🔄 How It Works

## 1. User Enters a Research Topic

The user provides a broad research question or topic.

For example:

```text
Climate Change
```

The topic is passed to the `ResearchPipeline`.

---

## 2. Planner Agent

The Planner Agent analyzes the topic and creates exactly six focused research tasks.

For example:

```text
Task 1: Causes of Climate Change
Task 2: Environmental Impacts
Task 3: Economic and Social Effects
Task 4: Mitigation Strategies
Task 5: Adaptation Strategies
Task 6: Future Outlook
```

The Planner uses a Pydantic schema to ensure the model returns structured task data.

---

## 3. Research Agent

Each research task is passed to a Research Agent.

The Research Agent:

1. Sends the task to Tavily.
2. Retrieves relevant web results.
3. Extracts titles, content, and URLs.
4. Provides the retrieved evidence to Gemini.
5. Generates a concise research summary.
6. Stores the findings together with their sources.

The research process follows:

```text
Web Search
    ↓
Retrieved Evidence
    ↓
Gemini Analysis
    ↓
Research Summary
```

---

## 4. Writer Agent

The Writer Agent receives the evidence collected from the research tasks.

It synthesizes the evidence into a structured report containing:

- Executive Summary
- Detailed Analysis
- Key Takeaways
- Conclusion

The Writer Agent is instructed to base the report on the supplied research evidence rather than generating unsupported information.

---

## 5. Optional Critic Agent

The Critic Agent provides a second layer of evaluation for the generated report.

It evaluates:

- Overall report quality
- Strengths
- Weaknesses
- Suggested improvements

The Critic is optional because it requires an additional Gemini API request.

This allows ResearchMind to operate with lower API usage when working within free-tier limits.

---

## 6. PDF Export

The completed report can be exported as a downloadable PDF directly from the Streamlit interface.

---

# 🧩 Project Structure

```text
ResearchMind/
│
├── agents/
│   ├── base_agent.py
│   ├── planner.py
│   ├── researcher.py
│   ├── writer.py
│   └── critic.py
│
├── config/
│   └── prompts.py
│
├── memory/
│
├── orchestrator/
│   └── pipeline.py
│
├── outputs/
│
├── schemas/
│   ├── task.py
│   ├── evidence.py
│   ├── report.py
│   └── review.py
│
├── services/
│   ├── gemini_service.py
│   ├── tavily_service.py
│   └── pdf_service.py
│
├── tests/
│
├── tools/
│
├── ui/
│
├── utils/
│
├── workflows/
│
├── docs/
│   └── screenshots/
│       ├── Main Interface.png
│       ├── Research Plan.png
│       └── Final Research Report.png
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **Google Gemini** | Planning, research analysis, report generation, optional evaluation |
| **Tavily** | Web search and evidence retrieval |
| **Streamlit** | Interactive web application |
| **Pydantic** | Structured output validation |
| **ReportLab** | PDF report generation |
| **python-dotenv** | Environment variable management |
| **Git / GitHub** | Version control |

---

# 🔐 Environment Variables

ResearchMind uses environment variables for API credentials.

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The `.env` file is excluded from version control through `.gitignore`.

**API keys should never be hardcoded into source code or committed to GitHub.**

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Sid1813/ResearchMind.git
cd ResearchMind
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Virtual Environment

### Windows

```powershell
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📊 Example Workflow

For the research topic:

```text
Climate Change
```

ResearchMind performs the following workflow:

```text
User Topic
    ↓
Planner Agent
    ↓
6 Research Tasks
    ↓
Tavily Web Search
    ↓
Research Evidence
    ↓
Research Summaries
    ↓
Writer Agent
    ↓
Structured Research Report
    ↓
Optional Critic Agent
    ↓
Quality Evaluation
    ↓
PDF Export
```

---

# 💡 Design Decisions

## Why Multiple Agents?

A single LLM prompt could generate a research report, but separating the workflow into specialized agents makes the system easier to understand, maintain, and extend.

Each agent has a distinct responsibility:

```text
Planner  → What should we research?

Research  → What does the retrieved evidence say?

Writer    → How should the evidence be synthesized?

Critic    → How good is the generated report?
```

This separation also makes it easier to replace or improve individual components without redesigning the entire application.

---

## Why Pydantic?

LLMs naturally produce text, but applications often need predictable structured data.

Pydantic provides a validation layer between the LLM and the rest of the application.

For example, the Planner Agent produces a `ResearchPlan` containing validated `ResearchTask` objects.

This makes the downstream pipeline more reliable than relying on free-form text parsing alone.

---

## Why Tavily?

ResearchMind is designed to perform web-grounded research rather than relying entirely on the model's internal knowledge.

Tavily provides external search results that are passed to the Research Agent and subsequently used by the Writer Agent.

This creates the following flow:

```text
Search
  ↓
Evidence
  ↓
Analysis
  ↓
Synthesis
```

---

## Why an Optional Critic?

The Critic Agent improves the system by providing an additional evaluation stage.

However, every additional Gemini call consumes API quota.

Therefore, ResearchMind allows the user to choose whether the final report should be evaluated.

This makes the application more practical when operating under free-tier API limits.

---

# 🧠 Key Engineering Concepts Demonstrated

This project demonstrates practical experience with:

- Multi-agent system architecture
- LLM API integration
- Prompt engineering
- Structured LLM outputs
- Pydantic validation
- Web-grounded generation
- Evidence-based report synthesis
- LLM-based evaluation
- API rate-limit management
- Modular Python architecture
- Streamlit application development
- PDF generation
- Environment variable management
- Git and GitHub workflows

---

# 📌 Project Status

**Version 1.0 — Completed**

ResearchMind currently supports an end-to-end research workflow:

```text
Plan → Search → Research → Write → Critique → Export
```

The application demonstrates how specialized LLM agents can be combined into a modular AI research workflow.

---

# 👨‍💻 Author

## Siddharth Ranganatha

**GitHub:** [@Sid1813](https://github.com/Sid1813)

ResearchMind was built as a hands-on project to explore practical **LLM, multi-agent, RAG, and AI engineering** concepts.

---


