def solution(table, languages, preference):
    answer = ''
    jobs = {}
    # score = {k: 0 for k in languages}
    # print(score)
    for row in table:
        r = row.split(" ")
        jobs[r[0]] = r[:0:-1]
    print(jobs)
    score = {}
    for job in jobs.keys():
        score[job] = 0
        for i, lang in enumerate(languages):
            for j, lang_s in enumerate(jobs[job]):
                if lang == lang_s:
                    score[job] += preference[i] * (j + 1)

    print(score)
    score = [(s, t) for t, s in score.items()]
    print(score)
    score = sorted(score, key=lambda x: x[1])
    print(score)
    top = max(score)[0]
    for s in score:
        if s[0] == top:
            answer = s[1]
            break
    # answer = max(score)[1]

    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
# languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5]
# preference = [7, 5, 5]
print(solution(table, languages, preference))
