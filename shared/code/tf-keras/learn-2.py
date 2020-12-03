data = numpy.random.random((1000, 32))
labels = numpy.random.random((1000, 10))

val_data = numpy.random.random((100, 32))
val_labels = numpy.random.random((100, 10))

model.fit(data, labels, epochs=10, batch_size=32,
          validation_data=(val_data, val_labels))
