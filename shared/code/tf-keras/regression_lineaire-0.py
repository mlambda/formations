import tensorflow as tf

# Paramètres du modèle
a = tf.Variable(tf.random_normal((1,1)), dtype=tf.float32,name='a')
b = tf.Variable(tf.random_normal((1,1)), dtype=tf.float32,name='b')

# Entrée et sortie du modèle
x = tf.placeholder(tf.float32,name="in")
y = tf.placeholder(tf.float32,name="out")

# Données
x_train = [1, 2, 3, 4]
y_train = [2.99,5.004,6.98,9.001]
