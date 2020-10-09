# Exécution du graphe 1000 fois sur l'ensemble des données
session = tf.Session()
init = tf.global_variables_initializer()
session.run(init) # reset a et b
for i in range(1000):
    session.run(train, {x: x_train, y: y_train})
# Evaluation de l'entrainement du modèle
a_app,b_app,erreur=session.run([a,b,loss],{x:x_train,y:y_train})
print("a: %s b: %s loss: %s"%(a_app, b_app, erreur))
