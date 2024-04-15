import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

for i in range(50):  #　50回繰り返す
    plt.subplot(5, 10, i + 1)  #　5x10に順番に表示する
    plt.imshow(digits.images[i], cmap="Greys")
    plt.title(digits.target[i])
    plt.axis('off')  # 枠線を非表示にする

plt.show()
