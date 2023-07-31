import smtplib
from email.message import EmailMessage


print("Email application started...Please wait...")
msg=EmailMessage()

msg['Subject']="Python tutorial"
msg['From']="keshavtrikha@gmail.com"
msg['To']="ranbirtrikha@gmail.com"
msg.set_content('Hello there/ this is demo email')
Myserver = smtplib.SMTP('smtp.gmail.com',587)
Myserver.starttls
Myserver.login('keshavtrikha08@gmail.com',"hpntgodehvanvdcz")
Myserver.send_message(msg)
Myserver.quit()
print('Email sent successfully')
