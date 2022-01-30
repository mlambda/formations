fig=plt.figure()

# ... #
fig.savefig("mon_plot",
    # --Optionnels--
    
    # Résolution de l'image,
    # ignore la valeur de fig si spécifié
    dpi=150,

    # png,pdf,jpg... 
    # peut être inclus dans le nom de fichier
    format="png", 
    
    # Fond du plot transparent,
    # ignore la valeur de fig si spécifié
    transparent=True
    )