import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_resume_text
from text_cleaner import clean_resume_text
from skill_extractor import extract_skills
from job_matcher import match_resume
from roadmap_generator import generate_roadmap
from report_generator import generate_pdf


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📄 AI Resume Analyzer")

st.sidebar.markdown("---")

st.sidebar.info(
"""
### About

This application analyzes resumes and recommends suitable job roles.

Features:

• Resume Parsing

• Skill Extraction

• TF-IDF Job Matching

• Skill Gap Analysis

• Learning Roadmap

• Resume Analytics Dashboard
"""
)

st.sidebar.markdown("---")

st.sidebar.success("Built using Python + Streamlit")

# ---------------- TITLE ---------------- #

st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write("Upload a PDF or DOCX resume to begin analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

# =======================================================
# MAIN APPLICATION
# =======================================================

if uploaded_file is not None:

    st.success(f"Uploaded Successfully : {uploaded_file.name}")

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_resume_text(uploaded_file)

    cleaned_text = clean_resume_text(resume_text)

    detected_skills, categorized_skills = extract_skills(cleaned_text)

    job_matches = match_resume(cleaned_text)

    best_role = job_matches.iloc[0]

    jobs = pd.read_csv("data/job_roles.csv")

    selected_role = best_role["Job Role"]

    role_row = jobs[
        jobs["Job Role"] == selected_role
    ].iloc[0]

    required_skills = role_row["Required Skills"].split()

    found_skills = []

    missing_skills = []

    for skill in required_skills:

        if skill.lower() in cleaned_text:

            found_skills.append(skill)

        else:

            missing_skills.append(skill)

    roadmap = generate_roadmap(missing_skills)

    # ===================================================
    # DASHBOARD METRICS
    # ===================================================

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💡 Skills Found",
            len(detected_skills)
        )

    with col2:

        st.metric(
            "🎯 Best Match",
            f"{best_role['Match Score']}%"
        )

    with col3:

        st.metric(
            "❌ Missing Skills",
            len(missing_skills)
        )

    st.markdown("---")

    # ===================================================
    # CHARTS
    # ===================================================

    st.header("📊 Resume Analytics Dashboard")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        fig = px.bar(
            job_matches.head(5),
            x="Job Role",
            y="Match Score",
            color="Match Score",
            text="Match Score",
            title="Top Job Recommendations"
        )

        fig.update_traces(textposition="outside")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart_col2:

        category_names = []

        category_counts = []

        for category, skills in categorized_skills.items():

            category_names.append(category)

            category_counts.append(len(skills))

        pie = px.pie(
            names=category_names,
            values=category_counts,
            title="Skill Distribution"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    # ===================================================
    # RESUME SCORE
    # ===================================================

    st.header("⭐ Resume Score")

    resume_score = min(
        100,
        len(detected_skills) * 5
    )

    st.metric(
        "Resume Score",
        f"{resume_score}/100"
    )

    if resume_score >= 85:

        st.success("Excellent Resume ⭐⭐⭐⭐⭐")

    elif resume_score >= 70:

        st.info("Good Resume ⭐⭐⭐⭐")

    elif resume_score >= 50:

        st.warning("Average Resume ⭐⭐⭐")

    else:

        st.error("Needs Improvement ⭐⭐")
        
    # ===================================================
    # RESUME TEXT
    # ===================================================

    st.header("📄 Resume")

    with st.expander("View Extracted Resume Text", expanded=False):

        st.text_area(
            "Resume Text",
            resume_text,
            height=250
        )

    with st.expander("View Cleaned Resume", expanded=False):

        st.text_area(
            "Cleaned Resume",
            cleaned_text,
            height=220
        )

    # ===================================================
    # DETECTED SKILLS
    # ===================================================

    st.header("💡 Detected Skills")

    if detected_skills:

        st.success(f"{len(detected_skills)} Skills Detected")

        cols = st.columns(3)

        for i, skill in enumerate(detected_skills):

            cols[i % 3].success(skill)

    else:

        st.warning("No skills detected.")

    # ===================================================
    # SKILLS BY CATEGORY
    # ===================================================

    st.header("📂 Skills by Category")

    if categorized_skills:

        for category, skills in categorized_skills.items():

            with st.expander(category):

                st.write(", ".join(skills))

    # ===================================================
    # JOB RECOMMENDATIONS
    # ===================================================

    st.header("🎯 Recommended Job Roles")

    st.dataframe(
        job_matches,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        f"🏆 Best Recommendation : {best_role['Job Role']} ({best_role['Match Score']}%)"
    )

    # ===================================================
    # MATCH PROGRESS
    # ===================================================

    st.header("📈 Match Score")

    progress = max(0, min(100, int(best_role["Match Score"])))

    st.progress(progress)

    st.write(f"Overall Match Score : **{progress}%**")

    # ===================================================
    # SKILLS PRESENT
    # ===================================================

    st.header("✅ Skills Present")

    if found_skills:

        for skill in found_skills:

            st.success(skill)

    else:

        st.warning("No matching skills found.")

    # ===================================================
    # MISSING SKILLS
    # ===================================================

    st.header("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:

            st.error(skill)

    else:

        st.success("No Missing Skills 🎉")

    # ===================================================
    # LEARNING ROADMAP
    # ===================================================

    st.header("🛣 Learning Roadmap")

    for week, tasks in roadmap.items():

        with st.expander(week):

            for task in tasks:

                st.write("✔", task)

    # ===================================================
    # RESUME SUGGESTIONS
    # ===================================================

    st.header("🤖 Resume Suggestions")

    suggestions = []

    if "Git" not in detected_skills:
        suggestions.append("Add Git to your technical skills.")

    if "Docker" not in detected_skills:
        suggestions.append("Learn Docker to improve deployment skills.")

    if "AWS" not in detected_skills:
        suggestions.append("Learning AWS or another cloud platform will improve employability.")

    if "SQL" not in detected_skills:
        suggestions.append("Include SQL if you have database knowledge.")

    if len(detected_skills) < 10:
        suggestions.append("Add more technical skills and personal projects to strengthen your resume.")

    if resume_score < 70:
        suggestions.append("Improve your resume by adding certifications, internships, and measurable achievements.")

    if suggestions:

        for suggestion in suggestions:

            st.info(suggestion)

    else:

        st.success("Excellent! Your resume already contains a strong technical profile.")

    st.markdown("---")

    st.caption("© AI Resume Analyzer | Developed using Streamlit, Pandas, Scikit-learn and Plotly")
    # ===================================================
    # DOWNLOAD PDF REPORT
    # ===================================================

    st.header("📄 Download Report")

    pdf_path = generate_pdf(
        filename="Resume_Report.pdf",
        best_role=best_role["Job Role"],
        match_score=best_role["Match Score"],
        detected_skills=detected_skills,
        missing_skills=missing_skills,
        roadmap=roadmap
)

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📥 Download Resume Analysis Report",
            data=pdf_file,
            file_name="Resume_Report.pdf",
            mime="application/pdf"
        )