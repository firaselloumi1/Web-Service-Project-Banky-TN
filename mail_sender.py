import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

subject = "Verify Firas Finance Account"

def generate_template(userid, verification_code, verification_url):
    html_template = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f4f7fc;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                color: #2a2a2a;
            }}
            .header h2 {{
                font-size: 28px;
                margin: 0;
                color: #2e7d32;
            }}
            .content {{
                margin: 20px 0;
                font-size: 16px;
                color: #333333;
                line-height: 1.6;
            }}
            .content h3 {{
                font-size: 24px;
                font-weight: bold;
                color: #007bff;
                margin-top: 10px;
            }}
            .btn {{
                display: inline-block;
                padding: 15px 25px;
                margin-top: 20px;
                background-color: #007bff;
                color: #ffffff;
                text-decoration: none;
                font-size: 18px;
                font-weight: bold;
                border-radius: 5px;
                text-align: center;
            }}
            .footer {{
                font-size: 14px;
                color: #999999;
                text-align: center;
                margin-top: 40px;
            }}
            .footer a {{
                color: #007bff;
                text-decoration: none;
            }}
            .footer a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>Your Firas Finance Account Verification</h2>
            </div>
            <div class="content">
                <p>Hello {userid},</p>
                <p>Thank you for signing up with Firas Finance. To complete your account setup, please use the verification code below:</p>
                <h3>{verification_code}</h3>
                <p>Alternatively, you can click the button below to verify your email directly:</p>
                <a href="{verification_url}" class="btn">Verify Your Email</a>
            </div>
            <div class="footer">
                <p>If you did not request this, please ignore this email.</p>
                <p>Best Regards, <br> The Firas Finance Team</p>
                <p><a href="https://www.firasfinance.com">Visit Our Website</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

def send_email(to_email: str, userid: str, verification_code: str, verification_url: str):
    try:
        msg = MIMEMultipart()
        msg["From"] = os.getenv('EMAIL')  # Get sender's email from environment variables
        msg["To"] = to_email
        msg["Subject"] = subject

        body = generate_template(userid, verification_code, verification_url)
        msg.attach(MIMEText(body, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(os.getenv('EMAIL'), os.getenv('EMAIL_PASS'))  
            server.send_message(msg)

        print(f"Verification email sent to {to_email} successfully.")
        return True

    except Exception as e:
        print(f"Could not send email. Reason: {e}")
        return False

# Example usage
if __name__ == "__main__":
    recipient_email = "recipient@example.com"  # Replace with the actual recipient's email
    userid = "abcd"  # Replace with the actual user ID
    verification_code = "ABC123"  # Replace with the actual verification code
    verification_url = "https://www.firasfinance.com/verify?code=ABC123"  # Replace with actual verification URL
    send_email(recipient_email, userid, verification_code, verification_url)
