from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = []

for i in range(1,11,2):
    data.append([i,i+1])

data_np_array = np.array(data)

robust = MinMaxScaler()

scaled = robust.fit_transform(data_np_array)

print(scaled)