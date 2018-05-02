#!/usr/bin/env python3
# -- coding: utf-8 --

import email
import poplib

login = input('bellopcl@gmail.com')
password = input('Savi1990')
pop_server = 'pop-mail.gmail.com'
pop_port = 995

mail_box = poplib.POP3_SSL(pop_server, pop_port)
mail_box.user(login)
mailbox.pass_(password)
numMessages = len(mail_box.list()[1])

if numMessages > 15:
    numMessages = 15
for i in range(15):
    (server_msg, body, octets) = mail_box.retr(i+1)
    for j in body:
        try:
            msg = email.message_from_string(j.decode("utf-8"))
            strtext = msg.get_payload()
            print(strtext)
        except:
            pass