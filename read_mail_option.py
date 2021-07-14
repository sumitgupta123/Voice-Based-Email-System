import os
import smtplib
import imaplib, email
from tts import *
from azurestt import *


def find_body(email_msg):
    if email_msg.is_multipart():
        for part in email_msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
                body = body.decode()
                return body

            elif part.get_content_type() == "text/html":
                continue

def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data


def search_sub(con,x):
    while True:
        text_to_speech("please say the subject to search mail ")
        sub=speech_to_text()
        text_to_speech("you said the subject as "+sub)
        text_to_speech("say yes to continue and no to re enter the subject and anything else to go back to previous menu")
        ch=speech_to_text()

        if(ch=='no'):
            continue
        
        elif(ch=='yes'):
            i=0
            for num in x:
                typ, data = con.fetch(num, '(RFC822)')
                raw = email.message_from_bytes(data[0][1])
                if(raw['Subject']==sub):
                    i=i+1

            text_to_speech("there are total "+str(i)+" mails matching this subject")
            if(i!=0):
                text_to_speech("say yes to read out the recent mail and print all mails matching this subject and anything else to go back")
                ch1=speech_to_text()
                if(ch1=='yes'):
                        k=1
                        for num in x:
                            typ, data = con.fetch(num, '(RFC822)')
                            raw = email.message_from_bytes(data[0][1])
                            if(raw['Subject']==sub):
                                print('from:'+raw['From'])
                        #text_to_speech(raw['From'])
                                print('to:'+raw['To'])
                                print('sub:'+raw['Subject'])
                                print("mail content: ")
                                body=find_body(raw)
                                print(body)
                                if(k==1):
                                    text_to_speech('audio output for first mail')
                                    text_to_speech('mail from '+raw['From'])
                                    text_to_speech('mail subject'+raw['Subject'])
                                    text_to_speech('mail content is '+body)
                                    k=k+1
                        text_to_speech("all mails seen and going back to previous menu")
                        return
                else:
                    text_to_speech("going back to previous menu")
                    return
            else:
                text_to_speech("going back to previous menu")
                return
        else:
            text_to_speech("going back to previous menu")
            return


def read_one(con,x):
    k=1
    for num in x:
        typ, data = con.fetch(num, '(RFC822)')
        raw = email.message_from_bytes(data[0][1])
        print('from:'+raw['From'])
         #text_to_speech(raw['From'])
        print('to:'+raw['To'])
        print('sub:'+raw['Subject'])
        print("mail content: ")
        body=find_body(raw)
        print(body)
        if(k==1):
            text_to_speech('audio output for first mail')
            text_to_speech('mail from '+raw['From'])
            text_to_speech('mail subject'+raw['Subject'])
            text_to_speech('mail content is '+body)
            k=k+1

def read_mail(mail_id,passw):
    imap_url = 'imap.gmail.com'
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(mail_id,passw)
#print(con.list())
    con.select('INBOX')
    type, data = con.search(None, 'ALL')
    x=data[0].split()    
    x.reverse()

    text_to_speech("total "+str(len(x))+" mails are there in inbox")

    type, data = con.search(None, 'UNSEEN')
    y=data[0].split()
    y.reverse()
    text_to_speech("total "+str(len(y))+" unseen mails are there in inbox")

    text_to_speech("you can search mail or read mails as in the order of recent to older one")
    while True:
        text_to_speech("say search to check the mail by subject")
        text_to_speech("say unseen to check the unseen mails ")
        text_to_speech("say all to show all mails") 
        text_to_speech("exit to go back to previous menu")
        text_to_speech('say anything else to hear the choices again')
        
        text_to_speech("say the choice")
        
        ch2=speech_to_text()
        text_to_speech("you selected the choice "+ch2)
        text_to_speech("say yes to continue and anythign else to re enter")
        ch3=speech_to_text()
        if(ch3=='yes'):
            if(ch2=='search'):
                search_sub(con,x)
            elif(ch2=='unseen'):
                if(len(y)==0):
                    text_to_speech("no unseen mails to check, you can try other options")
                    continue
                else:
                    text_to_speech("showing the unseen mails")
                    read_one(con,y)
                    text_to_speech("you can try other option as well")
                    continue
            elif(ch2=='all'):
                if(len(x)==0):
                    text_to_speech("no mails to check, you can try other options")
                    continue
                else:
                    text_to_speech("showing the all mails")
                    read_one(con,x)
                    text_to_speech("you can try other option as well")
                    continue
            elif(ch2=='exit'):
                text_to_speech('going back to previous menu')
                return
            else:
                continue

        else:
            continue

