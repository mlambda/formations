# With strings
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# With objects
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=[tf.keras.metrics.Accuracy()])

# With parameters
model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss="mse",       # Mean Squared Error
              metrics=['mae'])  # Mean Absolute Error
