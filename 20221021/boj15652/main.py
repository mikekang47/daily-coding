N,M = map(int, input().split())
li = []

def dfs(n):
    if len(li) == M:
        print(*li)
        return
    for i in range(n,N+1):
        li.append(i)
        dfs(i)
        li.pop()
dfs(1)


