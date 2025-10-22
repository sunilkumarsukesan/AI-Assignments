from sklearn.preprocessing import MinMaxScaler, RobustScaler
import numpy as np

data = np.array([[5,8],[2,2],[3,5],[0,7],[2,9]])

scaler = MinMaxScaler()
robust_scaler = RobustScaler()

print(scaler.fit_transform(data))
print(robust_scaler.fit_transform(data))

