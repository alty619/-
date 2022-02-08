# 점 A, C1, C2, C3, C4의 x,y좌표를 리스트로 input받는다.
A = list(map(float, input().split()))
C1 = list(map(float, input().split()))
C2 = list(map(float, input().split()))
C3 = list(map(float, input().split()))
C4 = list(map(float, input().split()))

# 변환이 용이하게 numpy로 바꾼다.
import numpy as np
A = np.array(A)
C1 = np.array(C1)
C2 = np.array(C2)
C3 = np.array(C3)
C4 = np.array(C4)

# points라는 array에 사각형 꼭짓점 좌표를 넣어준다.
points = np.vstack((C1,C2,C3,C4)) # 4*2 array
#print(points)

# 점과 사각형의 거리를 두 가지 경우로 나누어 구했다.
## 사각형의 한 변이 점과 가장 가까울 경우
## 사각형의 꼭짓점이 점과 가장 가까울 경우

## 사각형의 한 변이 점과 가장 가까울 경우
### 사각형의 두 꼭짓점을 잇는 직선의 방정식을 구하고, 이 직선과 '주어진 한 점을 지나면서 법선인 직선'의 교점을 구한다.
### 교점이 두 꼭짓점 사이, 즉 변 위에 있으면 한 점에서부터 면이 가장 가깝게 된다.
### 반면, 변 위에 없다면 꼭짓점이 가장 가까운 경우이므로 이 경우는 제외해준다.
### 구한 교점으로부터 주어진 점 사이의 거리중 가장 작은 값이 사각형까지의 거리가 된다.

# 직선을 만들기 위해 꼭짓점을 선택할때, 꼭짓점 2개를 선택 가능한 모든 조합 찾기
from itertools import combinations
groups = list(combinations(points,2))
#print(groups)

# 두 직선의 교점 구하는 함수 제작
def ip(x1,y1,x2,y2,x3,y3):
    # 선택한 두 꼭짓점을 이은 직선의 기울기를 기준으로 분류한다.
    if x2!=x1: # 직선의 기울기가 무한이 아닐때
        a = (y2-y1)/(x2-x1) # 직선의 기울기
        if a!=0: # 직선의 기울기가 0이 아닐때
            b = y1 - (a*x1) # 직선의 y절편
            c = y3 + (x3/a) # 주어진 점을 지나고, 법선인 직선의 y절편
            x_ = a*(c-b)/(a**2+1) # 두 직선의 교점 x좌표
            y_ = (b-c)/(a**2+1)+c # 두 직선의 교점 y 좌표
            intersectionpoint = [float(x_),float(y_)] # 교점을 리스트로 표현한다.
            return intersectionpoint
        else: # 기울기(a)가 0일때_ c = y3 + (x3/a) 을 구할때 0으로 나누게 되므로 불가능하니 따로 정의해준다.
            intersectionpoint = [float(x3),float(y1)] # 교점을 리스트로 표현한다.
            return intersectionpoint
    else : # 기울기가 무한일때
        intersectionpoint = [float(x1),float(y3)] # 교점을 리스트로 표현한다.
        return intersectionpoint

# 함수 이용해서 교점 찾기
interpoints = []
for group in groups:
    x1 = float(group[0][0])
    y1 = float(group[0][1])
    x2 = float(group[1][0])
    y2 = float(group[1][1])
    x3 = float(A[0])
    y3 = float(A[1])
    i = ip(x1,y1,x2,y2,x3,y3)
    #print(i)
    if x1 <= i[0] <= x2: #두 점 사이에 교점이 위치해야 사각형까지의 거리라고 할 수 있다. y값은 x값에 종속적이니 x만 판별해주면 된다.
        interpoints.append(i) # 사각형의 변 위에 있는 교점만 추가해준다.

#print(interpoints) # 교점 좌표들 리스트.

# 거리 구하는 함수 제작
import math
def distance(x1,y1,x2,y2):
    dist_ = float(math.sqrt((x1-x2)**2 +(y1-y2)**2))
    return(dist_)

# 교점과 사각형 밖에 주어진 한 점 사이의 거리
distance1 = []
for interpoint in interpoints:
    xx1 = float(interpoint[0])
    yy1 = float(interpoint[1])
    xx2 = float(A[0])
    yy2 = float(A[1])
    d = distance(xx1,yy1,xx2,yy2)
    distance1.append(d)

# 교점까지의 거리가 가장 짧은 것이 한 점에서부터 사각형까지의 거리가 된다.
mindistance1 = min(distance1)

# 사각형의 꼭짓점이 점과 가장 가까울 경우
distance2 = []
for point in points:
    xxx1 = float(point[0])
    yyy1 = float(point[1])
    xxx2 = float(A[0])
    yyy2 = float(A[1])
    d = distance(xxx1,yyy1,xxx2,yyy2)
    distance2.append(d)
# 꼭짓점까지의 거리가 가장 짧은 것이 한 점에서부터 사각형까지의 거리가 된다.
mindistance2 = min(distance2)
# 최종_ 한 점과 사각형 사이의 거리
print("{:.2f}".format(min(mindistance1,mindistance2)))





