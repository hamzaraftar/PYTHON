import smtplib

my_email = "hamzarafter765@gmail.com"
password = "xfkjeswphscjvncm"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

subject = "Subject: Test Email\n\n"
body = "Hello"
msg = subject + body

connection.sendmail(from_addr=my_email, to_addrs="hamzaraftar851@gmail.com", msg=msg)
connection.close()