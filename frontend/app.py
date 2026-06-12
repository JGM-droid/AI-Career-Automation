import requests
import streamlit as st


ANALYZE_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="AI Career Automation System", layout="wide")

st.title("AI Career Automation System")

st.write(
    "Paste a job description and upload your resume to get AI-powered analysis."
)

job_description = st.text_area(
    "Paste Job Description",
    height=300,
    placeholder="Paste the full job description here..."
)

uploaded_resume = st.file_uploader(
    "Upload Your Resume",
    type=["txt"]
)

if st.button("Analyze Job"):
    if not job_description.strip():
        st.warning("Please paste a job description.")
    elif not uploaded_resume:
        st.warning("Please upload your resume.")
    else:
        try:
            resume_text = uploaded_resume.read().decode("utf-8")
        except UnicodeDecodeError:
            st.error("The resume could not be read. Please upload a UTF-8 text file.")
        else:
            request_data = {
                "resume": resume_text,
                "job_description": job_description,
            }

            try:
                response = requests.post(
                    ANALYZE_URL,
                    json=request_data,
                    timeout=10,
                )
            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to the backend. Make sure FastAPI is "
                    "running at http://127.0.0.1:8000."
                )
            except requests.exceptions.Timeout:
                st.error("The backend took too long to respond. Please try again.")
            except requests.exceptions.RequestException as error:
                st.error(f"The analysis request failed: {error}")
            else:
                if response.status_code != 200:
                    st.error(
                        "The backend returned an error "
                        f"(HTTP {response.status_code})."
                    )
                else:
                    try:
                        analysis = response.json()
                    except ValueError:
                        st.error("The backend returned invalid JSON.")
                    else:
                        required_fields = {
                            "match_score",
                            "missing_skills",
                            "recommended_projects",
                            "summary",
                        }

                        if not isinstance(analysis, dict) or not required_fields.issubset(
                            analysis
                        ):
                            st.error("The backend response is missing required fields.")
                        else:
                            st.subheader("Analysis Results")
                            st.metric("Match Score", analysis["match_score"])

                            st.write("**Missing Skills**")
                            if analysis["missing_skills"]:
                                for skill in analysis["missing_skills"]:
                                    st.write(f"- {skill}")
                            else:
                                st.write("No missing skills detected.")

                            st.write("**Recommended Projects**")
                            if analysis["recommended_projects"]:
                                for project in analysis["recommended_projects"]:
                                    st.write(f"- {project}")
                            else:
                                st.write("No project recommendations yet.")

                            st.write("**Summary**")
                            st.write(analysis["summary"])
