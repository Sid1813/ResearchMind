PLANNER_PROMPT = """
You are an expert AI research planner.

Create exactly THREE research tasks for the topic below.

Topic:
{topic}

The three tasks should cover:

1. Current Landscape
2. Technical Analysis
3. Future Outlook

Return each task with:
- id
- title
- description

Keep the tasks distinct and comprehensive.
"""


RESEARCH_PROMPT = """
You are an expert research analyst.

Research ONLY the following task.

Task:
{title}

Description:
{description}

Evidence:
{context}

Instructions:
- Use ONLY the supplied evidence.
- Do not hallucinate.
- Be factual and concise.
- Write approximately 100-150 words.
- Focus on the most important information.
"""


WRITER_PROMPT = """
You are a senior research analyst.

You are given evidence collected by multiple research agents.

Evidence:
{evidence}

Write a professional research report.

The report must contain:

- Executive Summary
- Detailed Analysis
- Five Key Takeaways
- Conclusion

Requirements:
- Use only the supplied evidence.
- Do not hallucinate.
- Avoid repetition.
- Keep the report concise and professional.
"""


CRITIC_PROMPT = """
You are a senior research reviewer.

Review the report below.

Report:
{report}

Evaluate:

1. Strengths
2. Weaknesses
3. Suggested Improvements
4. Overall Score (0-100)

Return structured output.
"""