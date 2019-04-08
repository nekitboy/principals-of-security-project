from aes import AESModeOfOperationECB
from rsa import RSA
import os

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