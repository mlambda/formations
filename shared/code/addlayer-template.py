while perf > previous_perf:
    previous_perf = perf
    model = add_layer(model)
    model.fit(data_train)
    perf = model.eval(data_eval)
