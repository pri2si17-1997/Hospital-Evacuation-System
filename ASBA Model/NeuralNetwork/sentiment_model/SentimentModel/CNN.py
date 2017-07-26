import tensorflow as tf
import numpy as np

class CNN():
	def __init__(self, seq_len, classes_count, vocabulari_size, embed_size, filter_size, filer_count, L2_regularization_lambda = 0.0):
		self._inputX = tf.placeholder(tf.int32, [None, seq_len], name = "inputX")
		self._inputY = tf.placeholder(tf.float32, [None, classes_count], name = "inputY")
		self._droputProb = tf.placeholder(tf.float32, name = "dropoutProb")

		L2_Loss = tf.constants(0.0)

		with tf.device('/cpu:0'), tf.name_scope("embedding"):
			self._W = tf.Variable(tf.random_uniform([vocabulari_size, embed_size], -1.0, 1.0), name = "W")
			self._embedChars = tf.nn.embedding_lookup(self._W, self._inputX)
			self._embedCharsExpand = tf.expand_dims(self._embedChars, -1)

		outputs = []

		for index, 
