import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0], cmap="Greys")   #数値データをグレーの濃淡
plt.show()   #作成した画像を表示