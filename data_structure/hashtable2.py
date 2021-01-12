# Chaining
hash_table = [0 for i in range(8)]


def get_key(data):
    return hash(data)


def hash_func(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for idx in range(len(hash_table[hash_address])):
            if hash_table[hash_address][idx][0] == index_key:
                hash_table[hash_address][idx][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for idx in range(len(hash_table[hash_address])):
            if hash_table[hash_address][idx][0] == index_key:
                return hash_table[hash_address][idx][1]
        return None
    else:
        return None
    return hash_table[hash_address]


save_data('Dave', '010123123')
save_data('Andy', '01033334444')
print(hash_table)
print(read_data('Dave'))
