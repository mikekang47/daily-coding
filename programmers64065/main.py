
def solution(s: str) :
    answer = []
    li = s.split(",{")
    for i in li:
        i = i.replace("{", "")
        i = i.replace("}", "")
        p = i.split(",")
        answer.append(p)
    answer.sort(key=len)
    real = []
    for i in answer:
        for j in i:
            if len(real) == 0:
                real.append(j)
            if j not in real:
                real.append(j)
    real = list(map(int, real))
    print(real)
    return real


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)