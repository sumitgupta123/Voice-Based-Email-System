from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib
import imaplib, email
from tts import *
from azurestt import *
from signup import confirm,take_inp
from valid_email import *
from read_mail_option import *
from name_email import *
from update_details import *

def search_nickname():
    while True:
        text_to_speech("enter the nickname, character by character input is required")
        nickname = speech_to_text()
        nickname = mod_inp(nickname)
        text_to_speech("you have entered")
        text_to_speech_char(nickname)
        text_to_speech("say yes to continue or anything else to re-enter")
        flag = speech_to_text()
        if flag != "yes":
            continue
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "account_info"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM name_email")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == nickname:
                return x[1],1
        return "",0

def send_mail(mail_id,passw):
    while True:
        text_to_speech('Do you want search for email-id by providing nickname')
        text_to_speech('say yes to continue or anything else to go ahead by providing email id')
        name_ch=speech_to_text()
        res=0
        if(name_ch=='yes'):
            email,res=search_nickname()
            
        if(res==0 or name_ch!='yes'):
            to_email=take_inp('email ID of the recipient ')
        else:
            to_email=email

        #to_email+='@gmail.com'
        if(check_val(to_email)):
            text_to_speech('this email ID exists')
            break
        else:
            text_to_speech('this email ID does not exists, say yes to re enter the email ID and anything else to go to previous menu')
            ch=speech_to_text()
            if(ch=='yes'):
                continue
            else:
                return
    
    text_to_speech('please say the email subject')

    sub=speech_to_text()
    
    msg=MIMEMultipart('alternative')
    msg['From']=mail_id
    msg['To']=to_email
    msg['Subject']=sub

    #msg1='hello my name is sumit'
    text_to_speech('please say the mail content')
    msg1=speech_to_text()
    text_to_speech('mail content given is '+msg1)

    txt_part=MIMEText(msg1,'plain')
    msg.attach(txt_part)
    msg_str=msg.as_string()

    s= smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()

    s.login(mail_id,passw)

    s.sendmail(mail_id, to_email, msg_str)
    text_to_speech('mail has been sent successfully')

    s.quit()

    text_to_speech('you can store this email by providing a nickname and that can be used later by just providing the nickname')
    text_to_speech('say yes to store that and anything else to go back to previous menu')
    ch=speech_to_text()
    if(ch=='yes'):
        store_email(to_email)
    else:
        return

def go_back_check():
    text_to_speech('please say yes to stay on this page and hear the choices again and anything else to goto main menu')
    ch=speech_to_text()
    if(ch=='yes'):
        return 1
    else:
        return 0


def menu_func(username,mail_id,passw):
    while True:
        text_to_speech("choice available are")
        text_to_speech("say send to send an email")
        text_to_speech("say read to read an email")
        text_to_speech("say update to update the details")
        text_to_speech("say exit to go back to previous menu")
        text_to_speech("say anything else to hear the choice again")
        
        ch4="say the choice"
        text_to_speech(ch4)
        #print(ch4)
        #choice=int(input())
        choice=speech_to_text()
        text_to_speech("you have said the choice "+ choice)
        text_to_speech("say yes to continue, and anything else to re-enter the choice")
        cnf=speech_to_text()
        if(cnf=='yes'):
            if(choice=='send'):
                send_mail(mail_id,passw)
                if(go_back_check()):
                    continue
                else:
                    break
            elif(choice=='read'):
                read_mail(mail_id,passw)
                if(go_back_check()):
                    continue
                else:
                    break
            elif(choice=='update'):
                update_details(username)
                if(go_back_check()):
                    continue
                else:
                    break

            elif(choice=='exit'):
                text_to_speech('going back to main menu menu')
                break
            else:
                text_to_speech("going to hear the choice again")
                continue
        else:
            continue


#read_mail('sg99ready@gmail.com','ready@123')
