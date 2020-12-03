# Sérialisation d'un modèle vers JSON
json_string = model.to_json()

# Chargement d'un modèle depuis JSON
fresh_model = tf.keras.models.model_from_json(json_string)
