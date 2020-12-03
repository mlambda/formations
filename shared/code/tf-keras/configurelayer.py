# Utiliser une fonction d'activation
tf.keras.layers.Dense(64, activation="sigmoid")
# Ou
tf.keras.layers.Dense(64, activation=tf.keras.activations.sigmoid)

# Régularisation L1 des poids de la matrice
tf.keras.layers.Dense(64,
                      kernel_regularizer=tf.keras.regularizers.l1(0.01))

# Régularisation L2 des biais
tf.keras.layers.Dense(64,
                      bias_regularizer=tf.keras.regularizers.l2(0.01))

# Initialisation des poids avec une matrice orthogonale
tf.keras.layers.Dense(64,
                      kernel_initializer="orthogonal")

# Initialisation des biais avec une constante :
tf.keras.layers.Dense(
    64, bias_initializer=tf.keras.initializers.Constant(2.0))
