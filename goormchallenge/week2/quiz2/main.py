import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
start = s[0]
wordSet = []
cnt = 1
for i in range(1, len(s)):
    if s[i] == start:
        cnt += 1
    else:
        wordSet.append(start * cnt)
        cnt = 1
        start = s[i]

wordSet.append(start*cnt)

print(len(wordSet))
