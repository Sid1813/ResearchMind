from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


class PDFService:

    def export(self, report):

        filename = "outputs/research_report.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>Research Report</b>", styles["Title"]))

        story.append(
            Paragraph(
                "<b>Executive Summary</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                report.executive_summary,
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                "<b>Detailed Analysis</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                report.detailed_analysis,
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                "<b>Key Takeaways</b>",
                styles["Heading2"]
            )
        )

        for takeaway in report.key_takeaways:

            story.append(
                Paragraph(
                    f"• {takeaway}",
                    styles["BodyText"]
                )
            )

        story.append(
            Paragraph(
                "<b>Conclusion</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                report.conclusion,
                styles["BodyText"]
            )
        )

        doc.build(story)

        return filename