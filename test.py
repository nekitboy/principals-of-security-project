from des import triple_des
from aes import AESModeOfOperationECB
from rsa import RSA
from blowfish import Blowfish
from ranker import Ranker
import os
import json
from environment import TestSecurity, serialize

key_3des_24 = '0' * 24
key_3des_16 = '0' * 16
triple_des_m_24 = triple_des(key=key_3des_24, padmode=2)
triple_des_m_16 = triple_des(key=key_3des_16, padmode=2)
key_aes_128 = os.urandom(16)
key_aes_256 = os.urandom(32)
aes_128 = AESModeOfOperationECB(key_aes_128)
aes_256 = AESModeOfOperationECB(key_aes_256)
rsa_2048 = RSA(bits=2048)
rsa_1024 = RSA(bits=1024)
blowfish_128 = Blowfish(bytes(key_3des_16, 'utf-8'))
blowfish_192 = Blowfish(bytes(key_3des_24, 'utf-8'))
plaintexts = ['Hello World', 'ASDKMASKFMASKLDMASDMKAS'*100, '.;.ng[h;']
s_des_128 = TestSecurity('3-DES-128', plaintexts)
s_des_192 = TestSecurity('3-DES-192', plaintexts)
s_aes_128 = TestSecurity('AES-128', plaintexts)
s_aes_256 = TestSecurity('AES-256', plaintexts)
s_rsa_1024 = TestSecurity('RSA-1024', plaintexts)
s_rsa_2048 = TestSecurity('RSA-1024', plaintexts)
s_blowfish_128 = TestSecurity('Blowfish-128', plaintexts)
s_blowfish_192 = TestSecurity('Blowfish-128', plaintexts)

results_des_128 = s_des_128.run(triple_des_m_16.encrypt, triple_des_m_16.decrypt)
results_des_192 = s_des_192.run(triple_des_m_24.encrypt, triple_des_m_24.decrypt)
results_aes_128 = s_aes_128.run(aes_128.encrypt, aes_128.decrypt)
results_aes_256 = s_aes_256.run(aes_256.encrypt, aes_256.decrypt)
results_rsa_1024 = s_rsa_1024.run(rsa_1024.encrypt_data, rsa_1024.decrypt_data)
results_rsa_2048 = s_rsa_2048.run(rsa_2048.encrypt_data, rsa_2048.decrypt_data)
results_blowfish_128 = s_blowfish_128.run(blowfish_128.encrypt, blowfish_128.decrypt)
results_blowfish_192 = s_blowfish_128.run(blowfish_192.encrypt, blowfish_192.decrypt)
results = []
results.extend(results_des_128)
results.extend(results_des_192)
results.extend(results_aes_128)
results.extend(results_aes_256)
results.extend(results_rsa_1024)
results.extend(results_rsa_2048)
results.extend(results_blowfish_128)
results.extend(results_blowfish_192)
ranker = Ranker(results)
ranker.run_all()

def encrypt(data):
    return encrypt(data=data)
