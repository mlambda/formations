while (perf > perf_precedente):
    perf_precedente = perf
    ajouter_une_couche(model)
    apprendre(model,data_train)
    perf = calcul_perf(model, data_validation)
