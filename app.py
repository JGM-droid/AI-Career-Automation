import streamlit as st

st.set_page_config(
    page_title="AI Career Automation System",
    page_icon="💼",
    layout="wide"
)

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
    type=["pdf", "docx", "txt"]
)

if st.button("Analyze Job"):

    if not job_description:
        st.warning("Please paste a job description.")

    elif not uploaded_resume:
        st.warning("Please upload your resume.")

    else:
        st.success("Resume and job description received!")

        st.subheader("Coming Next")
        st.write("Next we will connect this app to OpenAI for real analysis.")