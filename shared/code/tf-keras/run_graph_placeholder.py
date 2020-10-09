with tf.Session() as session:
    result = session.run(mul, feed_dict={a:[1,2,3], b:[4,5,6]})
    print(result)
    
