import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

def send_soul_blueprint(client_name: str, client_email: str):
    # Load credentials from .env
    load_dotenv()
    email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    # Create the message
    msg = EmailMessage()
    msg["Subject"] = f"✨ Your Soul Blueprint, {client_name} ✨"
    msg["From"] = email
    msg["To"] = client_email
    msg.set_content(
        f"""Dear {client_name},

Your Soul Blueprint is attached as a beautiful PDF, crafted with intention and soul-aligned insight.

With love,
Star Franklyn
Human Potential Advisor ✨
"""
    )

    # Attach PDF
    pdf_path = "soul_blueprint.pdf"
    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="Your_Soul_Blueprint.pdf")

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        print("Soul Blueprint sent to", client_email)
