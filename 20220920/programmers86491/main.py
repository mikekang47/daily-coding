def solution(sizes: list):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


