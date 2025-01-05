import smtplib
my_email = "kamigood723@gmail.com"
password = 'password'

connection = smtplib.SMTP("smtp.gmail.com" , 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="hamzaasghar803@yahoo.com" , msg="Hello")
connection.close()