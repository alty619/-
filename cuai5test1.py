#Q1

# 첫째 줄에 N과 X를 받음
# 띄어쓰기로 두 값을 input받는데,
# input값은 str형태이므로 int로 변환해서 받기
N = int(input())
X = int(input())

A_input = [] # input값들을 받을 리스트 생성
A_output = [] # 결과값을 받을 리스트 생성

#수열 A의 정수들을 띄어쓰기로 구별해서 받기
A_input = list(map(int, input().split()))

# 수열 안의 수가 X 이하인 조건문 생성
for i in A_input :
    if i <= X :
        A_output.append(i) # 수열 A의 수가 X이하이면 결과값 리스트에 넣기

# 리스트 형태로 표현되는 결과값을 출력 예시와 같이 수 나열로 변환해주기
for i in A_output:
    print(i, end=" ")