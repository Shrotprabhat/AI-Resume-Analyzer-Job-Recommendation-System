# AI Resume Analyzer & Job Recommendation System

# SUBMITTED BY
SHROT PRABHAT
AIML
JUNE BATCH (C) 

## Overview

The AI Resume Analyzer is a Streamlit-based application that analyzes resumes, extracts technical skills, recommends suitable job roles, identifies skill gaps, and generates a learning roadmap.

## Features

- Resume Parsing (PDF & DOCX)
- Resume Text Cleaning
- Skill Extraction
- Job Recommendation using TF-IDF & Cosine Similarity
- Skill Gap Analysis
- Learning Roadmap
- Resume Score
- Interactive Dashboard
- Plotly Charts
- Downloadable PDF Report

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- ReportLab
- PyPDF
- Python-docx

## Project Structure

```
AI_RESUME_ANALYZER/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── report_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
└── reports/
```

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Project developed as an AI/ML academic project using Python and Streamlit.