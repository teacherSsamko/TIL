scores = list(map(int, input().split()))
asc = None
start = scores.pop(0)
for score in scores:
    if start < score:
        if asc is None:
            asc = "ascending"
            start = score
        elif asc == "ascending":
            start = score
            continue
        else:
            asc = "mixed"
            break
    else:
        if asc is None:
            asc = "descending"
            start = score
        elif asc == "descending":
            start = score
            continue
        else:
            asc = "mixed"
            break

print(asc)
