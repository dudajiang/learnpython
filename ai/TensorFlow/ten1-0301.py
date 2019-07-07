X = tf.placeholder('float')
Y = tf.placeholder('float')

W = tf.Variable(tf.random_normal([1]),name = 'weight')
b = tf.Variable(tf.zeros([1]),name = 'bias')

z = tf.multiply(X,W) + b

cost = tf.reduce_mean((tf.square(Y-z)))
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)