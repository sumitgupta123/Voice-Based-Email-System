import mysql.connector

def register(usr,passw,mob,dob,email,emailpass):
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

    sql = "INSERT INTO signup_data (usrname,usr_pass,mob_no,dob,email,email_pass) VALUES(%s,%s,%s,%s,%s,%s)"
    val=(usr,passw,mob,dob,email,emailpass)
    try:
        mycursor.execute(sql,val)

        mydb.commit()

    except:
        print("error in insertion")
        return 0

    if(mycursor.rowcount==1):
	#print("record inserted successfully")
        return 1
    else:
	#print("error")
        return 0

