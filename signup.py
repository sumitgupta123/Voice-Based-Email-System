from azurestt import *
from tts import *
from twilio_verify import *
from valid_email import *
from modify_input import *
from tts_char import text_to_speech_char
from insert1 import *
from encryption import *
import mysql.connector


def check_mob(mobile_no):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "account_info"
            )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM signup_data")
    myresult = mycursor.fetchall()
    flag = 0
    for x in myresult:
        if x[2] == mobile_no:
            flag =1
            break
    if flag == 1:
        return 0 #mobile number found 
    else: 
        return 1


def confirm(val):
    text_to_speech("you said:")
    text_to_speech_char(val)
    text_to_speech("say yes to continue and anything else to re enter")
    inp=speech_to_text()
    if(inp=='yes'):
        return 1
    else:
        return 0

def take_inp(field):
    while True:
        text_to_speech("please say the "+field)
        val=speech_to_text()
        out=mod_inp(val)
        print(out)
        if(confirm(out)==1):
            return out
        else:
            continue

def main_fun():

    text_to_speech("SIGN UP PAGE")


    usr=take_inp('username')

    pass1=take_inp('password')
    
    while True:
        mob=take_inp("mobile number")
        if(check_mob(mob)==0):
            text_to_speech('This mobile number already exists with some other account')
            text_to_speech('say yes to re enter the mobile number and anything else to go back to main menu')
            ch=speech_to_text()
            if(ch=='yes'):
                continue
            else:
                return
        res=send_otp(mob)
        if(res==1):
            text_to_speech("this mobile no is successfully approved")
            break
        else:
            text_to_speech("authentication failed ")
            text_to_speech('say yes to re enter the mobile number and anything else to go back to main menu')
            ch=speech_to_text()
            if(ch=='yes'):
                continue
            else:
                return


    dob=take_inp("date of birth in ddmmyyyy format")
    
    

    while True:
            email_id=take_inp("Email ID")

        #email_id=speech_to_text()
            #email_id+='@gmail.com'

            if(check_val(email_id)):
                text_to_speech("this Email ID exists")
                break
            else:
                text_to_speech("this Email ID does not exists, try again")
                continue

    while True:
                pass2=take_inp("email password")

                if(check_account(email_id,pass2)):
                    text_to_speech("credentials are correct")
                    break
                else:
                    text_to_speech("this password does not match with given Email ID,try again")
                    continue

    return usr,pass1,mob,dob,email_id,pass2


#usr,pass1,mob,dob,email_id,pass2=main_fun()
#pass1=encryption(pass1)
#pass2=encryption(pass2)
#register(usr,pass1,mob,dob,email_id,pass2)
#take_inp("password")
