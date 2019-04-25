import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
model = Sequential()
