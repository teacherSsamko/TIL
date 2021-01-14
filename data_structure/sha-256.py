import hashlib

data = 'test'.encode()  # encode() => string to byte
hash_object = hashlib.sha256()
hash_object.update(data)
hash_object.update(b'test')  # same with above
hex_dig = hash_object.hexdigest()
print(hex_dig)
