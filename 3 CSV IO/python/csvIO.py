import pandas as pd
import numpy as np
import time

N = 1
read_time = []
write_time = []

for i in range(N):
    tic = time.time()
    M = pd.DataFrame.from_csv(f"C:/pseudorandomcoder/data_set/dataset{i}.csv")
    read_time.append(time.time() - tic)
    print(f"read dataset{i}.csv")
    
    tic = time.time()
    M.to_csv(f"C:/pseudorandomcoder/data_set/python/dataset{i}_out.csv")
    write_time.append(time.time() - tic)
    print(f"wrote dataset{i}_out.csv")

print(f"Average Read Time: {np.mean(read_time)}")
print(f"Average Write Time: {np.mean(write_time)}")