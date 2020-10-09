#Sauvegarde de tout le graphe de calcul
sauvegarde=tf.train.Saver()
sauvegarde.save(session,'graphs/mygraph')

!ls -l graphs/
