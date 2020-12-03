model = tf.keras.models.Sequential()
# Une première couche de 10 convolutions de 3x3 pixels
model.add(tf.keras.layers.Conv2D(10,
                                 kernel_size=(3, 3),
                                 activation="relu",
                                 input_shape=(150, 150, 3)))
# Une couche de max pooling
model.add(tf.keras.layers.MaxPool2D(3,3))
# Une couche de redimensionnement, qui aplatit le tenseur
model.add(tf.keras.layers.Flatten())
# Une couche "Dense" avec 6 sorties et un softmax
model.add(tf.keras.layers.Dense(6, activation="softmax"))
# Compilation du modèle avec la définition de la loss
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
