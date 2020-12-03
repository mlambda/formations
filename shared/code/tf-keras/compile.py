# Compilation du modèle avec entropie croisée et accuracy
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Compilation équivalente mais permet la customisation
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=[tf.keras.metrics.Accuracy()])

# Exemple de compilation pour un problème de régression
model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss="mse",       # Mean Squared Error
              metrics=['mae'])  # Mean Absolute Error
