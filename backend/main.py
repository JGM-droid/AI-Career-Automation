from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class JobRequest(BaseModel):
    resume: str
    job_description: str


@app.get("/")
def home():
    return {"message": "AI Career Research Agent Backend Running"}


@app.post("/analyze")
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

    return {
        "match_score": score,
        "missing_skills": missing_skills,
        "summary": f"Resume analyzed against job description."
    }