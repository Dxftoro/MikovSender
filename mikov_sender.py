import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email import encoders
import os
import sys
import json

script_dir = os.path.dirname(sys.argv[0])
def settings_load():
	settings = {}
	with open(os.path.join(script_dir, "config.json"), encoding="utf-8") as file:
		settings = json.load(file)

	return settings

def parse_name(fpath):
    filename = ""
    labnum = ""
    author = ""

    for i in reversed(range(len(fpath))):   
        if fpath[i] == ".":
            labnum = fpath[i - 1]
        if fpath[i] == "\\":
            break

        filename = fpath[i] + filename
    
    for v in filename:
        if v == "_":
            break
        else:
            author = author + v
    
    return (filename, author, labnum)

filepath = input("Введите путь к файлу или перетащите сам файл сюда: ")
filepath = filepath.replace('"', '')

print("Загружаем настройки...\n")
settings = settings_load()
info_tuple = parse_name(filepath)

print("Визуальная информация: ", info_tuple)

message_title = str(settings["group"]) + ", " + str(settings["subgroup"]) + ", " + info_tuple[1] + ", Лаб " + info_tuple[2]
print("Тема сообщения: ", message_title + "\n")

sender_mail = settings["sender"]
app_password = settings["app_password"]
receiver_mail = settings["receiver"]

message = MIMEMultipart()
message["From"] = sender_mail
message["To"] = receiver_mail
message["Subject"] = Header(message_title, "utf-8")
message.attach(MIMEText(settings["description"], "html", "utf-8"))

part = MIMEApplication(open(filepath, "rb").read(), "vnd.openxmlformats-officedocument.wordprocessingml.document", Name=info_tuple[0])
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename=info_tuple[0])
message.attach(part)

print("Отправляем сообщение по адресу " + settings["receiver"] + "...")
smtp_server = smtplib.SMTP(host=settings["host"], port=settings["port"])
smtp_server.starttls()
smtp_server.login(sender_mail, app_password)

smtp_server.sendmail(sender_mail, receiver_mail, message.as_string())

smtp_server.quit()

print("Сообщение успешно отправлено!\n")