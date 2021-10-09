from datetime import datetime, timedelta


def solution(purchase):
    result = [0, 0, 0, 0, 0]
    recent_purchase = []
    pur_dict = dict()

    # list 를 dictonary로
    for item in purchase:
        pur_dict.update({date_to_days(item): str_pay(item)})

    d = 1
    class_now = 0
    points = 0
    while d < 366:
        if d in pur_dict:
            recent_purchase.append([d, pur_dict[d]])
            points += recent_purchase[-1][1]

        if recent_purchase:
            if d - recent_purchase[0][0] > 29:
                points -= recent_purchase.pop(0)[1]

        class_now = classfy(points)
        result[class_now] += 1
        d += 1

    return result


# date를 몇일째인지로


def date_to_days(item):
    std = datetime(2019, 1, 1)
    temp = datetime.strptime(item.split(' ')[0], "%Y/%m/%d")
    days = temp - std
    return days.days + 1


def str_pay(paystr):
    temp = paystr.split(' ')[1]
    return int(temp)


def classfy(points):

    if points < 10000:
        return 0
    elif points < 20000:
        return 1
    elif points < 50000:
        return 2
    elif points < 100000:
        return 3
    else:
        return 4


purchase = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
print(solution(purchase))
