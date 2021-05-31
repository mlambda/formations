# Model config to JSON
json_string = model.to_json()

# Model config from JSON
fresh_model = tf.keras.models.model_from_json(json_string)
