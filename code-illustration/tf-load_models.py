#Restauration du graphe sauvegardé
savedGraph = tf.train.import_meta_graph('graphs/mygraph.meta')
#session = tf.Session()
savedGraph.restore(session,tf.train.latest_checkpoint('graphs/'))

#Test du modèle avec de nouvelles valeurs
new_x=[5,10,50,100]
new_y_pred = session.run(y_pred,feed_dict={x:new_x})
print("y_pred(",new_x, ") = ", new_y_pred)
