import re

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


SKILL_PATTERNS = {
    "Python": [r"python"],
    "SQL": [r"sql"],
    "FastAPI": [r"fastapi"],
    "Streamlit": [r"streamlit"],
    "Docker": [r"docker"],
    "AWS": [r"aws", r"amazon web services"],
    "Git": [r"git"],
    "GitHub": [r"github"],
    "Machine Learning": [r"machine learning"],
    "APIs": [r"api", r"apis", r"rest api", r"restful api"],
    "Pandas": [r"pandas"],
    "NumPy": [r"numpy"],
    "scikit-learn": [r"scikit-learn", r"scikit learn", r"sklearn"],
}


def extract_skills(text: str) -> list[str]:
    normalized_text = text.lower()
    return [
        skill
        for skill, patterns in SKILL_PATTERNS.items()
        if any(
            re.search(rf"(?<!\w){re.escape(pattern)}(?!\w)", normalized_text)
            for pattern in patterns
        )
    ]


def recommend_projects(missing_skills: list[str]) -> list[str]:
    recommendations = []
    missing = set(missing_skills)

    if missing & {"Python", "FastAPI", "APIs"}:
        recommendations.append(
            "Build a documented FastAPI service with validation and REST endpoints."
        )
    if missing & {"SQL", "Pandas", "NumPy", "Machine Learning", "scikit-learn"}:
        recommendations.append(
            "Create a data analysis and machine learning project using SQL, Pandas, "
            "NumPy, and scikit-learn."
        )
    if missing & {"Docker", "AWS"}:
        recommendations.append(
            "Containerize an application with Docker and deploy it to AWS."
        )
    if "Streamlit" in missing:
        recommendations.append(
            "Build an interactive Streamlit dashboard for a real dataset."
        )
    if missing & {"Git", "GitHub"}:
        recommendations.append(
            "Publish a version-controlled project on GitHub with clear documentation."
        )

    return recommendations


class JobRequest(BaseModel):
    resume: str
    job_description: str


class AnalysisResponse(BaseModel):
    match_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    recommended_projects: list[str]
    summary: str
    interview_topics: list[str]


@app.get("/")
def home():
    return {"message": "AI Career Research Agent Backend Running"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_job(request: JobRequest):
    resume_skills = set(extract_skills(request.resume))
    job_skills = extract_skills(request.job_description)
    matched_skills = [skill for skill in job_skills if skill in resume_skills]
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]

    match_score = round(len(matched_skills) / len(job_skills) * 100) if job_skills else 0
    recommended_projects = recommend_projects(missing_skills)
    interview_topics = [
        f"Explain your practical experience with {skill}." for skill in job_skills
    ]

    if job_skills:
        summary = (
            f"Matched {len(matched_skills)} of {len(job_skills)} identified job skills. "
            f"Focus next on {len(missing_skills)} missing skill(s)."
        )
    else:
        summary = (
            "No predefined skills were identified in the job description. "
            "Add more technical detail for a useful comparison."
        )

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommended_projects": recommended_projects,
        "summary": summary,
        "interview_topics": interview_topics,
    }
