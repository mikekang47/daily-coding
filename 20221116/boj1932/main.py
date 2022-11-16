import sys
from functools import cache

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

triangle = []


def main():
    global triangle
    n = int(input())
    triangle = [None]
    for _ in range(n):
        triangle.append(list(map(int, input().split())))

    height = n
    result = []
    for i in range(height):
        result.append(get_max_sum(height, i))
    print(max(result))


@cache
def get_max_sum(height, i):
    global triangle
    if not (0 <= i < len(triangle[height])):
        return -sys.maxsize-1
    if height == 1:
        return triangle[1][0]
    return triangle[height][i] + max(get_max_sum(height-1, i), get_max_sum(height-1, i-1))


if __name__ == "__main__":
    main()