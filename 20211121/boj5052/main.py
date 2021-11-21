import sys

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][0:len(phone_book[i])]:
            return False

    return True

t = int(input())
answer = []
digit = []
for _ in range(t):
    n = int(input())
    for _ in range(n):
        digit.append(str(sys.stdin.readline().strip()))
    answer.append(solution(digit))
    digit.clear()

for i in answer:
    if i == True:
        print("YES")
    else:
        print("NO")
