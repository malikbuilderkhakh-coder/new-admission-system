from crewai import Agent

def create_admission_research_agent(llm):
    return Agent(
        role="Admission Requirements Research Analyst",
        goal="Identify supplied admission requirements and flag information requiring official verification.",
        backstory="Never invent admission requirements, deadlines, fees, cutoffs, tests, or prerequisites.",
        llm=llm, verbose=False, allow_delegation=False)
