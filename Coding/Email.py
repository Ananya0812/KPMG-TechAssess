import smtplib
sender_email = "ananyashah0812.as@gmail.com"
rec_email = "ananya.shah@myprosperity.com.au"
password = input(str("Please enter your password: "))
message = "Hey sent this using python!"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email sent to", rec_email)
