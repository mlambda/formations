data = numpy.random.random((1000, 32))
labels = numpy.random.random((1000, 10))

model.evaluate(data, labels, batch_size=32)

# Ou avec un Dataset TensorFLow
dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32)

model.evaluate(dataset)
