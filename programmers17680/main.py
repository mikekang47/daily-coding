import unittest

def solution(cacheSize, cities):
    answer = 0
    li = []
    for i in cities:
        city = i.lower()
        if city in li:
            answer += 1
            li.remove(city)
            li.append(city)
        else:
            if len(li) < cacheSize:
                li.append(city)
                answer += 5
            else:
                if len(li) != 0:
                    li.pop(0)
                if len(li) < cacheSize:
                    li.append(city)
                answer += 5
    return answer


class Test(unittest.TestCase):
    def test_solution(self):
        cacheSize = 3
        cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
        assert(solution(cacheSize,cities)) == 50

    def test_solution2(self):
        cacheSize = 3
        cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
        assert (solution(cacheSize, cities)) == 21