def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]

    arr1_a, arr1_b, arr2_a, arr2_b = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])

    for i in range(0,arr1_a,1) :
        for j in range(0,arr2_a*arr2_b,1):
            answer[i][int(j/arr2_a)] += (arr1[i][int(j%arr2_a)] * arr2[int(j%arr2_a)][int(j/arr2_a)])

    return answer
