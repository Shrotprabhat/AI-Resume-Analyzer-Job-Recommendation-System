from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(
    filename,
    best_role,
    match_score,
    detected_skills,
    missing_skills,
    roadmap
):
    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "<b>AI Resume Analysis Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<br/>",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Best Recommended Role:</b> {best_role}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Match Score:</b> {match_score}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<br/>",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<b>Detected Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in detected_skills:
        story.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    story.append(
        Paragraph(
            "<br/>",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"]
        )
    )

    if missing_skills:
        for skill in missing_skills:
            story.append(
                Paragraph(
                    f"• {skill}",
                    styles["Normal"]
                )
            )
    else:
        story.append(
            Paragraph(
                "No missing skills.",
                styles["Normal"]
            )
        )

    story.append(
        Paragraph(
            "<br/>",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<b>Learning Roadmap</b>",
            styles["Heading2"]
        )
    )

    for week, tasks in roadmap.items():

        story.append(
            Paragraph(
                f"<b>{week}</b>",
                styles["Heading3"]
            )
        )

        for task in tasks:
            story.append(
                Paragraph(
                    f"• {task}",
                    styles["Normal"]
                )
            )

    pdf.build(story)

    return os.path.abspath(filename)