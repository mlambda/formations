# Sauvegarde d'un modèle complet
model.save('my_model.h5')

# Chargement du modèle, avec optimiseur, perte et métriques
model = tf.keras.models.load_model('my_model.h5')
