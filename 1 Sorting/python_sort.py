import random
import time
from numpy import mean

N = int(1e5)
trials = int(1e3)

times = [0]*trials
my_rand = random.Random()

for i in range(trials):
    data = [my_rand.random() for j in range(N)]
    tic = time.time()
    # data = sorted(data)
    data.sort()
    times[i] = time.time() - tic
    print(f'Completed {i} trials\n')

print(f'Average Time: {mean(times)}\n')