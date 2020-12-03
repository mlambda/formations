model = tf.keras.models.Sequential()
# Il est impératif de spécifier input_shape pour la première couche
model.add(tf.keras.layers.Dense(64,
                                activation="sigmoid",
                                input_shape=(32,)))
# Ajouter une autre couche
model.add(tf.keras.layers.Dense(64, activation="relu"))
# Une dernière couche de classification avec softmax
model.add(tf.keras.layers.Dense(10, activation="softmax"))
