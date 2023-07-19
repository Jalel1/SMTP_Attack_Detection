import smtplib
import socket

from email.mime.text import MIMEText

#info de connexion au serveur SMTP & Messagerie

smtp_server = 'smtp.gmail.com'

smtp_port = 587

smtp_username = 'adresse@email.com'

smtp_password = 'mot de passe'

sender_email = 'adresse@email.com'

recipient_email = 'adresse_destinataire@email.com'

#Mail d'alerte

alert_message = f'Une Attaque a été détectée !!! '

#Connection au serveur SMTP

smtpObj = smtplib.SMTP(smtp_server, smtp_port)

smtpObj.starttls()

smtpObj.login(smtp_username, smtp_password)

#Recupération d'adresse ip locale du sys

ipaddress = socket.gethostbyname(socket.gethostbyname())

#Envoi Mail d'alerte

msg = MIMEText(alert_message)

msg['From'] = sender_email

msg['To'] = recipient_email

smtpObj.sendmail(sender_email, recipient_email, msg.as_string())

#Déconnexion du serveur SMTP
smtpObj.quit()

print('Alerte envoyée avec succés ')
