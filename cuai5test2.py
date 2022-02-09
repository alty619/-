# 2.

# pandas import해서 data.csv 불러오기
import pandas as pd
data = pd.read_csv("C:/Users/youth_0619/OneDrive - 중앙대학교/바탕 화면/data.csv")

# matplotlib의 pyplot함수 이용해서 그래프 그리기
import matplotlib.pyplot as plt
plt.plot(data['x'], data['y'])  # data의 x column을 x 좌표에, y column을 y 좌표에 도식.
plt.show()