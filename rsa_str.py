import rsa 
from insert1  import *
# key length should be atleast 16 
#publicKey, privateKey = rsa.newkeys(512) 

pub=rsa.key.PublicKey(8886297596606721013952439413611701085288337169299991322868189589717711134982395136567572725372948936903683499650059723897013053300591368019991430170638393, 65537)

pvt=rsa.key.PrivateKey(8886297596606721013952439413611701085288337169299991322868189589717711134982395136567572725372948936903683499650059723897013053300591368019991430170638393, 65537, 5533648034165691003561545461478357767241441143419777314762251634129873336401962583708381841618379809913304772584427750835020896245115236857538201874286897, 6909683811165553896004685137989433831017543004104469368879814613127218287827177077, 1286064288824200737428663555063487744602649673560564623900332841046381109)


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
