import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy


def imageToData(filename):

  grayImage = PIL.Image.open(filename).convert("L")
  grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)

  numImage = numpy.asarray(grayImage, dtype = float)
  numImage = 16 - numpy.floor(17 * numImage / 256)
  numImage = numImage.flatten()

  return numImage
