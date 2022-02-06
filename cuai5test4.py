A = list(map(int, input().split()))
C1 = list(map(int, input().split()))
C2 = list(map(int, input().split()))
C3 = list(map(int, input().split()))
C4 = list(map(int, input().split()))
import numpy as np
A = np.array(A)
C1 = np.array(C1)
C2 = np.array(C2)
C3 = np.array(C3)
C4 = np.array(C4)

points = np.vstack((C1,C2,C3,C4))
print(points) #
# 한 점이 사각형 밖의 점으로 주어졌으니
# 주어진 점 A와 사각형 이루는 점들 중 가장 가까운 두 점을
# 이은 선분이 점 A와의 거리가 가장 가까울 것이다.
# import math
# def distance(X,Y):
#     s = math.sqrt(math.pow(X[0]-Y[0],2) + math.pow(X[1]-Y[1]),2)
#     return s

# 점들에서 A의 x,y좌표 뺀 리스트들 만들기.
import math
points_1 = points - A
print(points_1) #
print(points_1[0]) #

# A에서 점까지의 거리 d를 구하고 거리 리스트에 집어넣기
distance = []
for i in range(0,4):
    d = math.sqrt(math.pow(points_1[i][0],2)+math.pow(points_1[i][1],2))
    distance.append(d)
print(distance) #
# 인덱스 붙이기
index_distance = [0, 1, 2, 3]
newdistance = np.vstack((distance,index_distance))
print(newdistance) #
# 세로로 변환시키기
newnewdistance = np.array(newdistance).T
print(newnewdistance) #
# 리스트 변환시키고
newnewdistance = list(newnewdistance)
# 정렬
newnewdistance.sort(key = lambda x:x[1])
print(newnewdistance)

# 위에서 두개의 리스트의 두번째 column의 인덱스값들을 받아오기
index1 = newnewdistance[0][1]
index2 = newnewdistance[1][1]
print(index1)
print(index2)

# 처음 주어진 점들 중 뭐가 가까운지 인덱스로 찾기
point1 = points[int(index1)]
point2 = points[int(index2)]
print(point1)
print(point2)

# 거리 구하기
def cal_dist(x1, y1, x2, y2, a, b):
    area = abs((x1-a) * (y2-b) - (y1-b) * (x2 - a))
    AB = ((x1-x2)**2 + (y1-y2)**2) **0.5
    finaldistance = area/AB
    print("{:.2f}".format(finaldistance))

cal_dist(point1[0],point1[1],point2[0],point2[1],A[0],A[1])

