# 1.

# 두 값 N과 X를 정수형태로 받기
N = int(input())
X = int(input())

# 수열 A의 정수들을 띄어쓰기로 구별해서 리스트에 받기
A = list(map(int, input().split()))

# 수열 안의 수가 X 이하인 조건문 생성
A_output = []  # 결과값을 받을 리스트 생성
for i in A:
    if i <= X:
        A_output.append(i)  # 수열 A의 수가 X이하이면 결과값 리스트에 넣기

# 리스트 형태로 표현되는 결과값을 출력 예시와 같도록 변환
for i in A_output:
    print(i, end=" ")