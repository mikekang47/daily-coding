import unittest


# def solution(stones, k):
#     answer = 0
#     while 1:
#         for i in range(len(stones)):
#             if stones[i] != 0:
#                 stones[i] -= 1
#             else:
#                 cnt = 0
#                 for j in range(i + 1, i + k + 1):
#                     if j >= len(stones):
#                         break
#                     if stones[j] == 0:
#                         cnt += 1
#                     else:
#                         break
#
#                     if cnt == k - 1:
#                         return answer
#         answer += 1


def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left

class Test(unittest.TestCase):
    def test_solution(self):
        stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
        k = 3
        assert solution(stones, k) == 3
