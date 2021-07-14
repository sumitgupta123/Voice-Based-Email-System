from tts import *
from gtts import gTTS

def text_to_speech_char(val):
    for i in val:
    	if(i=='.'):
    		text_to_speech('dot')
    	elif(i=='_'):
    		text_to_speech('underscore')
    	elif(i=='#'):
    		text_to_speech("hash")
    	else:
        	text_to_speech(i)



    


