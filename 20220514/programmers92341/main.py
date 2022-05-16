from collections import defaultdict
import math

def solution(fees, records):

    def get_minute(time):
        h, m = time.split(":")
        return int(h) * 60 + int(m)

    answer = list()
    parking = dict()
    total = defaultdict(int)

    for r in records:
        t, n, f = r.split()
        minute = get_minute(t)
        if n in parking:
            total[n] += minute - parking[n]
            del parking[n]
        else:
            parking[n] = minute


    end_minute = get_minute('23:59')
    for k, v in parking.items():
        total[k] += (end_minute - v)


    s1, m1, s2, m2 = fees
    for k, v in total.items():
        all = m1
        if v > s1:
            all += math.ceil((v - s1) / s2) * m2
        answer.append((k, all))

    answer.sort()
    return [a[1] for a in answer]