# Sauvegarde des poids dans un fichier HDF5
model.save_weights("my_model.h5", save_format="h5")

# Restauration des poids du modèle
model.load_weights("my_model.h5")
