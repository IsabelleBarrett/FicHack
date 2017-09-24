import tensorflow as tf
import collections
import numpy as np

sess = tf.Session()

def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()

    for word in words:
        dictionary[word] = len(dictionary)
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))


    return dictionary, reverse_dictionary

import re
words = re.findall(r'\w+', open('sample.txt').read().lower())

dictionary, reverse_dictionary = build_dataset(words)

vocab_size = len(dictionary)
n_inputs = 3
n_hidden = 512

x = tf.placeholder("float", [None, n_inputs, 1])
y = tf.placeholder("float", [None, vocab_size])

weights = {
    "out": tf.Variable(tf.random_normal([n_hidden, vocab_size]))
}
biases = {
    "out": tf.Variable(tf.random_normal([vocab_size]))
}

def RNN(x, weights, biases):
    x = tf.reshape(x, [-1, n_inputs])
    x = tf.split(x, n_inputs, 1)

    rnn_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)

    outputs, states = tf.contrib.rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

    return tf.matmul(outputs[-1], weights["out"]) + biases["out"]

pred = RNN(x, weights, biases)
symbols_in_keys = [ dictionary[str(words[i])] for i in range(len(words)) ]
for i in range(32):
    keys = np.reshape(np.array(symbols_in_keys), [-1, n_inputs, 1])

# print(sess.run(pred, feed_dict={x: symbols_in_keys}))
