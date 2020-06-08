import tensorflow as tf
a = tf.constant(6)
b = tf.constant(7)
mul = tf.multiply(a, b, name='a.b')
print(mul)

