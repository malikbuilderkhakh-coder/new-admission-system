# Pakistan University Admission Advisor

Beginner-friendly Streamlit + CrewAI multi-agent admission guidance system.

## Structure

```text
new-admission-system/
├── agents/
│   ├── __init__.py
│   ├── admission_research_agent.py
│   ├── eligibility_agent.py
│   ├── program_recommendation_agent.py
│   ├── admission_guidance_agent.py
│   └── admission_report_agent.py
├── data/
│   └── admission_data.json
├── app.py
├── config.py
├── crew_manager.py
├── data_loader.py
├── requirements.txt
├── runtime.txt
└── README.md
```

## Streamlit

Use `app.py` as the main file and Python 3.12. Add this to Streamlit Secrets:

```toml
GROQ_API_KEY = "your_actual_groq_api_key"
```

The JSON data file is only a starter dataset. Verify current university information from official sources.

This system provides guidance and does not guarantee admission.
