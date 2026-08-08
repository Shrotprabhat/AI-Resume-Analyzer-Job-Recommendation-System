import pandas as pd


def extract_skills(cleaned_text):

    skills_df = pd.read_csv("data/skill_dictionary.csv")

    detected_skills = []

    categorized_skills = {}

    cleaned_text = cleaned_text.lower()

    for _, row in skills_df.iterrows():

        category = row["Category"]

        skill = row["Skill"]

        if skill.lower() in cleaned_text:

            detected_skills.append(skill)

            if category not in categorized_skills:
                categorized_skills[category] = []

            categorized_skills[category].append(skill)

    detected_skills = sorted(list(set(detected_skills)))

    for category in categorized_skills:

        categorized_skills[category] = sorted(
            list(set(categorized_skills[category]))
        )

    return detected_skills, categorized_skills