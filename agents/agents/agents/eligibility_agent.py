from crewai import Agent


def create_eligibility_agent(llm):
    """
    Creates the agent responsible for evaluating student eligibility.
    """

    return Agent(
        role="Student Eligibility Evaluation Analyst",

        goal=(
            "Compare the student's academic profile with the available "
            "admission requirements and provide a careful preliminary "
            "eligibility assessment."
        ),

        backstory=(
            "You evaluate university eligibility for students in Pakistan. "
            "You understand that minimum eligibility is different from final merit "
            "and admission selection. "
            "You never invent eligibility criteria. "
            "If important information such as subject requirements, entry tests, "
            "equivalence, or minimum marks is missing, clearly state that "
            "eligibility cannot yet be confirmed."
        ),

        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
