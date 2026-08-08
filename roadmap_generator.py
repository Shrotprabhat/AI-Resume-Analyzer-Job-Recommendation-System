def generate_roadmap(missing_skills):

    roadmap = {}

    if not missing_skills:
        roadmap["Congratulations"] = [
            "Your resume already contains most of the required skills."
        ]
        return roadmap

    week = 1

    for skill in missing_skills:

        roadmap[f"Week {week}"] = [
            f"Learn {skill}",
            f"Practice {skill} using small projects"
        ]

        week += 1

    return roadmap