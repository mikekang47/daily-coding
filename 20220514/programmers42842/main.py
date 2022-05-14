def solution(brown, yellow):
    size = brown + yellow
    height = 2
    while height * 2 + (size / height) * 2 - 4 != brown:
        height += 1

    return [size / height, height]