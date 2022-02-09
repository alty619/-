# 점과 사각형의 거리를 두 가지 경우를 모두 고려해주어 구했다.
## 사각형의 한 변이 점과 가장 가까울 경우
## 사각형의 꼭짓점이 점과 가장 가까울 경우

## 사각형의 한 변이 점과 가장 가까울 경우
### 사각형의 두 꼭짓점을 잇는 직선의 방정식을 구하고, 이 직선과 '주어진 한 점을 지나면서 법선인 직선'의 교점을 구한다.
### 교점이 두 꼭짓점 사이, 즉 변 위에 있으면 한 점에서부터 면이 가장 가깝게 된다.
### 반면, 변 위에 없다면 사각형까지의 거리가 아니므로 제외해준다.
### 구한 교점으로부터 주어진 점 사이의 거리중 가장 작은 값이 최종 사각형까지의 거리의 후보가 된다.

## 사각형의 꼭짓점이 점과 가장 가까울 경우
### 한 점과 사각형 꼭짓점과의 거리를 구한다.
### 구한 거리 중 가장 작은 값이 최종 사각형까지의 거리의 후보가 된다.

## 두가지 경우로 구한 결과값 중 더 작은 값이 사각형까지의 최소거리가 된다.

from itertools import combinations
from math import sqrt


# 두 점 사이의 거리를 구하는 함수
def distance(A, B):
    return sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)


# 점 A에서 사각형의 변을 연장한 직선에 내린 수선의 발을 찾는 함수
def find_h_point(C1, C2, A):
    x1 = C1[0]
    y1 = C1[1]
    x2 = C2[0]
    y2 = C2[1]
    x_a = A[0]
    y_a = A[1]

    # 직선의 기울기가 무한이 아닐때
    if x2 != x1: 
        tangent = (y2 - y1)/(x2 - x1)  # 직선의 기울기
        
        # 직선의 기울기가 0이 아닐때
        if tangent != 0: 
            b = y1 - tangent*x1  # 직선의 y절편
            c = y_a + x_a/tangent  # 주어진 점을 지나고, 법선인 직선의 y절편

            intersec_x = tangent*(c-b)/(tangent**2+1)  # 두 직선의 교점 x좌표
            intersec_y = (b-c)/(tangent**2+1) + c  # 두 직선의 교점 y 좌표
            return (intersec_x, intersec_y)

        # 기울기가 0일때의 교점
        else:
            return (x_a, y1)

    # 기울기가 무한일때의 교점
    else : 
        return (x1, y_a)


############
### main ###
############

# 점 A, 사각형 C의 x,y좌표를 입력받음
A = list(map(float, input().split()))

C = []
for i in range(4):
    C.append(list(map(float, input().split())))

# 사각형 4개 꼭짓점으로부터 만들 수 있는 선분의 조합
groups = list(combinations(C, 2))

# 함수 이용해서 수선의 발 찾기
intersect_points = []
for group in groups:
    h_point = find_h_point(group[0], group[1], A)  # 수선의 발

    # x값,y값 범위 지정하기 위해 각 말단 조정
    x_min = min(group[0][0], group[1][0]) 
    x_max = max(group[0][0], group[1][0])
    y_min = min(group[0][1], group[1][1]) 
    y_max = max(group[0][1], group[1][1])

    if x_min <= h_point[0] <= x_max:  #두 점 사이에 수선의 발이 위치해야 사각형까지의 거리라고 할 수 있다.
        if y_min <= h_point[1] <= y_max: 
            intersect_points.append(h_point)  # 사각형의 변 위에 있는 수선의 발만 추가해준다.

# 수선의 발과 사각형 밖에 주어진 한 점 사이의 거리
distance_list = []
for point in intersect_points:
    distance_list.append(distance(point, A))

# 사각형의 꼭짓점과 거리 비교
for point in C:
    distance_list.append(distance(point, A))

# 찾은 거리 중 가장 가까운 것이 결과이다.
result = min(distance_list)

# 결과 출력
print(f"{result:.3}")




