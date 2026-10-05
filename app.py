import streamlit as st
from config import get_groq_api_key
from crew_manager import run_admission_crew

st.set_page_config(page_title="Pakistan University Admission Advisor", page_icon="🎓")
st.title("🎓 Pakistan University Admission Advisor")
st.write("Preliminary university admission guidance using five CrewAI agents.")

with st.form("student_form"):
    name = st.text_input("Student Name")
    qualification = st.selectbox("Current Qualification", ["FSc Pre-Engineering","FSc Pre-Medical","ICS","ICom","FA","A Levels","Other"])
    intermediate_marks = st.number_input("Intermediate / HSSC Percentage", 0.0, 100.0, 70.0)
    matric_marks = st.number_input("Matric / SSC Percentage", 0.0, 100.0, 75.0)
    preferred_field = st.text_input("Preferred Field", placeholder="e.g. Computer Science")
    city = st.text_input("Preferred City", placeholder="e.g. Lahore, Islamabad, Multan")
    university_type = st.selectbox("Preferred University Type", ["Public","Private","Any"])
    budget = st.text_input("Approximate Budget", placeholder="e.g. 150000 PKR per semester")
    entry_test_status = st.selectbox("Entry Test Status", ["Not taken","Taken","Not required / Unknown"])
    entry_test_score = st.text_input("Entry Test Score (optional)")
    notes = st.text_area("Additional Information / Goals")
    submitted = st.form_submit_button("Generate Admission Report")

if submitted:
    if not name.strip():
        st.error("Please enter the student's name.")
        st.stop()
    profile = {
        "name": name, "qualification": qualification,
        "intermediate_marks": f"{intermediate_marks}%",
        "matric_marks": f"{matric_marks}%",
        "preferred_field": preferred_field or "Not specified",
        "city": city or "Not specified",
        "university_type": university_type,
        "budget": budget or "Not specified",
        "entry_test_status": entry_test_status,
        "entry_test_score": entry_test_score or "Not provided",
        "notes": notes or "None",
    }
    try:
        with st.spinner("The admission agents are preparing your report..."):
            report = run_admission_crew(profile, get_groq_api_key())
        st.success("Admission report generated.")
        st.markdown(report)
        st.download_button("Download Report", report, "admission_report.txt", "text/plain")
    except Exception as exc:
        st.error("The admission system encountered an error.")
        st.code(str(exc))

st.divider()
st.caption("Guidance only. Always verify current eligibility, merit, fees, deadlines, tests, and documents from official university sources.")
