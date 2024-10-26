import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(message, 'plain'))

    # Start SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the sender's email account
    server.login(sender_email, sender_password)

    # Send email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully!")


if __name__ == "__main__":
    # Set the sender's email and password
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"

    # Set the recipient's email
    receiver_email = "recipient_email@example.com"

    # Set the email subject and message
    subject = "Test Email"
    message = "This is a test email sent from Python."

    # Call the send_email function
    send_email(sender_email, sender_password, receiver_email, subject, message)
