import sys
import statistics as st

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

print(round(st.mean(arr)))
print(st.median(arr))
a = st.multimode(arr)
a.sort()
m = a[1] if len(a) > 1 else a[0]
print(m)
print(max(arr) - min(arr))
