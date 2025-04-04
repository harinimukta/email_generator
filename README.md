✉️ Job Email Generator with Smart Portfolio Matching
This project is a Streamlit-based web application that generates personalized job outreach emails by scraping job descriptions from company career pages. It intelligently matches your tech portfolio to the job requirements and customizes the emails accordingly. You can optionally send the email via SMTP.

✨ Cold Email Generator
Scrapes job descriptions from career URLs.

Extracts job role and required skills using LLM (LangChain).

Matches job requirements with your skills and portfolio.

Generates customized emails for each role.

Supports email etiquette customization based on regions (US, Europe, Asia, etc.).

Sends emails using your Gmail account (via secure app password).

Also supports local rendering of emails without sending.

🗂️ Project Structure
bash
Copy
Edit
.
├── main.py                  # Entry point for the Chat Assistant (PDF & URL QA)
├── mailsend.py             # Entry point for the Job Email Generator + Email Sending
├── chains.py / chaindemo.py # LLM-based job extraction and email writing logic
├── portfolio.py            # Loads and queries tech stack portfolio links
├── utils.py                # Helper functions (e.g., text cleaning)
├── requirements.txt        # All dependencies
├── .env                    # Environment variables (API keys, passwords)
└── README.md               # You're here!
🛠️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/job-email-generator.git
cd job-email-generator
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add Environment Variables
Create a .env file with the following:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
If you're using email functionality:

env
Copy
Edit
EMAIL_ID=your_email@gmail.com
EMAIL_APP_PASSWORD=your_generated_app_password
🚀 Running the Applications
Run the PDF & URL Chat Assistant
bash
Copy
Edit
streamlit run main.py
Run the Cold Email Generator
bash
Copy
Edit
streamlit run mailsend.py
🧠 How It Works
LLM (LangChain): Extracts job roles and skills from text.

Portfolio Matcher: Checks if your portfolio contains relevant projects/tech stacks.

Email Generator: Writes a tailored email for each matched job.

SMTP Integration: Sends the emails through Gmail (optional).

📬 Email Sending Note
If you want to enable email sending:

Enable 2-step verification in your Gmail account.

Generate an App Password via Google account settings.

Use that in .env as EMAIL_APP_PASSWORD.

🧱 Built With
Streamlit

LangChain

Groq

ChromaDB

BeautifulSoup

HuggingFace Embeddings

SpeechRecognition

pyttsx3

💡 Future Ideas
Add support for LinkedIn job links.

Track email open and click rates.

Auto-schedule email sending.

Add feedback mechanism on email success.

