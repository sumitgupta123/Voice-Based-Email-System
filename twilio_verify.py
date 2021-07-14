from twilio.rest import Client
from tts import *
from azurestt import *
import time

def send_otp(mob_no):

    #we are considering indian numbers only Adding country code for the indian number
    mob_no='+91'+mob_no

    client = Client('AC1eba54264335c9d30b408001920b2faf', '611c7bf543243a516eb7841d1c361a3e')

    verify = client.verify.services('VA6e6a5965296f42957bc06655be2dd7e9')

    try:
        verify.verifications.create(to=mob_no, channel='sms')

        #print("OTP SENT successfully")
        text_to_speech("OTP SENT successfully, please wait for some time")
    except:
        #print("Not able to send otp, please check the mob no")
        text_to_speech("Not able to send otp, please check the mobile number")
        exit()

    i=1
    while True:
        time.sleep(10)
        text_to_speech("Please Provide The OTP: ")
        otp=speech_to_text()

        result = verify.verification_checks.create(to=mob_no, code=otp)
        if(result.status=='approved'):
            #print("Successfully approved")
            #text_to_speech("Successfully approved")
            return 1
            break
        else:
            if(i==1):
                text_to_speech("This is wrong OTP, you are getting one more chance")
                i+=1
                continue
            else:
                text_to_speech("two times wrong otp is given, you can not process further")
                break

    return 0

#mob_no=input("please enter the mob no: ")
#print(send_otp(mob_no))

