from twilio_verify import send_otp
from typing import Text
from modify_input import mod_inp
import mysql.connector
from tts import *
from azurestt import *
from tts_char import * 
import re
from valid_email import check_val,check_account

def isValid(s):
	Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
	return not Pattern.match(s)

def update_userpass(str):
    text_to_speech("say yes to update"+ str +"or anything else to go to the next field")
    ind = speech_to_text()
    if ind == "yes":
        while True:
            text_to_speech("say the new password, character by character input is required")
            field = speech_to_text()
            field = mod_inp(field)
            print(field)
            text_to_speech("you have entered")
            text_to_speech_char(field)
            text_to_speech("say yes to continue, no to re-enter, or anything else for main menu")
            ind = speech_to_text()
            if ind == "yes":
                return field
            elif ind == "no":
                continue
            else:
                return -1
    else:
        return 0

def update_mobile(username,mycursor,myresult):
    text_to_speech("say yes to update mobile number, or anything else to go to the next field")
    ind = speech_to_text()
    if ind == "yes":
        while True:
            text_to_speech("enter the mobile number")
            mobile_no = speech_to_text()
            mobile_no = mod_inp(mobile_no)
            text_to_speech("you have entered")
            text_to_speech_char(mobile_no)
            text_to_speech("say yes to continue, no to re-enter, or anything else for main menu")
            ind2 = speech_to_text()
            if ind2 == "yes":
                if isValid(mobile_no) or len(mobile_no) > 10 or len(mobile_no) < 10:
                    text_to_speech("you have entered invalid mobile number")
                    text_to_speech("say yes to re-enter, no to go to the next field, or anything else for main menu")
                    ind3 = speech_to_text()
                    if ind3 == "yes":
                        continue
                    elif ind3 == "no":
                        return 0
                    else:
                        return -1
                else:
                    flag = 0
                    for x in myresult:
                        if x[2] == mobile_no:
                            if x[0] == username:
                                text_to_speech("this mobile number is already linked with your account")
                                return mobile_no
                            else:
                                text_to_speech("this mobile number is already used in another account")
                                text_to_speech("say yes to enter mobile number again, no to go the next field, or anything else for main menu")
                                t1 = speech_to_text()
                                if t1 == "yes":
                                    flag = 1
                                    break
                                elif t1 == "no":
                                    flag = 2
                                    break
                                else:
                                    flag = 3
                                    break
                    if flag != 0:
                        if flag == 1:
                            continue
                        if flag == 2:
                            return 0
                        if flag == 3:
                            return -1
                    check = send_otp(mobile_no)
                    if check == 1:
                        text_to_speech("mobile number verified")
                        return mobile_no
                    else:
                        text_to_speech("mobile number not verified")
                        text_to_speech("say yes to enter again, no to go the next field, or anything else for main menu")
                        ind4 = speech_to_text()
                        if ind4 == "yes":
                            continue
                        elif ind4 == "no":
                            return 0
                        else:
                            return -1
            elif ind2 == "no":
                continue
            else:
                return -1
    else:
        return 0

def update_dob():
    text_to_speech("say yes to update birth details, or anything else to go to the next field")
    ind = speech_to_text()
    if ind == "yes":
        while True:
            text_to_speech("say the birth details in ddmmyyyy format")
            dob = speech_to_text()
            dob = mod_inp(dob)
            text_to_speech("you have entered")
            text_to_speech_char(dob)
            text_to_speech("say yes to continue, no to re-enter, or anything else for main menu")
            ind2 = speech_to_text()
            if ind2 == "yes":
                return dob
            elif ind2 == "no":
                continue
            else:
                return -1
    else:
        return 0

def update_gmail():
    text_to_speech("say yes to update Email ID , or anything else to go to the next field")
    ind = speech_to_text()
    if ind == "yes":
        while True:
            text_to_speech("say the Email ID character by character")
            gmail = speech_to_text()
            gmail = mod_inp(gmail)
            text_to_speech("you have entered")
            text_to_speech_char(gmail)
            text_to_speech("say yes to continue, no to re-enter, or anything else for main menu")
            ind2 = speech_to_text()
            if ind2 == "yes":
                if(check_val(gmail)):
                    return gmail
                else:
                    text_to_speech('This Email ID does not exists')
                    text_to_speech("say yes to enter again, no to go the next field, or anything else for main menu")
                    ch=speech_to_text()
                    if(ch=='yes'):
                        continue
                    elif(ch=='no'):
                        return 0
                    else:
                        return -1

            elif ind2 == "no":
                continue
            else:
                return -1
    else:
        return 0

def update_gmailpass(email1):
    text_to_speech("say yes to update the Email Password or anything else to go to the next field")
    ind = speech_to_text()
    if ind == "yes":
        while True:
            text_to_speech("say the new password, character by character input is required")
            field = speech_to_text()
            field = mod_inp(field)
            text_to_speech("you have entered")
            text_to_speech_char(field)
            text_to_speech("say yes to continue, no to re-enter, or anything else for main menu")
            ind = speech_to_text()
            if ind == "yes":
                if(check_account(email1,field)==0):
                    text_to_speech('This password does not match with the given email ID')
                    text_to_speech("say yes to enter again, no to go the next field, or anything else for main menu")
                    ch=speech_to_text()
                    if(ch=='yes'):
                        continue
                    elif(ch=='no'):
                        return 0
                    else:
                        return -1
                else:
                    return field
            elif ind == "no":
                continue
            else:
                return -1
    else:
        return 0



def update_details(username):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "account_info"
            )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT *from signup_data")
    myresult = mycursor.fetchall()

    sql="SELECT * from signup_data where usrname= %s"
    val=(username,)
    mycursor.execute(sql,val)
    myresult1=mycursor.fetchall()
    usrpass,mob,dob1,email,emailpass=myresult1[0][1],myresult1[0][2],myresult1[0][3],myresult1[0][4],myresult1[0][5]


    user_pass = update_userpass("voice mail password")
    if(user_pass==-1):
        return
    
    if(user_pass==0):
        user_pass=usrpass

    mobile_no = update_mobile(username,mycursor,myresult) 

    if(mobile_no==-1):
        return 

    if(mobile_no==0):
        mobile_no=mob

    dob = update_dob()
    if(dob==-1):
        return 

    if(dob==0):
        dob=dob1


    #print(user_pass,mobile_no,dob)
    gmail = update_gmail()
    if(gmail==-1):
        return

    if(gmail==0):
        gmail=email

    gmail_pass = update_gmailpass(gmail)
    if(gmail_pass==-1):
        return

    if(gmail_pass==0):
        gmail_pass=emailpass

    sql='UPDATE signup_data SET usr_pass= %s, mob_no= %s, dob= %s, email= %s, email_pass= %s where usrname= %s'
    val=(user_pass,mobile_no,dob,gmail,gmail_pass,username)
    mycursor.execute(sql,val)
    mydb.commit()
    text_to_speech('your details has been updated successfully')


#update_details("sgupta")