from heapq import heappush, heappop
n = int(input())
negative = []
positive = []
result = 0
for i in range(n):
    temp = int(input())
    if temp <= 0:
        heappush(negative, temp)
    elif temp > 0:
        heappush(positive, -temp)

while len(negative) >= 2:
    a = heappop(negative)
    b = heappop(negative)
    result += a * b
    
if len(negative) != 0:
    result += heappop(negative)


while len(positive) >= 2:
    a = heappop(positive)
    b = heappop(positive)

    result += max(-(a+b), a * b)
    
if len(positive) != 0:
    result += -heappop(positive)

print(result)
    