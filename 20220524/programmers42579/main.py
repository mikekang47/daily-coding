from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic = defaultdict(int)
    hap = defaultdict(list)
    for i in range(len(genres)):
        dic[genres[i]] += plays[i]
        hap[genres[i]].append([plays[i], i])

    for i in list(hap.keys()):
        hap[i].sort(key = lambda x: (-x[0], x[1]))

    keys = sorted(dic, key=lambda x: dic[x], reverse=True)
    print(keys)
    print(hap)
    print(dic)
    for i in keys:
        if len(hap[i]) == 1:
            answer.append(hap[i][0][1])
        else:
            for j in range(2):
                answer.append(hap[i][j][1])
    print(answer)
    return answer


genres = ["classic", "pop", "classic", "pop", "classic", "classic"]
plays = [400, 600, 150, 600, 500, 500]
solution(genres, plays)