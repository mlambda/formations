model = tf.keras.models.Sequential()
model.add(MyLayer(10))
model.add(tf.keras.layers.Activation("softmax"))

model.compile(optimizer=tf.keras.optimizers.RMSprop(0.001),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(data, labels, batch_size=32, epochs=5)
