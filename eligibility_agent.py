from crewai import Agent

def create_eligibility_agent(llm):
    return Agent(
        role="Student Eligibility Evaluation Analyst",
        goal="Compare the student's profile with available requirements and give a preliminary assessment.",
        backstory="Distinguish minimum eligibility from final merit and never guarantee admission.",
        llm=llm, verbose=False, allow_delegation=False)
