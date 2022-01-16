import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from Config.var_env import info


smtp_connection = smtplib.SMTP('smtp.gmail.com', 587)
email = info["EMAIL"]
password = info["SENHA"]


def connect_server():
    try:
        smtp_connection.ehlo()
        smtp_connection.starttls()
        smtp_connection.login(email, password)
    except:
        pass


def send_email(email_to, filename):
    connect_server()
    email_msg = MIMEMultipart()
    email_msg['From'] = email
    email_msg['To'] = email_to
    email_msg['Subject'] = 'Arquivo com Livros'
    msg = "Livros"
    email_msg.attach(MIMEText(msg, 'plain'))
    filename_read = str(filename).encode(encoding="utf-8")
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(filename_read)
    encoders.encode_base64(att)
    att.add_header('content-disposition', f'attachment', filename=f'livros.json')
    email_msg.attach(att)
    smtp_connection.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
