from django.test import TestCase

# https://www.tensorflow.org/guide/gpu
import tensorflow as tf
from tensorflow.python.client import device_lib


if __name__ == '__main__':
    tf.debugging.set_log_device_placement(True)
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)
    print(c)
    # print(device_lib.list_local_devices())
