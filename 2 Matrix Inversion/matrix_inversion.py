import numpy as np
from time import time
from numpy.linalg import inv

n = int(1e3)
trials = int(1e1)
run_time = []

for i in range(trials):
    A = np.random.randint(1, 100, (n, n))

    t1 = time()
    inv_A = inv(A)
    run_time.append(time() - t1)
    print(f"{i+1} runs complete")

print(f"Average runtime: {np.mean(run_time)}")  