
def calculate(x, y, op):
    return eval(x+op+y)


def dfs(index, val):
    global res
    if index >= N:
        res = max(res, val)
        return

    op = '+' if index == 0 else exp[index-1]
    if index + 2 < N:
        tmp = calculate(exp[index], exp[index+2], exp[index+1])
        dfs(index + 4, calculate(str(val), str(tmp), op))
    dfs(index + 2, calculate(str(val), str(exp[index]), op))


N = int(input())
exp = list(input())
res = -1e9
dfs(0, 0)
print(res)