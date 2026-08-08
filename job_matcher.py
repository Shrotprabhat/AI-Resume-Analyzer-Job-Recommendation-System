import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume(cleaned_resume):

    jobs = pd.read_csv("data/job_roles.csv")

    documents = [cleaned_resume]

    documents.extend(jobs["Required Skills"].tolist())

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    resume_vector = vectors[0]

    job_vectors = vectors[1:]

    similarity_scores = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    jobs["Match Score"] = (similarity_scores * 100).round(2)

    jobs = jobs.sort_values(
        by="Match Score",
        ascending=False
    )

    return jobs