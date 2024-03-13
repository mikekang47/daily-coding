from collections import defaultdict


def solution(participant, completion):
    answer = ''
    dic = defaultdict(int)
    res = defaultdict(int)
    for i in completion:
        dic[i] = dic[i] + 1

    for i in participant:
        res[i] = res[i] + 1

    for i in res.keys():
        if dic[i] == 0 or res[i] != dic[i]:
            print(i)
            return i