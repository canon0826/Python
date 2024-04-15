import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データーの個数=",len(digits.images))
print("画像データ=",digits.images[0])
print("何の数字か=",digits.target[0])