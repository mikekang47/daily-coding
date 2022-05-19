answer = 0

def dfs(numbers, target, sum, idx):
    global answer
    if idx == len(numbers):
        if sum == target:
            answer += 1
        return
    dfs(numbers, target, sum+numbers[idx], idx+1)
    dfs(numbers, target, sum-numbers[idx], idx+1)


def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer

numbers = [1, 1, 1, 1]
target = 3

print(solution(numbers, target))