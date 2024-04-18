import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

# 画像ファイルを数値リストに変換する
def imageToData(filename):

# 画像を8x8のグレースケールに変換
  grayImage = PIL.Image.open(filename).convert("L")
  grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)

# 数値リストに変換
  numImage = numpy.asarray(grayImage, dtype = float)
  numImage = 16 - numpy.floor(17 * numImage / 256)
  numImage = numImage.flatten()

  return numImage
