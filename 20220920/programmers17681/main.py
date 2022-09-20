def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        s = str(bin(i|j)[2:])
        # s = s.rjust(n, '0')
        s = s.replace("1", "#")
        s = s.replace("0", ' ')
        answer.append(s)
        print(s)

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n, arr1, arr2)