import numpy as np
import time

n = int(1e4)
trials = int(1e1)
run_time = []

for i in range(trials):
    A = np.ceil(100*np.random.rand(n, n))
    while(np.linalg.det(A) == 0):
        A = np.ceil(100*np.random.rand(n, n))

    t1 = time.time()
    inv_A = np.linalg.inv(A)
    run_time.append(time.time() - t1)
    print(f"{i+1} runs complete")

print(np.mean(run_time))