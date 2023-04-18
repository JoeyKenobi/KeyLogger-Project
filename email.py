import smtplib as slib

def send_mail(self, email, password, message):
    server = slib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

send_mail('completelogggerproject@gmail.com', 'Thisisthepa22word!', 'hi', 'this is the message')
