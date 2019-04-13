from des import triple_des
from aes import AESModeOfOperationECB
from rsa import RSA
from blowfish import Blowfish
from ranker import Ranker
import os
import json
from environment import TestSecurity, serialize

key = '0' * 24
triple_des_m = triple_des(key=key, padmode=2)
key_aes = os.urandom(16)
aes = AESModeOfOperationECB(key_aes)
rsa = RSA(bits=2048)
blowfish = Blowfish(bytes(key, 'utf-8'))
s_des = TestSecurity('3-DES', ['123', 'Hello World', 'ASDKMASKFMASKLDMASDMKAS'*100, '123'])
s_aes = TestSecurity('AES', ['123', 'Hello World', 'ASDKMASKFMASKLDMASDMKAS'*100, '123'])
s_rsa = TestSecurity('RSA', ['123', 'Hello World', 'ASDKMASKFMASKLDMASDMKAS'*100, '123'])
s_blowfish = TestSecurity('Blowfish', ['123', 'Hello World', 'ASDKMASKFMASKLDMASDMKAS'*100, '123'])

results_des = s_des.run(triple_des_m.encrypt, triple_des_m.decrypt)
results_aes = s_aes.run(aes.encrypt, aes.decrypt)
results_rsa = s_rsa.run(rsa.encrypt_data, rsa.decrypt_data)
#results_blowfish = s_blowfish.run(blowfish.encrypt, blowfish.decrypt)
results = []
results.extend(results_des)
results.extend(results_aes)
results.extend(results_rsa)
ranker = Ranker(results)
ranker.run_all()
print(json.dumps(results_des, default=serialize, indent=True))

def encrypt(data):
    return encrypt(data=data)
