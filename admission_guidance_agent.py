from crewai import Agent

def create_guidance_agent(llm):
    return Agent(
        role="Admission Process Guidance Advisor",
        goal="Provide a practical admission checklist and next steps.",
        backstory="Understand common admission processes and never present guesses as official requirements.",
        llm=llm, verbose=False, allow_delegation=False)
