# 5.
N,X = map(int, input().split())
A = []
A = list(map(int, input().split()))

if X == 1:
    A.sort()
    for i in A:
        print(i, end=" ")
elif X==0:
    A.sort(reverse = True)
    for i in A:
        print(i, end=" ")