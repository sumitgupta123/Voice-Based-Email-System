import mysql.connector
from tts import *
from azurestt import *
from tts_char import * 
from modify_input import *

def check_nickname(myresult):
    while True:
        text_to_speech("please say the nickname, character by character input is required")
        flag = 0
        l2 = 0
        nickname = speech_to_text()  #preprocess
        #nickname=take_inp('nickname')
        nickname=mod_inp(nickname)
        text_to_speech("you have entered your nickname as ")
        text_to_speech_char(nickname)
        text_to_speech("say yes to continue or anything else to enter nickname again")
        l1 = speech_to_text()
        if l1 == "yes":
            l2 = 1
        if l2 != 1:
            continue
        for x in myresult:
            if nickname == x[0]:
                text_to_speech("this nickname already exists")
                text_to_speech("say choose to enter the nickname again, or anything else for main menu")
                ind = speech_to_text()
                if ind == "choose" or ind == "CHOOOSE":
                    flag = 1
                    break
                else:
                    return -1 #main menu
        if flag == 1:
            continue
        return nickname
        
    
    
def store_email(email_id):
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
        if email_id == x[1]:
            text_to_speech("this email is already stored in the list with nick name")
            text_to_speech_char(x[0])
            return

    nickname = check_nickname(myresult)
    if nickname == -1:
        return #main menu
    sql = "INSERT INTO name_email values (%s,%s)"
    val = (nickname,email_id)
    mycursor.execute(sql,val)
    mydb.commit()
    text_to_speech("the details are successfully saved ")



#store_email('dhjvbhvjverv')