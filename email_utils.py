# email_utils.py
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_blueprint_email(recipient_email: str, client_name: str):
    msg = EmailMessage()
    msg["Subject"] = "Your Soul Blueprint is Ready ✨"
    msg["From"] = SMTP_EMAIL
    msg["To"] = recipient_email

    msg.set_content(f"Hi {client_name},\n\nYour Soul Blueprint is ready! Please find your personalized PDF attached.\n\nWith warmth,\nSoul Aligned")

    msg.add_alternative(f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color:#6D28D9;">Hi {client_name},</h2>
            <p>Your <strong>Soul Blueprint</strong> is ready ✨</p>
            <p>We've attached your personalized report as a PDF. We hope it brings you clarity and joy on your path.</p>
            <br>
            <p>With warmth,<br><strong>Soul Aligned</strong></p>
        </body>
    </html>
    """, subtype="html")

    # Attach the PDF
    with open("soul_blueprint.pdf", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="Your_Soul_Blueprint.pdf"
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
