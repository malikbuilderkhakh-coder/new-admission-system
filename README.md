# Pakistan University Admission Advisor — Multi-Agent MVP

A beginner-friendly Streamlit app using CrewAI and Groq to generate preliminary admission guidance for students in Pakistan.

## Features
- Five specialized CrewAI agents:
  1. Admission requirements research analyst
  2. Eligibility evaluation analyst
  3. Program recommendation advisor
  4. Admission process guidance advisor
  5. Final report writer
- Groq model: `openai/gpt-oss-120b`
- Streamlit form and downloadable Markdown report
- Modular Python files
- Streamlit Secrets for the API key

## Important limitation
This starter version does **not** perform live university web searches and does not contain a verified current university database. The JSON file is intentionally empty. The app must not be treated as an official eligibility checker. Add verified program records from official university websites and keep their source URLs and last-checked dates. Admission deadlines, eligibility, merit, fees, and entry-test rules can change.

## Files
- `app.py` — Streamlit user interface
- `config.py` — reads the API key from Streamlit Secrets
- `crew_manager.py` — builds and runs the CrewAI workflow
- `agents/` — one file for each agent
- `data/admission_data.json` — starter data structure
- `data_loader.py` — loads admission data
- `requirements.txt` — deployment dependencies
- `runtime.txt` — asks Streamlit Community Cloud to use Python 3.12

## Deploy without local setup

1. Create a new GitHub repository.
2. Upload all files and folders from this project. Keep the folder structure unchanged.
3. Open Streamlit Community Cloud and choose **Create app**.
4. Select your repository, branch, and `app.py` as the main file.
5. In Advanced settings / Secrets, add:

   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key"
   ```

6. Deploy the app. Never commit your real API key to GitHub.

## How to add verified university data
Edit `data/admission_data.json`. Add records only after checking the official university/program admission page. Include the direct official URL and date checked. Do not fill unknown fields with guesses.

## Common deployment troubleshooting
- **Missing GROQ_API_KEY:** Add the key in the Streamlit app's Secrets settings.
- **Invalid API key / model access:** Confirm the key works and the model is available in your Groq account.
- **Rate limit:** Wait for the limit to reset, reduce repeated submissions, or review your Groq plan.
- **Dependency build error:** Review Streamlit Cloud logs and confirm the pinned package versions remain compatible. Cloud environments and third-party APIs can change.
- **Eligibility appears uncertain:** Expected when no verified program criteria are available. This is intentional and safer than inventing requirements.

## Privacy
Do not collect CNIC, passwords, or unnecessary sensitive personal data in this MVP. Avoid storing student profiles unless you add an appropriate database, access controls, and a privacy policy.
