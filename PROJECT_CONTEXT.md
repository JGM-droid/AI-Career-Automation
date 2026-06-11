# AI Career Automation - Project Context

## Purpose

Build an AI-assisted career workflow that compares a resume with a job
description, identifies gaps, recommends portfolio work, and eventually supports
job-search and application automation.

## Fixed Architecture

- Backend: FastAPI
- Frontend: Streamlit
- AI provider: OpenAI

These choices are settled and should not be revisited.

## Current Repository State

- `backend/main.py` exposes a health-style root route and `POST /analyze`.
- The analysis endpoint uses Pydantic request and response models.
- FastAPI provides local Swagger documentation for testing the API.
- Current analysis is deterministic and rule-based; it does not call OpenAI.
- `frontend/app.py` collects a job description and a `.txt` resume upload.
- The frontend reads UTF-8 resume text and sends it with the job description to
  `POST http://127.0.0.1:8000/analyze`.
- The frontend renders the match score, missing skills, recommended projects,
  and analysis summary returned by the backend.
- The frontend reports invalid text encoding, request failures, invalid backend
  responses, and unavailable backend connections.
- Dependencies for FastAPI, Streamlit, HTTP requests, and OpenAI are installed.
- PDF and DOCX resume extraction are not implemented.
- Resume parsing, structured skill extraction, and AI analysis are not yet
  implemented.
- There are no automated tests, authentication, database, logging setup, README,
  deployment configuration, or CI setup.
- The `data`, `outputs`, and `prompts` directories are currently empty.

## Current Milestone

Phase 1: Foundation.

The FastAPI backend, Swagger interface, Streamlit frontend, and local
frontend/backend integration are implemented. The next milestone is Phase 2:
Resume Processing.

## Scope Order

1. Expand resume processing beyond basic `.txt` extraction.
2. Add resume parsing, skill extraction, and gap analysis.
3. Replace rule-based analysis with structured OpenAI analysis.
4. Add production capabilities such as authentication, persistence, logging,
   tests, and deployment.

## Working Constraints

- Do not create another virtual environment.
- Do not modify `.env` or commit secrets.
- Prefer small changes that can be tested immediately.
- Preserve the working `.txt` flow while adding PDF and DOCX extraction.
- Keep OpenAI integration separate from the resume-processing foundation.
- Avoid production infrastructure work until the core analysis workflow is
  stable.
