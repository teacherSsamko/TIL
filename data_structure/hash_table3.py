# Linear Probing
hash_table = [0 for i in range(8)]


def get_key(data):
    return hash(data)


def hash_func(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for idx in range(hash_address, len(hash_table)):
            if hash_table[idx] == 0:
                hash_table[idx] = [index_key, value]
                return
            elif hash_table[idx][0] == index_key:
                hash_table[1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0:
        for idx in range(hash_address, len(hash_table)):
            if hash_table[idx] == 0:  # Key Point!!!
                return None
            elif hash_table[idx][0] == index_key:
                return hash_table[idx][1]

    else:
        return None


save_data('Dave', '010123123')
save_data('Andy', '01033334444')
print(hash_table)
print(read_data('Dave'))
