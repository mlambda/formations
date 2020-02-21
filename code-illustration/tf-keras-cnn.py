model = Models.Sequential()
#Un premier Layer de 10 convolutions de 3x3 pixels
model.add(Layers.Conv2D(10,kernel_size=(3,3),activation='relu',
                        input_shape=(150,150,3)))
#Un Layer "max pooling"
model.add(Layers.MaxPool2D(3,3))
#Un Layer "Flatten"
model.add(Layers.Flatten())
#Un Layer "Dense" avec 6 sorties et un softmax
model.add(Layers.Dense(6,activation='softmax'))
#Compilation du modèle avec la définition de la loss
model.compile(optimizer=Optimizer.Adam(lr=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
