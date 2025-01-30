import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chaindemo import Chain
from portfolio import Portfolio
from utils import clean_text
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to send email using SMTP
def send_email(to_email, subject, body):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "muktaharini@gmail.com"  # Replace with your email
        sender_password = "kpvz zwem dqkm lqks"  # Use the generated app password here

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return True, body
    except Exception as e:
        return False, str(e)


# Function to create the Streamlit app
def create_streamlit_app(llm, portfolio, clean_text):
    st.markdown('<div class="main-title">📧 Job Email Generator</div>', unsafe_allow_html=True)

    # Input fields
    url_input = st.text_input("Enter a URL:", 
                               value="https://careers.microsoft.com/us/en/search-results?keywords=software%20engineering", 
                               key="url_input")
    recipient_email = st.text_input("Enter recipient email address (optional):", 
                                    value="", 
                                    key="email_input", 
                                    placeholder="recipient@example.com")

    # Dropdown for region selection
    region = st.selectbox(
        "Select the region for email etiquette:",
        options=["Default", "US", "Europe", "Asia", "Australia"],
        key="region_select"
    )

    # Generate email button
    submit_button = st.button("Generate Email", key="submit_btn")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            email_body = ""

            for job in jobs:
                role = job.get("role", "Unknown Role")
                skills = job.get("skills", [])
                matching_links = []

                # Check if at least one skill matches the tech stacks in the portfolio
                for skill in skills:
                    links = portfolio.query_links([skill])
                    if links:
                        matching_links.extend(links)

                # If any matching links are found, include them in the email
                if matching_links:
                    email = llm.write_mail(job, matching_links, region)
                else:
                    # If no matches, generate email without links
                    email = llm.write_mail(job, None, region)

                email_body += f"Job Role: {role}\n{email}\n\n"

            if email_body:
                if recipient_email:
                    success, message = send_email(recipient_email, f"Job Opportunities in {region}", email_body)
                    if success:
                        st.success("Email sent successfully!", icon="✅")
                        st.markdown("### Sent Email Content:")
                        st.markdown(f'<div class="email-content">{message}</div>', unsafe_allow_html=True)
                    else:
                        st.error(f"Failed to send email: {message}")
                else:
                    st.markdown("### Generated Email Content:")
                    st.markdown(f'<div class="email-content">{email_body}</div>', unsafe_allow_html=True)
            else:
                st.warning("No job descriptions found.")
        except Exception as e:
            st.error(f"An Error Occurred: {e}")
if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Email Generator", page_icon="✉️")
    create_streamlit_app(chain, portfolio, clean_text)
