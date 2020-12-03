callbacks = [
    # Interrompt l'apprentissage si `val_loss` ne s'améliore plus depuis
    # 2 epochs
    tf.keras.callbacks.EarlyStopping(patience=2,
                                     monitor="val_loss"),
    # Sauvegarde le meilleur model
    tf.keras.callbacks.ModelCheckpoint(filepath='models/bestmodel.hdf5',
                                       verbose=1,
                                       save_best_only=True)
]
model.fit(data, labels, batch_size=32, epochs=5, callbacks=callbacks,
          validation_split=0.2)
