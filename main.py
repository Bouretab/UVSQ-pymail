import smtplib
import json

email = "jan.bellon-huet@ens.uvsq.fr"

cred_file = open('webmail/cred.json')
cred = json.load(cred_file)

password = cred['password']
login = cred['login']

cred_file.close()

receiver = input('Receiver : ')

with smtplib.SMTP_SSL('smtps.uvsq.fr', 465) as smtp:

    smtp.login(login, password)

    subject = input('\nSubject : ')
    body = input('\nBody : ')

    message = "Subject: {}\n\n{}".format(subject, body)

    print(f'\nMessage : {message}\n')

    smtp.sendmail(email, [receiver], message)

    print('Email sent successfully !')