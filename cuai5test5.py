# 5.
# N, X를 입력받기
N,X = map(int, input().split())

# 수열 A 입력받기
A = list(map(int, input().split()))

# X에 따라 수열 정렬
if X == 1:
    A.sort()  # 오름차순
    for i in A:
        print(i, end=" ")  # 정렬된 수열 출력
elif X==0:
    A.sort(reverse = True) # 내림차순
    for i in A:
        print(i, end=" ")  # 정렬된 수열 출력
else :
    print("X에 1 또는 0을 입력하세요")  # X에 0,1이 아닌 다른 수가 입력될 경
