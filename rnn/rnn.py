import tensorflow as tf

sess = tf.Session()

message = tf.placeholder(tf.string)

name = tf.Variable(["Steve", "Chris", "Alfred"], dtype= tf.string)

concat_node = tf.string_join([message, name], " ")

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(concat_node, {message: "hello"}))
