from cryptography.fernet import Fernet 
from insert1 import *

# generate a key for encryptio and decryption 
#key = Fernet.generate_key() 

key=b'add-your-key'
#print(key)
# Instance the Fernet class with the key 

def encryption(msg):
    fernet = Fernet(key) 

# be encoded to byte string before encryption 
    enc = fernet.encrypt(msg.encode()) 

    #print("original string: ", msg) 
    #print("encrypted string: ", enc) 

    
    res=enc.decode('utf-8')
    return res
# decrypt the encrypted string with the 
# Fernet instance of the key, 
# that was used for encrypting the string 
# encoded byte string is returned by decrypt method, 
# so decode it to string with decode methos 

def decryption(cipher):
    fernet = Fernet(key)
    cipher=cipher.encode()
    dec = fernet.decrypt(cipher).decode() 

    print("decrypted string: ", dec) 

    return dec


#msg=input("enter the message: ")
#enc=encryption(msg)
#enc1=enc
#print("encrypted one: "+enc)
#print("decrypted one: "+decryption(enc))
#register(enc)
