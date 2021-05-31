model = tf.keras.Sequential()
model.add(layers.Embedding(input_dim=1000, output_dim=64))
model.add(layers.GRU(128))
model.add(layers.Dense(10, activation='softmax'))
model.summary()

