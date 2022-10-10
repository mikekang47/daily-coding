from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    dic[int(input())] += 1
if dic[0] > dic[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")