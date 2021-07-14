import azure.cognitiveservices.speech as speechsdk
from tts import *

def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription="xxxxxxxxx(subscription id for azure", region="eastus")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    #print(result.text)
    len1=len(result.text)
    if(len1==0):
        text_to_speech('You have not provided any input')
        text_to_speech("We are getting an manual error from your side and we are exiting the system, thank you for using")
        exit()

    if(result.text[len1-1]=='.'):
        print(result.text[0:len1-1].lower())
        return result.text[0:len1-1].lower()
    else:
        print(result.text[0:len1].lower())
        return result.text[0:len1].lower()



