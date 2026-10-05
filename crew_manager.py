from crewai import Agent, Crew, LLM, Process, Task
from config import MODEL_NAME
from data_loader import load_admission_data

def run_admission_crew(profile: dict, api_key: str) -> str:
    llm = LLM(model=MODEL_NAME, api_key=api_key, temperature=0.2, max_tokens=2200)

    research = Agent(
        role="Admission Requirements Research Analyst",
        goal="Analyze supplied admission information without inventing requirements.",
        backstory="Carefully analyze Pakistani university admission information. Never invent deadlines, fees, cutoffs, tests, or prerequisites.",
        llm=llm, verbose=False, allow_delegation=False)

    eligibility = Agent(
        role="Student Eligibility Evaluation Analyst",
        goal="Give a careful preliminary eligibility assessment.",
        backstory="Compare the student profile with supplied requirements. Distinguish eligibility from final merit and never guarantee admission.",
        llm=llm, verbose=False, allow_delegation=False)

    recommendation = Agent(
        role="Degree Program Recommendation Advisor",
        goal="Recommend suitable degree fields based on the student profile.",
        backstory="Advise Pakistani students about suitable study fields without inventing university offerings.",
        llm=llm, verbose=False, allow_delegation=False)

    guidance = Agent(
        role="Admission Process Guidance Advisor",
        goal="Provide a practical admission checklist and next steps.",
        backstory="Understand common Pakistani admission processes and clearly mark information that requires official verification.",
        llm=llm, verbose=False, allow_delegation=False)

    report = Agent(
        role="Final Admission Report Writer",
        goal="Combine all findings into a clear student-friendly report.",
        backstory="Write simple reports that separate supported information, preliminary assessment, recommendations, and verification items.",
        llm=llm, verbose=False, allow_delegation=False)

    profile_text = "\n".join(f"- {k}: {v}" for k, v in profile.items())
    data = load_admission_data()

    t1 = Task(
        description=f"""Analyze this student profile and local admission data.
STUDENT:
{profile_text}
DATA:
{data}
Identify supported facts, missing information, and items requiring official verification. Never invent university-specific facts.""",
        expected_output="Concise admission research note.", agent=research)

    t2 = Task(
        description=f"""Evaluate preliminary eligibility for this student:
{profile_text}
Use the research findings. Explain likely eligibility only where supported, missing requirements, and why final admission cannot be guaranteed.""",
        expected_output="Careful preliminary eligibility assessment.", agent=eligibility, context=[t1])

    t3 = Task(
        description=f"""Recommend suitable degree fields for:
{profile_text}
Use previous findings. Do not invent university offerings, fees, deadlines, or rules.""",
        expected_output="Suitable study directions with reasons.", agent=recommendation, context=[t1,t2])

    t4 = Task(
        description=f"""Create an admission action plan for:
{profile_text}
Include documents to prepare, entry-test preparation, application steps, and items to verify. Do not guess university-specific requirements.""",
        expected_output="Practical admission checklist.", agent=guidance, context=[t1,t2,t3])

    t5 = Task(
        description=f"""Write the final report for:
{profile_text}
Use these sections:
# Admission Summary
# Preliminary Eligibility
# Recommended Study Areas
# Admission Action Plan
# Information That Must Be Verified
# Final Advice
Do not guarantee admission or invent facts.""",
        expected_output="Clear final admission guidance report in Markdown.",
        agent=report, context=[t1,t2,t3,t4])

    crew = Crew(
        agents=[research,eligibility,recommendation,guidance,report],
        tasks=[t1,t2,t3,t4,t5],
        process=Process.sequential, verbose=False)
    return str(crew.kickoff())
