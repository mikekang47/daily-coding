n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

# 크레인이 옮길 수 있는 무게의 최댓값
max_weight = max(crain)

# 모든 박스를 옮길 수 없는 경우
if max(box) > max_weight:
    print(-1)
    exit()

