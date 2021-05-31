g = tf.get_default_graph()
y_pred = g.get_tensor_by_name("y_pred:0")
#x = g.get_tensor_by_name("in:0")
# ...

#Construction d'un nouveau calcul à partir de y_pred
new_op = tf.multiply(y_pred, 10)
new_y_pred = session.run(new_op,feed_dict={x:new_x})
print("new_op(",new_x, ") = ", new_y_pred)
