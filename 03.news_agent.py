from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from email.message import EmailMessage
import os, smtplib

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT", "")

def send_email(subject, content):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT
        
        msg.set_content(content, charset='utf-8')
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            
        return "Email sent successfully"
    
    except Exception as e:
        return f"Failed to send email: {str(e)}"

agent = Agent(
    model = OpenAIChat(id="gpt-4.1-mini"),
    tools = [
        TavilyTools(),
        send_email
    ],
    debug_mode = True
)

if __name__ == "__main__":
    from prompt import NEWSLETTER_PROMPT
    agent.run(NEWSLETTER_PROMPT)
    
