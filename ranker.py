import numpy as np

class Ranker:
    def __init__(self, results):
        self.results = results
        self.encrypt_time_score = {}
        self.memory_encrypt_score = {}
        self.decrypt_time_score = {}
        self.memory_decrypt_score = {}
        self.average_encrypt_time = {}
        self.average_decrypt_time = {}
        self.average_memory_encrypt = {}
        self.average_memory_decrypt = {}
        self.plaintexts_encrypt_time_score = {}
        self.plaintexts_decrypt_time_score = {}
        self.plaintexts_encrypt_memory_score = {}
        self.plaintexts_decrypt_memory_score = {}
        self.plaintexts = []

    def avg_time_to_encrypt(self):
        indexed = {}
        for result in self.results:
            if result['algorithm'] in indexed:
                indexed[result['algorithm']].append(result['time_to_encrypt'])
            else:
                indexed[result['algorithm']] = [result['time_to_encrypt']]
        indexed_avg = {}
        for k, v in indexed.items():
            indexed_avg[k] = np.average(v)
        self.average_encrypt_time = indexed_avg
        sort = sorted(indexed_avg.items(), key=lambda x: x[1])
        best_value = sort[0][1]
        for rez in sort:
            self.encrypt_time_score[rez[0]] = best_value / rez[1]

    def avg_memory_to_encrypt(self):
        indexed = {}
        for result in self.results:
            if result['algorithm'] in indexed:
                indexed[result['algorithm']].append(result['memory_to_encrypt'])
            else:
                indexed[result['algorithm']] = [result['memory_to_encrypt']]
        indexed_avg = {}
        for k, v in indexed.items():
            indexed_avg[k] = np.average(v)
        self.average_memory_encrypt = indexed_avg
        sort = sorted(indexed_avg.items(), key=lambda x: x[1])
        best_value = sort[0][1]
        for rez in sort:
            self.memory_encrypt_score[rez[0]] = best_value / rez[1]

    def avg_time_to_decrypt(self):
        indexed = {}
        for result in self.results:
            if result['algorithm'] in indexed:
                indexed[result['algorithm']].append(result['time_to_decrypt'])
            else:
                indexed[result['algorithm']] = [result['time_to_decrypt']]
        indexed_avg = {}
        for k, v in indexed.items():
            indexed_avg[k] = np.average(v)
        self.average_decrypt_time = indexed_avg
        sort = sorted(indexed_avg.items(), key=lambda x: x[1])
        best_value = sort[0][1]
        for rez in sort:
            self.decrypt_time_score[rez[0]] = best_value / rez[1]

    def avg_memory_to_decrypt(self):
        indexed = {}
        for result in self.results:
            if result['algorithm'] in indexed:
                indexed[result['algorithm']].append(result['memory_to_decrypt'])
            else:
                indexed[result['algorithm']] = [result['memory_to_decrypt']]
        indexed_avg = {}
        for k, v in indexed.items():
            indexed_avg[k] = np.average(v)
        self.average_memory_decrypt = indexed_avg
        sort = sorted(indexed_avg.items(), key=lambda x: x[1])
        best_value = sort[0][1]
        for rez in sort:
            self.memory_decrypt_score[rez[0]] = best_value / rez[1]

    def plaintext_parse(self):
        for result in self.results:
            if result['data_str'] not in self.plaintexts:
                self.plaintexts.append(result['data_str'])

    def plaintexts_encrypt_time(self):
        if not self.plaintexts:
            self.plaintext_parse()
        for plaintext in self.plaintexts:
            temp = []
            for result in self.results:
                if result['data_str'] == plaintext:
                    temp.append((result['algorithm'], result['time_to_encrypt']))
            temp = sorted(temp, key=lambda x: x[1])
            best_value = temp[0][1]
            temp_scored = []
            for rez in temp:
                temp_scored.append((rez[0], best_value / rez[1]))
            self.plaintexts_encrypt_time_score[plaintext] = temp_scored

    def plaintexts_decrypt_time(self):
        if not self.plaintexts:
            self.plaintext_parse()
        for plaintext in self.plaintexts:
            temp = []
            for result in self.results:
                if result['data_str'] == plaintext:
                    temp.append((result['algorithm'], result['time_to_decrypt']))
            temp = sorted(temp, key=lambda x: x[1])
            best_value = temp[0][1]
            temp_scored = []
            for rez in temp:
                temp_scored.append((rez[0], best_value / rez[1]))
            self.plaintexts_decrypt_time_score[plaintext] = temp_scored

    def plaintexts_encrypt_memory(self):
        if not self.plaintexts:
            self.plaintext_parse()
        for plaintext in self.plaintexts:
            temp = []
            for result in self.results:
                if result['data_str'] == plaintext:
                    temp.append((result['algorithm'], result['memory_to_encrypt'] + 0.1))
            temp = sorted(temp, key=lambda x: x[1])
            best_value = temp[0][1]
            temp_scored = []
            for rez in temp:
                temp_scored.append((rez[0], best_value / rez[1]))
            self.plaintexts_encrypt_memory_score[plaintext] = temp_scored

    def plaintexts_decrypt_memory(self):
        if not self.plaintexts:
            self.plaintext_parse()
        for plaintext in self.plaintexts:
            temp = []
            for result in self.results:
                if result['data_str'] == plaintext:
                    temp.append((result['algorithm'], result['memory_to_decrypt'] + 0.1))
            temp = sorted(temp, key=lambda x: x[1])
            best_value = temp[0][1]
            temp_scored = []
            for rez in temp:
                temp_scored.append((rez[0], best_value / rez[1]))
            self.plaintexts_decrypt_memory_score[plaintext] = temp_scored

    def run_all(self):
        self.avg_time_to_encrypt()
        self.avg_memory_to_decrypt()
        self.avg_memory_to_encrypt()
        self.avg_time_to_decrypt()
        self.plaintexts_encrypt_time()
        self.plaintexts_decrypt_time()
        self.plaintexts_encrypt_memory()
        self.plaintexts_decrypt_memory()
        pass
