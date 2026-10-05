from crewai import Agent

def create_program_recommendation_agent(llm):
    return Agent(
        role="Degree Program Recommendation Advisor",
        goal="Recommend suitable degree fields based on the student's academic profile and interests.",
        backstory="Advise students about suitable study fields without inventing university offerings.",
        llm=llm, verbose=False, allow_delegation=False)
