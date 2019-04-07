class Test():

    def string_to_hex(string):
        return bytes_to_hex(string_to_bytes(string))


    def string_to_bytes(string):
        return string.encode('utf-8')


    def bytes_to_hex(data):
        return data.hex()


    def bytes_to_string(data):
        return data.decode('utf-8', errors='replace')


    def hex_to_string(hex):
        return bytes.fromhex(hex)


    def run(self, encrypt, decrypt):
        key = ('0'*24)
        data = '�T1N-x��Y2'.encode('utf-8')
        print('*** DATA')
        print(data)

        encrypted = encrypt(data=data)

        print('*** Encrypting')
        print(encrypted)
        print(encrypted.decode('utf-8', errors='replace'))

        decoded = decrypt(encrypted)
        print('*** Decrypting')
        print(decoded)
