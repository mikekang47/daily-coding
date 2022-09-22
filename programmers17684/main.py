import unittest


def solution(msg):
    answer = []
    dic = {}
    num = 65
    for i in range(1, 27):
        dic[chr(num)] = i
        num += 1
    i, last = 0, 27
    while msg:
        j = 1
        while msg[:j] in dic.keys() and j <= len(msg):
            j += 1
        j -= 1

        answer.append(dic[msg[:j]])
        dic[msg[:j + 1]] = last
        last += 1
        msg = msg[j:]
    return answer


class Test(unittest.TestCase):

    def test_solution(self):
        msg = "KAKAO"
        assert solution(msg) == [11, 1, 27, 15]
