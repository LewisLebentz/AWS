import smtplib

# Specifying the from and to addresses

fromaddr = 'from@from.com'
toaddrs  = 'to@to.com'

# Writing the message (this message will appear in the email)

msg = 'Enter you message here'

# Login

username = 'user@gmail.com'
password = 'password'

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
