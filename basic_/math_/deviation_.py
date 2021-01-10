import numpy as np

arr1 = (5, 6, 7, 8, 9)
arr2 = (0, 5, 7, 9, 14)

mean1 = np.mean(arr1)
mean2 = np.mean(arr2)
print("mean of arr1: ", mean1)
print("mean of arr2: ", mean2)

variance1 = np.var(arr1)
variance2 = np.var(arr2)
print("variance of arr1: ", variance1)
print("variance of arr2: ", variance2)

standard_deviation1 = np.std(arr1)
standard_deviation2 = np.std(arr2)
print("standard deviation of arr1: ", standard_deviation1)
print("standard deviation of arr2: ", standard_deviation2)

