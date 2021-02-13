import pandas
import smtplib

my_email = "XXX@gmail.com"  # Change Here
my_password = "XXX"  # Change Here

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(my_email, my_password)

email_list = pandas.read_excel('excel_sheet.xlsx')

count = 0
names = email_list['NAME_COLUMN']  # Change Here
emails = email_list['EMAIL_COLUMN']  # Change Here

for single in range(len(emails)):
    name = names[single]
    email = emails[single]

    # Change Name Below & Add Your Message.

    message = """From: YOUR NAME <""" + my_email + """>
To: """ + name + """ <""" + email + """>
MIME-Version: 1.0
Content-type: text/html
Subject: SRM Buddies - New App Released

YOUR MESSAGE GOES HERE...
"""
    server.sendmail(my_email, [email], message)
    count += 1
    print("Sent To: " + name + " Done(Total): " + str(count))
server.close()
