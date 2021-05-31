data = numpy.random.random((1000, 32))
labels = numpy.random.random((1000, 10))

model.fit(data, labels, epochs=10, batch_size=32)
