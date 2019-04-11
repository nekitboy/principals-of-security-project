import time
import copy
from memory_profiler import LineProfiler, choose_backend, profile



def profile1(func):
    def wrapper(*args, **kwargs):
        mem_usage = 0
        prof = LineProfiler(backend=choose_backend('psutil'))
        val = prof(func)(*args, **kwargs)

        for (filename, lines) in prof.code_map.items():

            for (lineno, mem) in lines:
                inc = 0
                if mem:
                    mem_usage += mem[0]
                #print('Memory: ', mem)

        #show_results(prof, stream=stream, precision=precision)
        return val, mem_usage

    return wrapper

@profile1
def empty():
    return None

temp, null_memory = empty()

class TestSecurity():

    def __init__(self, algo, data):
        self.time = -1
        self.algo = algo
        self.temp_time = 0
        self.data = data
        self.null_memory = null_memory


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


    @profile1
    def encrypt(self, encryptor, data):
        a = copy.deepcopy(encryptor)
        d = copy.deepcopy(data)
        return a(data=d)

    @profile1
    def decrypt(self, decryptor, data):
        a = copy.deepcopy(decryptor)
        d = copy.deepcopy(data)
        return a(data=d)


    def run(self, encryptor, decryptor):

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

            encrypted, memory = self.encrypt(encryptor=encryptor, data=data)

            test['time_to_encrypt'] = self.stop_timer()
            test['memory_to_encrypt'] = (memory - self.null_memory) * 1024
            test['encrypted'] = encrypted

            self.start_timer()
            decrypted, memory = self.decrypt(decryptor=decryptor, data=encrypted)
            test['time_to_decrypt'] = self.stop_timer()
            test['time'] = test['time_to_encrypt'] + test['time_to_decrypt']
            test['memory_to_decrypt'] = (memory - self.null_memory) * 1024

            test['decrypted'] = decrypted
            test['decrypted_str'] = self.bytes_to_string(self, decrypted)

            results.append(test)
        return results


def serialize(data):
    if isinstance(data, bytes):
        return str(data)

    return data


def calc_avalanche(bytes1, bytes2):
    """
    Calculate avalanche effect
    :param bytes1: bytes object
    :param bytes2: bytes object
    :return: (avalanche_diff, avalanche_percent)
    """
    if len(bytes1) != len(bytes2):
        raise Exception("Couldn't calculate avalanche effect of bytes with different lengths")

    diff = 0
    for byte1, byte2 in zip(bytes1, bytes2):
        diff += bin(byte1 ^ byte2).count('1')

    return diff, diff/len(bytes1*8)
