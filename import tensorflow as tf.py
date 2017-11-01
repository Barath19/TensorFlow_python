import tensorflow as tf

a = tf.constant([2])
b = tf.constant([15600000000])

c = tf.add(a,b)

session = tf.Session()

result = session.run(c)

session.close()

with tf.Session() as session:
	result = session.run(c)
	print(result)