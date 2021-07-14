import mysql.connector
from twilio_verify import *
from tts import *
from azurestt import *
from tts_char import * 
#from signup import take_inp,confirm
from modify_input import *


def enter_pass(mobile_no,mycursor,mydb,trial):
#needs preprocessing
    while True:
        #password=take_inp('New Password')
        text_to_speech("Enter a new password")
        password = speech_to_text()
        password=mod_inp(password)                 
        text_to_speech("you have entered password as ")
        text_to_speech_char(password)                                   
        text_to_speech("say yes to continue or no to re-enter the password")
        ind = speech_to_text()
        if ind == "yes" or ind == "YES":
            sql = "UPDATE signup_data SET usr_pass = %s where mob_no = %s"
            val = (password,mobile_no)
            mycursor.execute(sql,val)
            mydb.commit()
            text_to_speech("your password has been successfully updated")
            text_to_speech("Now you will be directed to main menu")
            break
        elif ind == "NO" or ind == "no":
            if trial == 0:
                text_to_speech("you have exceded the limit, returning to main menu")
                return
                #main menu
            else:
                trial = trial-1
                #enter_pass(mobile_no,mycursor,mydb,trial)
                continue
        else:
            if trial == 0:
                text_to_speech("you have exceded the limit, returning to main menu")
                return 
            else:
                trial = trial -1
                text_to_speech("Enter the right choice")
                continue


def check_account():
    text_to_speech("Enter your phone number associated with voice mail account")
    mobile_no = speech_to_text()   #needs preprocessing
    text_to_speech("you have entered your phone number as")
    text_to_speech_char(mobile_no)
    text_to_speech("say yes to continue, no to enter again, and anything else for main menu")
    flag = speech_to_text()
    if flag == "YES" or flag == "yes":
        return mobile_no
    elif flag == "NO" or flag == "no":
        check_account()
    else:
        return -1  #main_menu 

def forgot_pass():
    trial = 2
    mobile_no = check_account()
    if mobile_no == -1:
        return
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "account_info"
        )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from signup_data")
    myresult = mycursor.fetchall()
    flag = 0

    for x in myresult:
        if x[2] == mobile_no:
            flag = 1
            break

    if flag == 0:
        text_to_speech("Such number does not exists")
        #goto main menu
    else:
        result = send_otp(mobile_no)
        if result == 0:
            text_to_speech("Verification failed, redirecting to the main menu")
        else:
            enter_pass(mobile_no,mycursor,mydb,trial)

            
#forgot_pass()