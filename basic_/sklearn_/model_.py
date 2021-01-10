from sklearn import datasets
from sklearn.linear_model import LinearRegression

###引入数据###
load_data = datasets.load_boston()
data_X = load_data.data
data_y = load_data.target
print(data_X.shape)
# (506, 13)data_X共13个特征变量

'''
数据训练完成之后得到模型，我们可以根据不同模型得到相应的属性和功能，并将其输出得到直观结果。
假如通过线性回归训练之后得到线性函数y=0.3x+1，我们可通过_coef得到模型的系数为0.3，通过_intercept得到模型的截距为1。
'''

###训练数据###
model = LinearRegression()
model.fit(data_X, data_y)
# 预测前4个数据
model.predict(data_X[:4, :])

###属性和功能###
print(model.coef_)
print(model.intercept_)

# 模型的参数
print(model.get_params())

# 对训练情况进行打分
print(model.score(data_X, data_y))
