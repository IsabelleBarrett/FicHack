import tensorflow as tf

sess = tf.Session()

a = tf.placeholder(tf.string)
b = tf.placeholder(tf.string)

concat_node = tf.string_join([a, b], " ")

print(sess.run(concat_node, {a: "hello", b: "world"}))
