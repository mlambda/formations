import tensorflow as tf
# Paramètres du modèle
a = tf.Variable(tf.random_normal((1,1)), dtype=tf.float32,name='a')
b = tf.Variable(tf.random_normal((1,1)), dtype=tf.float32,name='b')
# Entrée et sortie du modèle
x = tf.placeholder(tf.float32,name="in")
y = tf.placeholder(tf.float32,name="out")
# Le modèle de regression linéaire
y_pred=tf.add(tf.multiply(a,x),b,name='y_pred')
# La fonction de perte (Loss)
loss = tf.reduce_sum(tf.square(y_pred - y),name='loss') 
# Méthode de recherche du minimum
lambda=0.1
train = tf.train.GradientDescentOptimizer(lambda).minimize(loss)
# Données
x_train = [1, 2, 3, 4]
y_train = [2.8,5.2,6.4,9.5]
