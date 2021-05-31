# Activation function
tf.keras.layers.Dense(64, activation="sigmoid")
# Or
tf.keras.layers.Dense(64, activation=tf.keras.activations.sigmoid)

# Weights with L1 regularization
tf.keras.layers.Dense(64,
                      kernel_regularizer=tf.keras.regularizers.l1(0.01))

# Biases with L2 regularization
tf.keras.layers.Dense(64,
                      bias_regularizer=tf.keras.regularizers.l2(0.01))

# Weights initialization with an orthogonal matrix
tf.keras.layers.Dense(64,
                      kernel_initializer="orthogonal")

# Biases initialization with a constant
tf.keras.layers.Dense(
    64, bias_initializer=tf.keras.initializers.Constant(2.0))
