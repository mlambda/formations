import json
import pprint
# Serialize a model to JSON format
json_string = model.to_json()
pprint.pprint(json.loads(json_string))
# Load a model configuration
fresh_model = tf.keras.models.model_from_json(json_string)
