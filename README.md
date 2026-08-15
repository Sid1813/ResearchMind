# 🧠 ResearchMind

### Autonomous Multi-Agent Research Platform

ResearchMind is an AI-powered multi-agent research platform that transforms a broad research question into a structured, evidence-grounded research report.

The system uses specialized AI agents to **plan research, retrieve web evidence, synthesize findings, generate a report, optionally critique the result, and export the final report as a PDF.**

Built with **Python, Google Gemini, Tavily, Streamlit, Pydantic, and ReportLab**.

---

## 📸 Demo

### ResearchMind Dashboard

<!-- Add your main Streamlit screenshot here -->
<!-- Save it as: assets/dashboard.png -->

![ResearchMind Dashboard](assets/dashboard.png)

The dashboard allows users to enter a research topic and generate an end-to-end research report.

---

## 🚀 Features

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

ResearchMind uses a modular multi-agent pipeline:

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
