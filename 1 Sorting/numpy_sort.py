import time
import numpy as np

N = int(1e5)
trials = int(1e3)

times = np.zeros((trials, 1))

for i in range(trials):
    data = np.random.rand(N, 1)
    tic = time.time()
    data = np.sort(data, axis=0)
    times[i] = time.time() - tic
    print(f'Completed {i} trials\n')

print(f'Average Time: {np.mean(times)}\n')