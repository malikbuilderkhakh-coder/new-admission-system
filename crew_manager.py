from crewai import Crew, Process, Task, LLM
from agents.admission_research_agent import create_admission_research_agent
from agents.eligibility_agent import create_eligibility_agent
from agents.program_recommendation_agent import create_program_recommendation_agent
from agents.admission_guidance_agent import create_guidance_agent
from agents.admission_report_agent import create_report_agent
from data_loader import load_admission_data

def run_admission_crew(profile: dict, api_key: str) -> str:
    """
    Create five specialized CrewAI agents and run them in sequence.
    Each agent uses the same Groq model, but has a different responsibility.
    """
    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
        temperature=0.2,
        max_tokens=2200,
    )

    research_agent = create_admission_research_agent(llm)
    eligibility_agent = create_eligibility_agent(llm)
    recommendation_agent = create_program_recommendation_agent(llm)
    guidance_agent = create_guidance_agent(llm)
    report_agent = create_report_agent(llm)

    admission_data = load_admission_data()
    profile_text = "\n".join(f"- {key}: {value}" for key, value in profile.items())
    data_text = str(admission_data)

    research_task = Task(
        description=(
            "Review the student profile and the admission data supplied below. "
            "Extract only criteria supported by the data. State that the included dataset is illustrative "
            "and may be incomplete or outdated. Do not claim to have browsed the web. List what official "
            "information must be verified for the student's preferred field and location.\n\n"
            f"STUDENT PROFILE:\n{profile_text}\n\nAVAILABLE ADMISSION DATA:\n{data_text}"
        ),
        expected_output="A short research note separating supplied facts, unverified requirements, and official checks needed.",
        agent=research_agent,
    )

    eligibility_task = Task(
        description=(
            "Using the student profile and the preceding research note, evaluate preliminary eligibility. "
            "Do not invent cutoffs. If exact official criteria are unavailable, return 'Cannot determine yet' "
            "and explain exactly what evidence is missing. Distinguish minimum eligibility from merit/selection.\n\n"
            f"STUDENT PROFILE:\n{profile_text}"
        ),
        expected_output="A cautious eligibility assessment with reasons, unknowns, and any subject/test checks needed.",
        agent=eligibility_agent,
        context=[research_task],
    )

    recommendation_task = Task(
        description=(
            "Recommend up to five program areas or program-search targets aligned with the student's interests, "
            "qualification, location, university preference, and budget. Do not invent university offerings. "
            "If the supplied dataset does not verify a specific program, label it as a search target rather than "
            "a confirmed offering. Explain reach/match/safer options only when evidence supports the distinction.\n\n"
            f"STUDENT PROFILE:\n{profile_text}"
        ),
        expected_output="A ranked shortlist of program areas/search targets with reasons and verification needs.",
        agent=recommendation_agent,
        context=[research_task, eligibility_task],
    )

    guidance_task = Task(
        description=(
            "Create a practical next-step checklist for the student. Include likely documents to prepare as a "
            "general checklist, entry-test questions to confirm, official pages to locate, and questions to ask "
            "admission offices. Do not invent dates, fees, or official policy.\n\n"
            f"STUDENT PROFILE:\n{profile_text}"
        ),
        expected_output="A practical checklist with general items clearly distinguished from university-specific requirements.",
        agent=guidance_agent,
        context=[research_task, eligibility_task, recommendation_task],
    )

    report_task = Task(
        description=(
            "Write the final Markdown report for the student. Use these headings: Profile Summary, "
            "Eligibility Assessment, Recommended Program Directions, What Must Be Verified, Action Plan, "
            "Important Disclaimer. Clearly label any uncertain point. Do not claim live research or official "
            "eligibility. Keep it useful and beginner-friendly."
        ),
        expected_output="A complete Markdown admission guidance report.",
        agent=report_agent,
        context=[research_task, eligibility_task, recommendation_task, guidance_task],
    )

    crew = Crew(
        agents=[
            research_agent,
            eligibility_agent,
            recommendation_agent,
            guidance_agent,
            report_agent,
        ],
        tasks=[
            research_task,
            eligibility_task,
            recommendation_task,
            guidance_task,
            report_task,
        ],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()
    return str(result)
