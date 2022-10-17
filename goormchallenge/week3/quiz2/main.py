from collections import defaultdict

dic = {1: [1, '.', ',', '?', '!'], 2: [2, 'A', 'B', 'C'], 3: [3, 'D', 'E', 'F'],
       4: [4, 'G', 'H', 'I'], 5: [5, 'J', 'K', 'L'], 6: [6, 'M', 'N', 'O'],
       7: ['P', 'Q', 'R', 'S'], 8: [8, 'T', 'U', 'V'], 9: [9, 'W', 'X', 'Y', 'Z']
       }
n = int(input())
s = list(input())
cnt = 1
start = s[0]
result = ""
for i in range(1, len(s)):
    if start == s[i]:
        cnt += 1
    else:
        result += str(dic[int(start)][cnt % len(dic[int(start)])-1]) if cnt % len(dic[int(start)]) != 0 else dic[int(start)][-1]
        cnt = 1
        start = s[i]

result += str(dic[int(start)][cnt % len(dic[int(start)])-1]) if cnt % len(dic[int(start)]) != 0 else dic[int(start)][-1]
print(result)
