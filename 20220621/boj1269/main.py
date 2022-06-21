n, m = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

chaA = set(A).difference(B)
chaB = set(B).difference(A)
print(len(chaA)+len(chaB))
