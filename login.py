from signup import confirm,take_inp
from tts import *
from modify_input import *
import mysql.connector

def check_login(usrn,passd):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="account_info"
        )

    except:
        print("!!!ERROR in connecting to the DATABASE!!!")

    mycursor = mydb.cursor()
    sql="SELECT * from signup_data where usrname = %s and usr_pass = %s"
    val=(usrn,passd,)
    mycursor.execute(sql,val)

    myresult = mycursor.fetchall()

    if(len(myresult)==1):
        return myresult[0][4],myresult[0][5],1
    else:
        return "","",0


def log_in():
    #text_to_speech("Note: username and password are provided character by character")

    usr_nm=take_inp('username')

    passw=take_inp('password')
    #usr_nm="sumit"
    #passw="233dfsd332"

    email,passw,res=check_login(usr_nm,passw)

    if(res==1):
        text_to_speech("credentials are correct, successfully logged in")
        return usr_nm,email,passw,1

    else:
        text_to_speech("wrong credentials")
        return "",email,passw,0

#print(log_in())










