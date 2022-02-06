#3.
# A,B,C 값을 받기
A = int(input())
B = int(input())
C = int(input())

# 가장 긴 변을 찾기위해 리스트에 넣어서 정렬
edges = [A, B, C]
edges.sort() # 오름차순 정렬

# 정렬된 리스트에서 작은것부터 A,B,C라고 재정의해주기
A = edges[0]
B = edges[1]
C = edges[2] # 가장 긴 변

# 함수 Pythagrean() 생성
def Pythagorean():
    if C < (A + B) : # 삼각형의 생성조건_ 가장 긴 변이 나머지 두 변의 합보다 작아야 삼각형 생성됨.
        if (C**2) == (A**2)+(B**2) : # 직각삼각형의 조건
            print("직각삼각형")
        elif (C**2) >= (A**2)+(B**2) : # 둔각삼각형의 조건
            print("둔각삼각형")
        else :
            print("예각삼각형") # 위의 두 경우가 아니면 예각삼각형
    else :
        print("NO") # 삼각형 생성조건 충족 못할시 NO 반환

# 함수 출력
Pythagorean()