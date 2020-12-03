class MyLayer(tf.keras.layers.Layer):
    def __init__(self, output_dim, **kwargs):
        super().__init__(**kwargs)
        self.output_dim = output_dim

    def build(self, input_shape):
        self.kernel = self.add_weight(
            name='kernel', shape=(input_shape[1], self.output_dim),
            initializer='uniform', trainable=True)

    def call(self, inputs):
        return inputs @ self.kernel

    def get_config(self):
        base_config = super().get_config()
        base_config['output_dim'] = self.output_dim
        return base_config

    @classmethod
    def from_config(cls, config):
        return cls(**config)
