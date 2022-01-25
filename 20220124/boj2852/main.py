n = int(input())
one_point = 0
two_point = 0
one_time = 0
two_time = 0
prev = 0
for i in range(n):
    a, b = input().split()
    time = int(b[:2])*60 + int(b[3:])
    if one_point == two_point:
        prev = time
    elif one_point > two_point:
        one_time += time - prev
        prev = time
    else:
        two_time += time - prev
        prev = time

    if a == '1':
        one_point += 1
    else:
        two_point += 1

if one_point > two_point:
    one_time += 48 * 60 - prev
elif one_point < two_point:
    two_time += 48 * 60 - prev

print(str(one_time//60).zfill(2) + ':'+str(one_time % 60).zfill(2))
print(str(two_time//60).zfill(2) + ':'+str(two_time % 60).zfill(2))








