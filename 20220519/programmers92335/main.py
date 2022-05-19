import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def jinbup(n, k):
    if k == 10:
        return str(n)
    li = []
    while n != 0:
        li.append(n % k)
        n = int(n / k)
    li.reverse()
    li = list(map(str, li))
    return ''.join(li)

def solution(n, k):
    answer = 0
    s = jinbup(n,k)
    sosu = s.split('0')
    for i in sosu:
        if i.isdigit():
            if isPrime(int(i)) and int(i) != 1:

                answer += 1
    return answer

n = 437674
k = 3

solution(n, k)