import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

"""
inputs:
	fromaddr
	toaddr
	from_pass

Original code can be found here:
http://naelshiab.com/tutorial-send-email-python/
"""


def send_mail(fromaddr, toaddr, from_pass):

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = 'Code Complete'
	 
	body = 'your code is complete'
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, from_pass)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()


