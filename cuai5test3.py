# 3.
from math import sqrt

# 함수 Pythagrean()
def Pythagorean(A, B, C):
    if C < (A + B) :  # 삼각형의 생성조건
        if C == sqrt((A**2)+(B**2)) :  # 직각삼각형의 조건
            print("직각삼각형")
        elif C >= sqrt((A**2) + (B**2)) :  # 둔각삼각형의 조건
            print("둔각삼각형")
        else :
            print("예각삼각형")  # 위의 두 경우가 아니면 예각삼각형
    else :
        print("NO")  # 삼각형 생성조건 충족 못할시 NO 반환


# A,B,C 값을 받아 edges 리스트에 넣기
edges =[]
for i in range(3):
    edges.append(int(input()))
edges.sort()  # 오름차순 정렬

# 정렬된 리스트에서 작은것부터 A,B,C라고 재정의해주기
A = edges[0]
B = edges[1]
C = edges[2]  # 가장 긴 변

# 함수 출력
Pythagorean(A,B,C)