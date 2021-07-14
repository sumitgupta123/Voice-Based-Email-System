from tts import *
from azurestt import *
from login import *
from signup import *
from project2 import *
from change_pass import *

text_to_speech("WELCOME TO THE VOICE BASED EMAIL SYSTEM")

#LOOPING OVER THE CHOICES 
while True:
     
    text_to_speech("AVAILABLE OPTIONS ARE ")

    text_to_speech("SAY login FOR LOGIN")

    text_to_speech("SAY signup FOR SIGNUP")

    text_to_speech("SAY forgot password IF YOU HAVE SIGNED UP AND FORGOT THE PASSWORD")

    text_to_speech("SAY exit TO close the application")

    text_to_speech("SAY ANYTHING ELSE TO HEAR THE OPTIONS AGAIN")
     
    text_to_speech("PLEASE SAY THE CHOICE ")
    choice=speech_to_text()
    print("given choice: "+choice)
    
    if(choice=='login' or choice=='sign up' or choice=='forgot password' or choice=='exit'):
        text_to_speech("YOU HAVE SELECTED THE CHOICE "+choice)
        text_to_speech("SAY yes TO CONTINUE AND no TO RE-ENTER")
        choice2=speech_to_text()
        print("given choice: "+choice2)
        if(choice2=='yes'):
            if(choice=='login'):
                usrn,usr,passw,res=log_in()
                if(res==1):
                    menu_func(usrn,usr,passw)
                else:
                    text_to_speech("say yes to re enter login credentials and anything else to go back to main menu")
                    log_again_ch=speech_to_text()
                    if(log_again_ch()=='yes'):
                        usrn,usr,passw,res=log_in()
                        if(res==1):
                            menu_func(usrn,usr,passw)
                        else:
                            continue
                    else:
                        continue
            elif(choice=='sign up'):
                usr,pass1,mob,dob,email_id,pass2=main_fun()
                #pass1=encryption(pass1)
                #pass2=encryption(pass2)
                if(register(usr,pass1,mob,dob,email_id,pass2)):
                    text_to_speech("Succesfully registered, say yes to login now and anything else to go to the main menu")
                    log_ch=speech_to_text()
                    if(log_ch=='yes'):
                        usrn,usr,passw,res=log_in()
                        if(res==1):
                            menu_func(usrn,usr,passw)
                        else:
                            text_to_speech("say yes to re enter login credentials and anything else to go back to main menu")
                            log_again_ch=speech_to_text()
                            if(log_again_ch()=='yes'):
                                usrn,usr,passw,res=log_in()
                                if(res==1):
                                    menu_func(usrn,usr,passw)
                                else:
                                    continue
                        
                            else:
                                continue
                    else:
                        continue
                else:
                    text_to_speech("not able to register going back to the main menu")
                    continue
            elif(choice=='forgot password'):
                forgot_pass()
            elif(choice=='exit'):
                text_to_speech('Thank you for using our application')
                break
            else:
                continue
        else:
            continue  #want to re-enter
    else:
        continue   #want to hear the options again




