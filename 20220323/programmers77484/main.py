def solution(lottos, win_nums):
    result = [6, 6, 5, 4, 3, 2, 1]

    zero = lottos.count(0)
    cnt = 0
    answer = []

    for num in lottos:
        if num in win_nums:
            win_nums.remove(num)
            cnt += 1

    print(win_nums)
    print(lottos)
    print(cnt)

    answer.append(result[zero + cnt])
    answer.append(result[cnt])

    return answer