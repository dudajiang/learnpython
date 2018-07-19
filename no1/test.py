# -*- coding: utf-8 -*-

from sklearn import datasets

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((1, -1))

print(digits.images[0])
print(data[0])