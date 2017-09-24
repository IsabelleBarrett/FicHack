import tensorflow as tf
import collections

sess = tf.Session()

def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()

    for word in count:
        dictionary[word] = len(dictionary)
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

    return dictionary, reverse_dictionary

def RNN(x, weights, biases):
    x = tf.reshape(x, [-1, n_inputs])
    x = tf.split(x, n_inputs, 1)

    rnn_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)

    outputs, states = tf.contrib.rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

    return tf.matmul(outputs[-1], weights["out"]) + biases["out"]

import re
words = re.findall(r'\w+', open('sample.txt').read().lower())

dictionary, reverse_dictionary = build_dataset(words)

vocab_size = len(dictionary)
n_inputs = 3
n_hidden = 512

weights = {
    "out": tf.Variable(tf.random_normal([n_hidden, vocab_size]))
}
biases = {
    "out": tf.Variable(tf.random_normal([vocab_size]))
}

print(RNN(dictionary, weights, biases))
