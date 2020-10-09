matrix1 = tf.constant([[1., 2.],[3., 4.]])
matrix2 = tf.constant([[5.,6.],[7.,8.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as session:
        result = session.run(product)
        print(result)
