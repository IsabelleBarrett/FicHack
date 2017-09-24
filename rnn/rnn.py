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

import re
words = re.findall(r'\w+', open('sample.txt').read().lower())

print(build_dataset(words)[0])
