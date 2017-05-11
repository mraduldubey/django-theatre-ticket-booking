import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def autoreply(toaddr):
	"""SEnd reply to contact submission."""

	fromaddr = "mraduldubeymd19@gmail.com"
	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Contact mDeommerce reply"

	body = "Thanks for contacting us. We will get back to you after processing your submission.  Mradul Dubey, CEO, eCommerce Django Project"

	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "PASSWORD FOR FROMADDR")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
