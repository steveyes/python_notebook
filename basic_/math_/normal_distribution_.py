import matplotlib.pyplot as plt
import numpy as np

n = 100000
box_width = 1
row_count = 1000
col_count = 1000

a = np.ones(n) * box_width / 2
for i in range(row_count):
    delta = (np.random.randint(0, 2, n) - 0.5) * box_width / col_count
    a += delta
    a = np.clip(a, 0, box_width)

plt.hist(a, col_count // 2)
plt.show()
