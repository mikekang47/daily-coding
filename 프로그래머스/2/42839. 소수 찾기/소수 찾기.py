import itertools
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    res = []
    for i in range(1, len(numbers) + 1):
        res += list(itertools.permutations(list(numbers), i))
    r = list(map(lambda x: int(''.join(x)), res))
    count = 0
    r = list(set(r))
    print(r)
    for i in r:
        if is_prime(i):
            count += 1

    return count


print(solution("17"))
print(solution("011"))
