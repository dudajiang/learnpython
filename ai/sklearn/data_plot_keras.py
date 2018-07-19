import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
import matplotlib.pyplot as plt

# Generate dummy data
x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 1))

x_axis = np.arange(100,120,1)
x_predict = x_train[100:120]
y_real = y_train[100:120]


# #############################################################################
# Keras

model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
print(score)

y_predict =  model.predict(x_predict)

# #############################################################################
# Look at the results
lw = 2
plt.scatter(x_axis, y_real, color='darkorange', label='data')
plt.plot(x_axis, y_predict, color='navy', lw=lw, label='keras')
# plt.plot(x_axis, y_lin, color='c', lw=lw, label='Linear model')
# plt.plot(x_axis, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Keras')
plt.legend()
plt.show()