model = tf.keras.models.Sequential()

# Specifying input_shape is mandatory for the first layer
model.add(tf.keras.layers.Dense(64, activation="sigmoid", input_shape=(32,)))

# Another hidden layer
model.add(tf.keras.layers.Dense(64, activation="relu"))

# Final layer with a softmax activation
model.add(tf.keras.layers.Dense(10, activation="softmax"))
