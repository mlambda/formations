from tensorflow.keras import layers as kl

model = tf.keras.Sequential()
# Il est impératif de spécifier input_shape pour la première couche :
model.add(layers.Dense(64, activation='sigmoid', input_shape=(32,)))
# Ajouter une autre couche :
model.add(layers.Dense(64, activation='relu'))
# Une dernière couche de classification avec softmax ;
model.add(layers.Dense(10, activation='softmax'))
