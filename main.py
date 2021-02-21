from mern import NumericOutlier

obj = NumericOutlier()
x = [11,31,21,19,8,54,35,26,23,13,29,17]

# using Z Score
print(obj.find(x, "zscore"))

# using Inter Quartile Range Score
print(obj.find(x, "iqr"))