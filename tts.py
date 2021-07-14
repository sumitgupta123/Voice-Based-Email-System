from playsound import playsound
from gtts import gTTS

def text_to_speech(mytext):

    language = 'en'
    try:
        myobj = gTTS(text=mytext, lang=language, slow=False)

    except:
        print("failed to connect to server, please check your internet")
        return
    # welcome 
    myobj.save("welcome.mp3")

    # Playing the converted file 
    #os.system("mpg123 welcome.mp3")
    playsound('welcome.mp3')


#msg=input("Enter Email ID: ")
#text_to_speech("chracter by character output of email ID")
#for i in msg:
#    text_to_speech(i)





