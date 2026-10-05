import streamlit as st
from config import get_groq_api_key
from crew_manager import run_admission_crew

st.set_page_config(
    page_title="Pakistan University Admission Advisor",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Pakistan University Admission Advisor")
st.caption("A beginner-friendly multi-agent admission guidance MVP for students in Pakistan.")

with st.sidebar:
    st.header("About this app")
    st.write(
        "Five AI agents help organize admission information, compare your profile "
        "with available criteria, suggest programs, and prepare an action plan."
    )
    st.warning(
        "This is guidance, not an official admission decision. Requirements and "
        "deadlines change. Confirm every important detail on the university's official website."
    )

try:
    api_key = get_groq_api_key()
except Exception as exc:
    st.error(str(exc))
    st.stop()

st.subheader("1. Your academic profile")

col1, col2 = st.columns(2)
with col1:
    student_name = st.text_input("Name (optional)")
    qualification = st.selectbox(
        "Current / completed qualification",
        ["FSc Pre-Engineering", "FSc Pre-Medical", "ICS", "ICom", "FA", "A-Levels", "DAE", "Other"],
    )
    intermediate_percentage = st.number_input(
        "Intermediate / equivalent percentage",
        min_value=0.0, max_value=100.0, value=75.0, step=0.5,
        help="If you have not completed it, enter your latest available percentage and explain that in notes.",
    )
    matric_percentage = st.number_input(
        "Matric / O-Level equivalent percentage",
        min_value=0.0, max_value=100.0, value=80.0, step=0.5,
    )

with col2:
    preferred_field = st.selectbox(
        "Preferred field",
        [
            "Computer Science", "Software Engineering", "Artificial Intelligence",
            "Cybersecurity", "Engineering", "Medicine / Dentistry",
            "Business / Management", "Accounting / Finance", "Social Sciences",
            "Natural Sciences", "Not sure yet",
        ],
    )
    preferred_city = st.selectbox(
        "Preferred city / area",
        ["Any city in Pakistan", "Islamabad / Rawalpindi", "Lahore", "Karachi",
         "Peshawar", "Quetta", "Multan", "Faisalabad", "Other"],
    )
    university_type = st.selectbox("University preference", ["Any", "Public", "Private"])
    budget = st.selectbox(
        "Approximate tuition budget",
        ["Not decided", "Low budget / prefer public universities",
         "Up to PKR 100,000 per semester", "PKR 100,000–250,000 per semester",
         "Above PKR 250,000 per semester"],
    )

st.subheader("2. Entry test and extra information")
col3, col4 = st.columns(2)
with col3:
    entry_test_status = st.selectbox(
        "Entry test status",
        ["Not taken yet", "Taken — score available", "Registered / waiting for result", "Not sure whether required"],
    )
with col4:
    entry_test_score = st.text_input("Entry test name and score (if any)", placeholder="e.g., university test, 72/100")

extra_notes = st.text_area(
    "Other details (optional)",
    placeholder="For example: preferred universities, subject marks, domicile, scholarship need, or whether results are awaiting.",
)

st.info(
    "For a reliable eligibility comparison, the app needs current, official criteria for each specific program. "
    "The starter dataset is illustrative and is not a complete or live list of Pakistani admissions."
)

if st.button("Analyze my admission options", type="primary", use_container_width=True):
    if intermediate_percentage == 0 and qualification not in ["Other"]:
        st.warning("Please enter your latest intermediate/equivalent percentage. Enter 0 only if that is your actual result.")
    else:
        profile = {
            "student_name": student_name.strip() or "Student",
            "qualification": qualification,
            "intermediate_percentage": intermediate_percentage,
            "matric_percentage": matric_percentage,
            "preferred_field": preferred_field,
            "preferred_city": preferred_city,
            "university_type": university_type,
            "budget": budget,
            "entry_test_status": entry_test_status,
            "entry_test_score": entry_test_score.strip() or "Not provided",
            "extra_notes": extra_notes.strip() or "None",
        }
        with st.spinner("The five agents are preparing your admission guidance. This can take a few minutes..."):
            try:
                report = run_admission_crew(profile, api_key)
                st.session_state["admission_report"] = report
                st.session_state["admission_profile"] = profile
            except Exception as exc:
                st.error("The admission analysis could not be completed.")
                st.code(str(exc))
                st.caption(
                    "Check that GROQ_API_KEY is correctly configured in Streamlit Secrets, "
                    "the model is enabled for your Groq account, and your API quota is available."
                )

if "admission_report" in st.session_state:
    st.divider()
    st.subheader("3. Your admission guidance report")
    st.markdown(st.session_state["admission_report"])
    st.download_button(
        "Download report as Markdown",
        data=st.session_state["admission_report"],
        file_name="admission_guidance_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
