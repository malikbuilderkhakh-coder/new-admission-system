from crewai import Agent


def create_report_agent(llm):
    """
    Creates the final report-writing agent.
    """

    return Agent(
        role="Admission Report Writer",

        goal=(
            "Combine the findings from the other admission agents into "
            "a clear, organized, student-friendly admission report."
        ),

        backstory=(
            "You are an experienced educational report writer. "
            "You create simple and understandable admission reports for students "
            "and parents. "
            "You clearly separate confirmed information, preliminary assessment, "
            "and information that still needs verification. "
            "You never guarantee university admission."
        ),

        llm=llm,
        verbose=False,
        allow_delegation=False,
    )
