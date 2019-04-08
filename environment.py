import time

class TestSecurity():

    def __init__(self, algo, data):
        self.time = -1
        self.algo = algo
        self.temp_time = 0
        self.data = data

    @staticmethod
    def string_to_bytes(self, string):
        return string.encode('utf-8')

    @staticmethod
    def bytes_to_hex(self, data):
        return data.hex()

    @staticmethod
    def string_to_hex(self, string):
        return self.bytes_to_hex(self.string_to_bytes(string))

    @staticmethod
    def bytes_to_string(self, data):
        return data.decode('utf-8', errors='replace')

    @staticmethod
    def hex_to_string(self, hex):
        return bytes.fromhex(hex)

    def start_timer(self):
        self.temp_time = time.time()

    def stop_timer(self):
        return time.time() - self.temp_time

    def run(self, encrypt, decrypt):

        results = []
        for i, cur_data in enumerate(self.data):

            test = dict()
            test['id'] = i
            test['algorithm'] = self.algo

            data = cur_data
            if isinstance(cur_data, bytes):
                test['data_str'] = self.bytes_to_string(self, cur_data)
            if isinstance(cur_data, str):
                test['data_str'] = cur_data
                data = cur_data.encode('utf-8')
            test['data'] = data

            self.start_timer()

            encrypted = encrypt(data=data)
            test['time_to_encrypt'] = self.stop_timer()
            test['encrypted'] = encrypted

            self.start_timer()
            decrypted = decrypt(encrypted)
            test['time_to_decrypr'] = self.stop_timer()

            test['decrypted'] = decrypted
            test['decrypted_str'] = self.bytes_to_string(self, decrypted)

            results.append(test)
        return results


def serialize(data):
    if isinstance(data, bytes):
        return str(data)

    return data