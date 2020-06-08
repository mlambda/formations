# Utiliser une fonction d'activation :
layers.Dense(64, activation='sigmoid')
# Ou:
layers.Dense(64, activation=tf.keras.activations.sigmoid)

# L1 regularization des poids de la matrice :
layers.Dense(64, kernel_regularizer=tf.keras.regularizers.l1(0.01))

# L2 regularization des biais:
layers.Dense(64, bias_regularizer=tf.keras.regularizers.l2(0.01))

# Initialisation des poids avec une matrice orthogonale :
layers.Dense(64, kernel_initializer='orthogonal')

# Initialisation des biais avec une constante :
layers.Dense(64, bias_initializer=tf.keras.initializers.Constant(2.0))
