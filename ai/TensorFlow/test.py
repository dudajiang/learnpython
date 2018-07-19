import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.random_normal([2,20])
sess = tf.Session()
out = sess.run(a)
x,y = out

print(x,y)

plt.scatter(x,y)
plt.show()