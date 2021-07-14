import rsa 
from insert1  import *
# key length should be atleast 16 
#publicKey, privateKey = rsa.newkeys(512) 

pub=rsa.key.PublicKey("generate and add rsa pub key")

pvt=rsa.key.PrivateKey('generate and add private key')

def encrypt(msg):
#message = "sumitguptajnvalwar@gmail.com"

# encode to byte string before encryption 
# with encode method 
    enc_msg = rsa.encrypt(msg.encode(), pub) 

    #print("original string: ", msg) 
    #print("encrypted string: ", enc_msg)
    return enc_msg

#print(type(encMessage))

# public key cannot be used for decryption 
def decrypt(enc_msg):
    dec_msg = rsa.decrypt(enc_msg, pvt).decode() 

    #print("decrypted string: ", dec_msg)
    return dec_msg

msg=input("enter the message: ")
enc=encrypt(msg)
enc1=enc
print("encrypted one: "+str(enc))
print("decrypted one: "+decrypt(enc))

x=enc1.decode('latin-1')
#x=x.decode('utf-8')
print(type(x))
print(x)
register(x)
