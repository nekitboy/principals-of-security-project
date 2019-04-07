from des import triple_des
from environment import Test

key = '0' * 24
triple_des_m = triple_des(key=key, padmode=2)
t = Test()
t.run(triple_des_m.encrypt, triple_des_m.decrypt)