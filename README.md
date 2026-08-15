# 🧠 ResearchMind

### Autonomous Multi-Agent Research Platform

ResearchMind is an AI-powered research platform that takes a research topic, breaks it into smaller tasks, researches each task using web search, and generates a structured research report.

It uses multiple specialized AI agents instead of relying on a single LLM call.

---

## 🚀 How It Works

```text
Research Topic
      ↓
Planner Agent
      ↓
Research Agents
      ↓
Web Search + Evidence
      ↓
Writer Agent
      ↓
Final Research Report
      ↓
Optional AI Critic
      ↓
PDF Export
```

---

## ✨ Features

* 🧠 AI-powered research planning
* 🔍 Web research using Tavily
* 🤖 Multi-agent architecture
* 📝 Automated report generation
* 🧐 Optional AI quality review
* 📄 PDF report export
* 📊 Streamlit dashboard
* 🔒 Environment-based API keys
* 🧩 Pydantic structured outputs

---

## 🖥️ Screenshots

### Main Interface

![ResearchMind](docs/screenshots/home.png)

### Research Plan & Findings

![Research Plan](docs/screenshots/research-plan.png)

### Final Report

![Final Report](docs/screenshots/final-report.png)

> **Add your screenshots to:** `docs/screenshots/`

---

## 🏗️ Project Structure

```text
ResearchMind/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── writer.py
│   └── critic.py
│
├── orchestrator/
│   └── pipeline.py
│
├── schemas/
│
├── services/
│   ├── gemini_service.py
│   ├── tavily_service.py
│   └── pdf_service.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

* **Python**
* **Google Gemini**
* **Tavily**
* **Streamlit**
* **Pydantic**
* **ReportLab**

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/sidhu2sharp/ResearchMind.git
cd ResearchMind
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API keys

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run

```bash
streamlit run app.py
```

---

## 🎯 Example

Enter:

```text
Future of Agentic AI
```

ResearchMind will automatically create research tasks, collect web evidence, generate a report, and optionally evaluate the report using the Critic Agent.

---

## 👨‍💻 Author

**Sidhu Ranganatha**
