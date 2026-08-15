# 🧠 ResearchMind

### Autonomous Multi-Agent Research Platform

ResearchMind is an AI-powered research platform that automatically decomposes a research topic into multiple sub-tasks, performs web research in parallel/sequential agent workflows, synthesizes the collected evidence into a structured research report, optionally evaluates the report using an AI critic, and exports the final result as a PDF.

The project was built to explore **multi-agent AI systems, LLM orchestration, structured outputs, web-grounded generation, and modular AI application architecture**.

---

## 🚀 Overview

Traditional research workflows require manually:

1. Defining the research questions
2. Searching for relevant information
3. Reading and organizing sources
4. Synthesizing findings
5. Writing the final report
6. Reviewing the quality of the report

ResearchMind automates this workflow through a modular multi-agent pipeline.

Given a topic such as:

> **"Future of Agentic AI"**

ResearchMind generates a structured research plan containing six tasks, researches each task using web search, generates evidence-backed findings, synthesizes those findings into a professional report, and optionally performs an additional AI-based quality review.

### High-Level Workflow

```text
Research Topic
      │
      ▼
┌─────────────────┐
│  Planner Agent  │
└────────┬────────┘
         │
         ▼
   Research Tasks
    ┌────┼────┐
    │    │    │
    ▼    ▼    ▼
 Research Agents
    │    │    │
    └────┼────┘
         │
         ▼
   Collected Evidence
         │
         ▼
┌─────────────────┐
│   Writer Agent  │
└────────┬────────┘
         │
         ▼
    Final Report
         │
         ├───────────────┐
         ▼               ▼
   PDF Export      Optional Critic
                         │
                         ▼
                  Quality Review
```

---

## ✨ Features

* 🧠 **AI Research Planning**

  * Automatically decomposes a topic into six focused research tasks.

* 🔍 **Web-Grounded Research**

  * Uses Tavily to retrieve relevant web information.
  * Research agents use retrieved evidence rather than relying solely on model knowledge.

* 🤖 **Multi-Agent Architecture**

  * Planner, Researcher, Writer, and Critic agents have separate responsibilities.

* ⚡ **Sequential Research Pipeline**

  * Research tasks are processed sequentially to remain compatible with Gemini free-tier request limits.
  * The architecture can be extended to parallel execution when higher API quotas are available.

* 📝 **AI Report Generation**

  * Combines collected evidence into an executive summary, detailed analysis, key takeaways, and conclusion.

* 🧐 **Optional AI Critic**

  * The final report can be evaluated using an additional Gemini request.
  * The critic identifies strengths, weaknesses, improvements, and provides an overall score.

* 📊 **Research Dashboard**

  * Displays task count, collected sources, AI quality score, and execution time.

* 📄 **PDF Export**

  * Generates a downloadable PDF version of the final research report.

* 🧩 **Structured LLM Output**

  * Uses Pydantic schemas to validate structured model responses.

* 🌐 **Streamlit Interface**

  * Provides a simple interactive UI for running research workflows.

* 🔐 **Environment-Based API Configuration**

  * API credentials are loaded from environment variables rather than being hardcoded.

---

## 🖥️ Application Preview

### Main Interface

<!-- Add screenshot here: docs/screenshots/home.png -->

![ResearchMind Main Interface](docs/screenshots/home.png)

The main interface allows the user to enter a research topic and optionally enable AI-based report evaluation.

---

### Research Plan & Findings

<!-- Add screenshot here: docs/screenshots/research-plan.png -->

![Research Plan and Findings](docs/screenshots/research-plan.png)

ResearchMind displays the generated research tasks along with the findings and sources collected for each task.

---

### Final Research Report

<!-- Add screenshot here: docs/screenshots/final-report.png -->

![Final Research Report](docs/screenshots/final-report.png)

The final report contains:

* Executive Summary
* Detailed Analysis
* Key Takeaways
* Conclusion
* Downloadable PDF

When enabled, the AI Quality Review also displays strengths, weaknesses, and suggested improvements.

---

## 🏗️ Architecture

ResearchMind follows a modular agent-based architecture.

```text
                         ┌──────────────────┐
                         │    Streamlit UI  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ ResearchPipeline │
                         └────────┬─────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 ▼                ▼                ▼
          ┌────────────┐   ┌──────────────┐  ┌─────────────┐
          │   Planner  │   │  Researcher  │  │   Writer    │
          │    Agent   │   │    Agents    │  │    Agent    │
          └────────────┘   └──────┬───────┘  └──────┬──────┘
                                  │                 │
                                  ▼                 │
                           ┌──────────────┐         │
                           │ Tavily Search│         │
                           └──────┬───────┘         │
                                  │                 │
                                  └────────┬────────┘
                                           │
                                           ▼
                                  ┌────────────────┐
                                  │  Final Report  │
                                  └───────┬────────┘
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                       ┌────────────┐          ┌────────────┐
                       │ PDF Export │          │ AI Critic  │
                       └────────────┘          └────────────┘
```

---

## 🔄 Research Pipeline

### 1. Planner Agent

The Planner Agent receives the user's research topic and generates exactly six research tasks.

For example:

```text
Topic:
"Future of Agentic AI"

        ↓

Task 1: Current Agentic AI Landscape
Task 2: Agent Architectures
Task 3: Applications
Task 4: Technical Challenges
Task 5: Safety and Reliability
Task 6: Future Trends
```

The output is validated using a Pydantic `ResearchPlan` schema.

---

### 2. Research Agents

Each task is passed to a Research Agent.

The Research Agent:

1. Receives the task.
2. Queries Tavily.
3. Collects relevant search results.
4. Builds an evidence context.
5. Sends the evidence to Gemini.
6. Generates a concise research summary.
7. Stores the source title and URL.

The research agent is explicitly instructed to:

> Use only the supplied evidence and avoid inventing facts.

This helps reduce unsupported LLM-generated claims.

---

### 3. Writer Agent

The Writer Agent receives the evidence collected from all research tasks.

It generates a structured report containing:

```text
Executive Summary
        ↓
Detailed Analysis
        ↓
Key Takeaways
        ↓
Conclusion
```

The writer is instructed to base the report on the supplied research evidence rather than generating unsupported information.

---

### 4. Optional Critic Agent

The Critic Agent is optional because it requires an additional Gemini API request.

When enabled, the critic evaluates the final report and returns:

```text
Overall Score
Strengths
Weaknesses
Suggested Improvements
```

The UI exposes this functionality through:

```text
☑ Evaluate final report using AI
```

This design allows ResearchMind to remain usable within tighter API quotas while retaining the complete multi-agent architecture.

---

### 5. PDF Export

The completed report is passed to the PDF service.

The user can then download:

```text
Research_Report.pdf
```

directly from the Streamlit interface.

---

## 🧱 Project Structure

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
├── workflows/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── test_gemini.py
```

---

## 🧩 Components

### `agents/`

Contains the individual AI agents.

#### `base_agent.py`

Provides common functionality for agents, including interaction with the Gemini service.

#### `planner.py`

Responsible for decomposing the research topic into structured tasks.

#### `researcher.py`

Responsible for web search, evidence collection, and research summarization.

#### `writer.py`

Responsible for synthesizing research evidence into the final report.

#### `critic.py`

Responsible for optional AI-based report evaluation.

---

### `orchestrator/`

Contains the central workflow controller.

#### `pipeline.py`

Coordinates the entire research workflow:

```text
Planner
   ↓
Research
   ↓
Writer
   ↓
Optional Critic
```

This keeps the agents independent from the application interface.

---

### `schemas/`

Contains Pydantic models used to enforce structured data.

Examples include:

```text
ResearchTask
ResearchPlan
Evidence
Source
ResearchReport
Review
```

Using schemas prevents different agents from passing arbitrary unstructured data throughout the system.

---

### `services/`

Contains integrations with external services.

#### `gemini_service.py`

Handles communication with the Gemini API.

#### `tavily_service.py`

Handles web search and retrieval.

#### `pdf_service.py`

Converts the final research report into a PDF.

---

### `app.py`

Contains the Streamlit frontend.

The UI is intentionally implemented using Python and Streamlit without custom CSS so that the application remains simple to understand and maintain.

---

## 🛠️ Tech Stack

| Technology    | Purpose                                                   |
| ------------- | --------------------------------------------------------- |
| Python        | Core programming language                                 |
| Streamlit     | Web application interface                                 |
| Google Gemini | LLM reasoning, planning, writing, and optional evaluation |
| Tavily        | Web search and research retrieval                         |
| Pydantic      | Structured output validation                              |
| ReportLab     | PDF report generation                                     |
| python-dotenv | Environment variable management                           |
| Git           | Version control                                           |
| GitHub        | Source code hosting                                       |

---

## 🔐 Environment Variables

API keys are stored locally in a `.env` file.

Example:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The `.env` file is excluded from Git using `.gitignore`.

### Important

Never commit API keys directly into:

* Python files
* Jupyter notebooks
* README files
* configuration files
* Git repositories

The project uses environment variables instead.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sidhu2sharp/ResearchMind.git
cd ResearchMind
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```powershell
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env`

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ▶️ Usage

### Step 1 — Enter a research topic

Example:

```text
Future of Agentic AI
```

### Step 2 — Choose whether to evaluate the report

The AI critic is optional.

Leaving it disabled reduces the number of Gemini requests.

### Step 3 — Generate the report

ResearchMind will:

```text
Create Research Plan
        ↓
Research Each Task
        ↓
Collect Sources
        ↓
Generate Report
        ↓
Optional AI Review
        ↓
Generate PDF
```

### Step 4 — Explore the results

The application displays:

* Research tasks
* Research findings
* Source URLs
* Final report
* AI quality review
* Execution time
* Source count

### Step 5 — Download the report

Click:

```text
📄 Download Research Report (PDF)
```

---

## 💡 Design Decisions

### Why separate agents?

Each agent has a single responsibility.

Instead of one giant prompt handling the entire workflow:

```text
One LLM
   ↓
Everything
```

ResearchMind separates responsibilities:

```text
Planner → Researcher → Writer → Critic
```

This makes the system:

* Easier to debug
* Easier to extend
* Easier to test
* Easier to reason about
* Easier to replace individual components

---

### Why use Pydantic?

LLMs naturally generate text, but multi-agent systems require predictable data structures.

For example, the Planner should return:

```json
{
    "tasks": [
        {
            "id": 1,
            "title": "...",
            "description": "..."
        }
    ]
}
```

Pydantic validates this structure before the rest of the pipeline uses it.

This reduces failures caused by malformed model responses.

---

### Why use Tavily?

A language model's internal knowledge may be incomplete or outdated.

Tavily provides external web retrieval that allows ResearchMind to ground its research process in retrieved sources.

The architecture therefore becomes:

```text
Web Search
    ↓
Evidence
    ↓
LLM Synthesis
```

rather than:

```text
LLM
 ↓
Unverified Answer
```

---

### Why is the Critic optional?

The critic requires an additional LLM request.

Since the application was designed to work with constrained/free-tier API quotas, the critic can be disabled when request limits are important.

This provides a practical trade-off:

```text
Normal Mode
Planner + Research + Writer

Evaluation Mode
Planner + Research + Writer + Critic
```

---

### Why sequential research?

The original architecture experimented with parallel research agents using `ThreadPoolExecutor`.

However, multiple simultaneous Gemini requests can quickly hit free-tier rate limits.

The current pipeline therefore prioritizes reliability:

```text
Task 1 → Task 2 → Task 3 → Task 4 → Task 5 → Task 6
```

over maximum throughput.

The architecture can be changed back to parallel execution when higher API quotas are available.

---

## 📈 Future Improvements

ResearchMind can be extended in several directions.

### 1. Parallel Research

Run independent research tasks concurrently when API limits permit.

```text
             ┌→ Research 1
Planner ─────┼→ Research 2
             ├→ Research 3
             ├→ Research 4
             ├→ Research 5
             └→ Research 6
```

This would significantly reduce total execution time.

---

### 2. Persistent Memory

Add persistent research memory so that previous research can be reused.

Potential technologies:

* ChromaDB
* FAISS
* PostgreSQL + pgvector

This would allow ResearchMind to answer follow-up questions without repeating the entire research process.

---

### 3. Better Source Ranking

Introduce source-quality scoring based on:

* Relevance
* Authority
* Recency
* Citation frequency
* Domain reliability

---

### 4. Fact Verification Agent

Add a dedicated verification agent between research and writing:

```text
Research
   ↓
Fact Verification
   ↓
Writer
   ↓
Critic
```

This could identify conflicting claims and unsupported statements before the final report is generated.

---

### 5. Research Memory

Store previous research sessions so users can:

* Reopen previous reports
* Compare research over time
* Ask follow-up questions
* Reuse previously collected evidence

---

### 6. Improved Agent Observability

Track:

* Agent execution time
* Token usage
* API requests
* Search latency
* Number of sources
* Failure/retry counts

This would make the platform easier to monitor in a production environment.

---

### 7. Human-in-the-Loop Research

Allow users to approve or modify the generated research plan before the agents begin searching.

```text
Topic
  ↓
AI Planner
  ↓
Human Approval
  ↓
Research
  ↓
Writer
```

This would make the system more controllable for high-stakes research.

---

## 🧪 Testing

The project contains a dedicated Gemini connectivity test:

```bash
python test_gemini.py
```

This can be used to verify that:

* The virtual environment is active
* The Gemini SDK is installed
* The API key is available
* The configured Gemini model is accessible

---

## ⚠️ API Limits

ResearchMind relies on external APIs and therefore inherits their request and quota limitations.

In particular, free-tier LLM usage can impose request-per-minute limits.

The current implementation reduces unnecessary requests by:

* Running research sequentially
* Making the Critic optional
* Avoiding unnecessary LLM calls
* Using structured responses where appropriate

For larger workloads, higher API quotas or a paid API plan may be required.

---

## 🔒 Security

Sensitive credentials should never be committed to source control.

The project `.gitignore` excludes:

```text
.env
venv/
__pycache__/
*.pyc
```

Only environment variable names should appear in source code.

For production deployment, secrets should be managed using a dedicated secret-management system rather than local `.env` files.

---

## 📊 Example Output

For the research topic:

```text
What is Data Engineering?
```

ResearchMind may produce tasks such as:

```text
1. Definition and Core Concepts
2. Data Engineering Architecture
3. Data Pipelines and ETL
4. Modern Data Platforms
5. Data Engineering Tools
6. Future Trends
```

Each task is researched independently before the findings are synthesized into the final report.

---

## 🎯 Learning Objectives

This project was built to develop practical understanding of:

* Large Language Model APIs
* Prompt engineering
* Multi-agent systems
* Agent orchestration
* Retrieval-augmented workflows
* Web-grounded LLM applications
* Structured LLM outputs
* Pydantic validation
* API integration
* Concurrency and rate limiting
* Streamlit application development
* PDF generation
* Environment and secret management
* Modular Python architecture

---

## 🧠 Key Takeaway

ResearchMind demonstrates how a complex research workflow can be decomposed into specialized AI components rather than relying on a single monolithic LLM call.

The core architecture is:

```text
             User
              │
              ▼
           Planner
              │
              ▼
        Research Tasks
              │
              ▼
          Researchers
              │
              ▼
          Web Evidence
              │
              ▼
            Writer
              │
              ▼
        Final Research
              │
        ┌─────┴─────┐
        ▼           ▼
      PDF         Critic
                  │
                  ▼
             AI Evaluation
```

This architecture provides a foundation for extending ResearchMind into a more sophisticated autonomous research system with persistent memory, fact verification, source ranking, human approval, and parallel agent execution.

---

## 👨‍💻 Author

**Siddharth Ranganatha**

Built as a practical exploration of AI/ML engineering, LLM applications, multi-agent systems, and research automation.

---

## 📄 License

This project is available for educational and portfolio purposes.
