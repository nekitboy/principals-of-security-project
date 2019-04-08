from des import triple_des
import json
from environment import TestSecurity, serialize

key = '0' * 24
triple_des_m = triple_des(key=key, padmode=2)
t = TestSecurity('3-DES', ['123', 'Hello World', 'ASDKMASKFMASKLDMASDMKAS'])
print(json.dumps(t.run(triple_des_m.encrypt, triple_des_m.decrypt), default=serialize, indent=True))
