from crewai import Agent

def create_report_agent(llm):
    return Agent(
        role="Final Admission Report Writer",
        goal="Combine findings into a clear student-friendly admission report.",
        backstory="Separate supported information, preliminary assessment, recommendations, and verification items.",
        llm=llm, verbose=False, allow_delegation=False)
