# Le modèle de regression linéaire
y_pred=tf.add(tf.multiply(a,x),b,name='y_pred')

# La fonction de perte (Loss)
loss = tf.reduce_sum(tf.square(y_pred - y),name='loss') 

# Méthode de recherche du minimum
lr=0.01
train = tf.train.GradientDescentOptimizer(lr).minimize(loss)
