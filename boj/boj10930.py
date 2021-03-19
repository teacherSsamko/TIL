from hashlib import sha256
S = input()
print(sha256(S.encode()).hexdigest())
