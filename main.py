from mern import NumericOutlier

x = [1, 2, 100, 20]

obj = NumericOutlier()
pred = obj._iqr(x)
print(pred)
