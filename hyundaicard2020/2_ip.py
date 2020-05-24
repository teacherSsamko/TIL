def solution(ip_addrs, langs, scores):
    answer = 0
    unique_ip = set(ip_addrs)
    ip_index = {}
    print(unique_ip)

    for ip in unique_ip:
        indexs = [i for i, x in enumerate(ip_addrs) if x == ip]
        ip_index.update({ip: indexs})

    for ip, indexs in ip_index.items():
        same_ip = len(indexs)
        if same_ip >= 4:
            answer += same_ip
        elif same_ip == 3 and valid_group(indexs, langs):
            answer += same_ip
            print(ip)
        elif same_ip == 2 and valid_group(indexs, langs) and scores[indexs[0]] == scores[indexs[1]]:
            answer += 2
            print(indexs)
            print(ip)

    return len(ip_addrs) - answer


def valid_group(indexs, langs):
    lang_grp = ["C++", "C", "C#"]
    temp = []
    for i in indexs:
        if langs[i] in lang_grp:
            langs[i] = "C"
        temp.append(langs[i])
    temp = set(temp)
    if len(temp) == 1:
        return True

    return False


# ip_addrs = ["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111",
#             "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"]
# langs = ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"]
# scores = [294, 197, 373, 45, 294, 62, 373, 373]
# print(solution(ip_addrs, langs, scores))

ip_addrs = ["7.124.10.0", "7.124.10.0", "0.0.0.0",
            "7.124.10.0", "0.0.0.0", "7.124.10.0"]
langs = ["C++", "Java", "C#", "C#", "C", "Python3"]
scores = [314, 225, 45, 0, 155, 400]
print(solution(ip_addrs, langs, scores))
