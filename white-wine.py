import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

quality_lst = []
alcohol_lst = []
so2_lst = []
with open('./assets/winequality-white.csv', mode='r') as myfile:
    reader = csv.reader(myfile, delimiter=';')
    for row in reader:
        so2_lst.append(row[6])
        alcohol_lst.append(row[10])
        quality_lst.append(row[11])
quality_arr = np.array(quality_lst[1:], dtype=int)
alcohol_arr = np.array(alcohol_lst[1:], dtype=float)
so2_arr = np.array(so2_lst[1:], dtype=float)

# plt.plot(quality_arr)
# plt.show()


# plt.plot(quality_arr,alcohol_arr, 'x')
# plt.show()
srednie = []
idx = []
for i in range(3, 10):
    idx.append(i)
    srednie.append(np.mean(alcohol_arr[quality_arr == i]))

slope, intercept, r_val, p_val, std_err = stats.linregress(quality_arr, alcohol_arr)
idx = np.array(idx)

plt.plot(quality_arr, alcohol_arr, 'x')
plt.plot(idx, srednie, 'ro')
plt.plot(idx, slope*idx + intercept, 'g-')
plt.show()
