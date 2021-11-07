n = int(input())
arr = []
for i in range(n):
    arr.append(input())
sentence = list(arr[0])
for i in range(n):
    for a in range(len(sentence)):
        if sentence[a] == arr[i][a]:
            continue
        else:
            sentence[a] = '?'

print(''.join(sentence))