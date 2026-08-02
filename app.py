import time

import streamlit as st

from orchestrator.pipeline import ResearchPipeline
from services.pdf_service import PDFService


st.set_page_config(
    page_title="ResearchMind",
    page_icon="🧠",
    layout="wide"
)

# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.title("🧠 ResearchMind")

    st.markdown("---")

    st.markdown(
        """
### Features

- ✅ AI Planning
- ✅ Web Search (Tavily)
- ✅ Multi-Agent Pipeline
- ✅ AI Writer
- ✅ Optional AI Critic
- ✅ PDF Export
- ✅ Structured Output (Pydantic)
"""
    )

    st.markdown("---")

    st.caption("Version 1.0")


# ============================================================
# Main UI
# ============================================================

st.title("🧠 ResearchMind")
st.subheader("Autonomous Multi-Agent Research Platform")

topic = st.text_input(
    "Research Topic",
    placeholder="Future of Agentic AI"
)

evaluate_report = st.checkbox(
    "Evaluate final report using AI (uses one extra Gemini request)",
    value=False
)

if st.button("Generate Research Report"):

    if not topic:
        st.warning("Please enter a research topic.")
        st.stop()

    start_time = time.time()

    pipeline = ResearchPipeline()

    progress = st.progress(0)

    status = st.empty()
    status.info("🧠 Planner Agent is creating a research plan...")

    plan, evidence, report, review = pipeline.run(
        topic,
        evaluate_report=evaluate_report
    )

    progress.progress(100)

    status.success("✅ Research pipeline completed successfully!")

    execution_time = round(
        time.time() - start_time,
        2
    )

    st.success("Research Complete!")

    # ============================================================
    # Dashboard Metrics
    # ============================================================

    total_tasks = len(plan.tasks)

    total_sources = sum(
        len(item.sources)
        for item in evidence
    )

    review_score = (
        f"{review.score}/100"
        if review is not None
        else "N/A"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Research Tasks",
            total_tasks
        )

    with col2:
        st.metric(
            "Sources Collected",
            total_sources
        )

    with col3:
        st.metric(
            "AI Quality Score",
            review_score
        )

    with col4:
        st.metric(
            "Execution Time",
            f"{execution_time}s"
        )

    # ============================================================
    # Agent Status
    # ============================================================

    st.divider()

    st.header("🤖 Agent Execution Status")

    col1, col2 = st.columns(2)

    with col1:

        st.success("🧠 Planner Agent Completed")

        st.success("🔍 Research Agents Completed")

    with col2:

        st.success("✍️ Writer Agent Completed")

        if review is not None:
            st.success("🧐 Critic Agent Completed")
        else:
            st.info("🧐 Critic Agent Skipped")

    # ============================================================
    # Research Plan
    # ============================================================

    st.divider()

    st.header("📋 Research Plan")

    for task in plan.tasks:

        with st.expander(
            f"Task {task.id}: {task.title}"
        ):

            st.write(task.description)

    # ============================================================
    # Research Findings
    # ============================================================

    st.divider()

    st.header("📚 Research Findings")

    for item in evidence:

        with st.expander(item.title):

            st.subheader("📝 Summary")
            st.write(item.findings)

            st.subheader("🔗 Sources")

            for source in item.sources:

                st.markdown(
                    f"- [{source.title}]({source.url})"
                )

    # ============================================================
    # Final Report
    # ============================================================

    st.divider()

    st.header("📄 Final Research Report")

    st.subheader("Executive Summary")
    st.write(report.executive_summary)

    st.subheader("Detailed Analysis")
    st.write(report.detailed_analysis)

    st.subheader("Key Takeaways")

    for takeaway in report.key_takeaways:

        st.markdown(
            f"- {takeaway}"
        )

    st.subheader("Conclusion")
    st.write(report.conclusion)

    # ============================================================
    # Download PDF
    # ============================================================

    pdf_service = PDFService()

    pdf_path = pdf_service.export(
        report
    )

    with open(pdf_path, "rb") as file:

        st.download_button(
            label="📄 Download Research Report (PDF)",
            data=file,
            file_name="Research_Report.pdf",
            mime="application/pdf"
        )

    # ============================================================
    # AI Review
    # ============================================================

    if review is not None:

        st.divider()

        st.header("🧐 AI Quality Review")

        st.metric(
            "Overall Score",
            f"{review.score}/100"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Strengths")

            for strength in review.strengths:

                st.markdown(
                    f"- {strength}"
                )

        with col2:

            st.subheader("⚠️ Weaknesses")

            for weakness in review.weaknesses:

                st.markdown(
                    f"- {weakness}"
                )

        st.subheader("🚀 Suggested Improvements")

        for improvement in review.improvements:

            st.markdown(
                f"- {improvement}"
            )