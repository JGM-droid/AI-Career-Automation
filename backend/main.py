from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class JobRequest(BaseModel):
    resume: str
    job_description: str


class AnalysisResponse(BaseModel):
    match_score: int
    missing_skills: list[str]
    recommended_projects: list[str]
    summary: str


@app.get("/")
def home():
    return {"message": "AI Career Research Agent Backend Running"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_job(request: JobRequest):

    resume_text = request.resume
    job_text = request.job_description

    score = 75

    if "python" in resume_text.lower():
        score += 10

    if "aws" in resume_text.lower():
        score += 10

    missing_skills = []

    if "docker" in job_text.lower() and "docker" not in resume_text.lower():
        missing_skills.append("Docker")

    if "aws" in job_text.lower() and "aws" not in resume_text.lower():
        missing_skills.append("AWS")

    recommended_projects = []

    if "python" in resume_text.lower():
        recommended_projects.append("AI Career Research Agent")

    if "machine learning" in resume_text.lower():
        recommended_projects.append("Neural Network Diabetes Classification")

    return {
        "match_score": score,
        "missing_skills": missing_skills,
        "recommended_projects": recommended_projects,
        "summary": "Resume analyzed against job description."
    }