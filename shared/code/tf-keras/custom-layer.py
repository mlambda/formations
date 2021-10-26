class MyLayer(tf.keras.layers.Layer):
    # Sauvegarde des paramètres
    def __init__(self, output_dim, **kwargs):
        super().__init__(**kwargs)
        self.output_dim = output_dim

    # Création des poids
    def build(self, input_shape):
        self.kernel = self.add_weight(
            name="kernel",
            shape=(input_shape[1], self.output_dim),
            initializer="uniform",
            trainable=True,
        )

    # Calcul de la couche
    def call(self, inputs):
        return inputs @ self.kernel
