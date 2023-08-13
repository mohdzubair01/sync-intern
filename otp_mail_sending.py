import random
import smtplib
from email.mime.text import MIMEText

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(receiver_email, otp):
    sender_email = "mohdzubair16jan@gmail.com"                           
    password = "xquuqhpihjgkgcku"                                             

    subject = "OTP Verification"
    message = f"Your OTP is: {otp}"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        if not password:
            password = input("Enter your Gmail password: ")

        server.login(sender_email, password)  

        server.sendmail(sender_email, [receiver_email], msg.as_string())
        server.quit()
        print("OTP sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Username and Password not accepted. Check your credentials.")
    except Exception as e:
        print("Error sending OTP:", e)

def verify_otp(otp, user_input_otp):
    return otp == user_input_otp

def main():
    email = input("Enter your email: ")
    otp = generate_otp()
    send_email(email, otp)

    user_input_otp = input("Enter the OTP you received: ")

    if verify_otp(otp, user_input_otp):
        print("OTP verified successfully.")
    else:
        print("Incorrect OTP. Please try again.")

if __name__ == "__main__":
    main()
