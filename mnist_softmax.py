

#This file contains the simple softmax egression apllied on MNIST dataset that has pictures of digits from 0-9 and correspondng labels. Predict the label(number) if feeded with a picture of a digit.
#To understand better visit: https://www.tensorflow.org/get_started/mnist/beginners

#Download the MNIST dataset
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b) #Predicted output

y_ = tf.placeholder(tf.float32, [None, 10]) #Labeled or Known output

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), eduction_indices=[1])) #Loss

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy) #Learning Here

sess = tf.InteractiveSession()

tf.global_variables_initializer().run()

for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) #accuracy of neural net

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
