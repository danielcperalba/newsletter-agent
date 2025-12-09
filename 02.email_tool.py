from email.message import EmailMessage
from dotenv import load_dotenv
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
    
if __name__ == "__main__":
    subjectTest = "Test Email from Newsletter Agent"
    contentTest = "This is a test email sent from the newsletter agent script."
    result = send_email(subjectTest, contentTest)
    print(result)
    
    reponse = send_email(subjectTest, contentTest)
    print(reponse)
