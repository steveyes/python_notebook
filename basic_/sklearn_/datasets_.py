from sklearn import datasets
import matplotlib.pyplot as plt

# 构造的各种参数可以根据自己需要调整
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)


# 绘制构造的数据
plt.figure()
plt.scatter(X, y)
plt.show()
