model = tf.keras.models.Sequential()
# A first layer of 3 x 3 kernels
model.add(
    tf.keras.layers.Conv2D(
        10, kernel_size=(3, 3), activation="relu", input_shape=(150, 150, 3)
    )
)
# Max pooling layer
model.add(tf.keras.layers.MaxPool2D(3, 3))
# Flatten the result of the MaxPool2D to feed it to a Dense
model.add(tf.keras.layers.Flatten())
# Final layer: fully dependent on the output
model.add(tf.keras.layers.Dense(6, activation="softmax"))
# Model compilation with a fitting loss & optimizer and informative metrics
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
