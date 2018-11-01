import tensorflow as tf
import numpy as np
import tensorflow.contrib.eager as tfe

dataset = tf.data.Dataset.from_tensor_slices(
    (np.array([1.0, 2.0, 3.0, 4.0, 5.0]), np.random.uniform(size=(5, 2)))
)
iterator = dataset.make_one_shot_iterator()
one_element = iterator.get_next()
with tf.Session() as sess:
    try:
        while True:
            aa = one_element 
            print(sess.run(aa))
            print(sess.run(aa[0]))
            print(sess.run(aa[1][0]))
            # print(sess.run(one_element))

    except tf.errors.OutOfRangeError:
        print("end!")
