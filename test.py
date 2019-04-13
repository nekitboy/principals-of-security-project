from des import triple_des
from aes import AESModeOfOperationECB
from rsa import RSA
import os
import json
from environment import TestSecurity, serialize

key = '0' * 24
triple_des_m = triple_des(key=key, padmode=2)
t = TestSecurity('3-DES', ['123', 'Hello World', 'ASDKMASKFMASKLDMASDMKAS'*100, '123'])

results = t.run(triple_des_m.encrypt, triple_des_m.decrypt)
print(json.dumps(results, default=serialize, indent=True))

def encrypt(data):
    return encrypt(data=data)
  
key = os.urandom(16)
plaintext = bytearray('hello', 'utf-8')
while len(plaintext) % 16 != 0:
    plaintext.append(0)
plaintext = bytes(plaintext)
aes = AESModeOfOperationECB(key)
aes_encrypted = aes.encrypt(plaintext)
print(aes_encrypted)
aes_decrypted = aes.decrypt(plaintext)
print(aes_decrypted)
rsa = RSA(bits=2048)
rsa_encrypted = rsa.encrypt(plaintext)
print(rsa_encrypted)
rsa_decrypted = rsa.decrypt(rsa_encrypted)
print(rsa_decrypted)
