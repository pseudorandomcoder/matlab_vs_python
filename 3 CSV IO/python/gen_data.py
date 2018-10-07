import pandas as pd
import numpy as np

N = 10
n = 36
m = int(1e6)

for i in range(N):
    M = np.random.rand(m, n)
    M_df = pd.DataFrame(M)
    M_df.to_csv(f"C:/Users/pseud/Google Drive/YouTube Videos/MATLAB vs Python/3 CSV IO/python/dataset{i}.csv")

# M = pd.DataFrame.from_csv(f"C:/Users/pseud/Google Drive/YouTube Videos/MATLAB vs Python/3 CSV IO/python/dataset0.csv")
# M.to_csv(f"C:/Users/pseud/Google Drive/YouTube Videos/MATLAB vs Python/3 CSV IO/python/dataset0_2_out.csv")
