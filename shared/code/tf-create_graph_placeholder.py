import tensorflow as tf
a = tf.placeholder(tf.float32 , name = "var_a")
b = tf.placeholder(tf.float32 , name = "var_b")
mul = tf.multiply(a, b, name='a.b')
print(mul)
