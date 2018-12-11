# coding=utf-8
"""
Author: Héctor Sánchez
Date: February-24-2018
Last Modification: December-24-2018
Description: MNIST 
"""
import os
import numpy as np

from utils_MNIST import load_mnist

if __name__=='__main__':
  MNIST_path = './data/'
  MNIST_files = ['train-images.idx3-ubyte','train-labels.idx1-ubyte',
                 't10k-images.idx3-ubyte','t10k-labels.idx1-ubyte']
  
  train_ims = load_mnist(MNIST_path+MNIST_files[0])
  train_cls  = load_mnist(MNIST_path+MNIST_files[1])
  test_ims = load_mnist(MNIST_path+MNIST_files[2])
  test_cls= load_mnist(MNIST_path+MNIST_files[3])
