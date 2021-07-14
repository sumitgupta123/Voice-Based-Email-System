from azurestt import *

def mod_inp(val):

    #val=speech_to_text()

    res=val.split()
    #print(res)

    mod_str=str()
    
    for word in res:
        #print(word.lower())
        if(word=='underscore'):
            mod_str+='_'
        elif(word=='dot'):
            mod_str+='.'
        elif(word=='dash'):
            mod_str+='-'
        elif(word=='at'):
            mod_str+='@'
        elif(word=='apostrophe'):
            mod_str+="'"
        elif(word=='hash'):
            mod_str+='#'
        else:
            mod_str+=word

    return mod_str




