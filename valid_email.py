from validate_email import validate_email
import smtplib
import requests

def check_val(email_id):

    #email_address = "rajneesh1.sahay79@gmail.com"
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email_id})
    status = response.json()['status']
    if status == "valid":
        #print("email is valid")
        return 1
    elif status == "invalid":
        #print("email is invalid")
        return 0
    else:
        #print("email was unknown")
        return 0

def check_account(email_id,passw):
  
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()

    try:
        s.login(email_id,passw)

    except:

        #print("!!!!!Invalid Credentials!!!!!")
        return 0

    return 1

