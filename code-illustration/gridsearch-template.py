lr_grid = [ 0.1 0.001 0.0001 0.00001]
for lr in lr_grid:
    train = tf.train.GradientDescentOptimizer(lr).minimize(loss)
    ...


