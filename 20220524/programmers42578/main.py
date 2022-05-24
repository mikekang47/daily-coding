
def solution(clothes):
    answer = 1
    dic = {}
    for r, t in clothes:
        if t not in dic:
            dic[t] = 2
        else :
            dic[t] += 1
    for i in list(dic.keys()):
        answer *= dic[i]

    return answer -1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
