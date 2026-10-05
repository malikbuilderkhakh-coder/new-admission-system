from crewai import Agent


def create_guidance_agent(llm):
    """
    Creates the agent responsible for admission process guidance.
    """

    return Agent(
        role="Admission Process Guidance Advisor",

        goal=(
            "Provide the student with a practical admission checklist, "
            "including documents, entry-test preparation, application steps, "
            "and important information that should be verified."
        ),

        backstory=(
            "You understand common university admission processes in Pakistan. "
            "You know that every university can have different requirements. "
            "You provide general guidance but never present guessed deadlines, "
            "fees, documents, or policies as official university requirements."
        ),

        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
