from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from email.message import EmailMessage
import os, smtplib, time
from datetime import datetime

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT", "")
SEND_TIME = os.getenv("SEND_TIME", "23:33")

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
    debug_mode = False
)

if __name__ == "__main__":
    from prompt import NEWSLETTER_PROMPT
    agent.run(NEWSLETTER_PROMPT)
    
    print(f"Agendamento de envio para {SEND_TIME}...")
    last_sent_date = None
    
    while True:
        now = datetime.now()
        
        if now.strftime("%H:%M") == SEND_TIME and last_sent_date != now.date():
            print("Enviando newsletter...")
            
            try:
                prompt_data = f"DATA: {now:'%d/%m/%Y'}\n\n {NEWSLETTER_PROMPT}"
                agent.run(prompt_data)
                last_sent_date = now.date()
                print("Newsletter enviada com sucesso.")
                time.sleep(65)
            
            except Exception as e:
                print(f"Erro ao gerar ou enviar a newsletter: {str(e)}")
                time.sleep(10)
        else:
            time.sleep(10)
    
