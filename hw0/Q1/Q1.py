#!/usr/bin/env python3
# coding: utf-8
# File: Q2.py
# Author: lxw
# Date: 7/12/17 21:30 PM

import numpy
import random

class Q1:
    heightA = 100
    widthA = 200
    heightB = 200
    widthB = 300
    def create_matrix(self):
        with open("./matrixA.txt", "w") as f:
            for row in range(self.heightA):
                for col in range(self.widthA):
                    f.write("{} ".format(random.randint(-100, 100)))
                f.write("\n")

        with open("./matrixB.txt", "w") as f:
            for row in range(self.heightB):
                for col in range(self.widthB):
                    f.write("{} ".format(random.randint(-100, 100)))
                f.write("\n")

    def run_Q1(self):
        matrix_a = numpy.loadtxt("./matrixA.txt")
        # print(matrix_a)
        print(matrix_a.shape)
        matrix_b = numpy.loadtxt("./matrixB.txt")
        # print(matrix_b)
        print(matrix_b.shape)
        # matrix_c = matrix_a * matrix_b	# NO
        matrix_c = numpy.dot(matrix_a, matrix_b)
        print(matrix_c)
        print(matrix_c.shape)
        matrix_c = matrix_c.flatten()
        print(matrix_c)
        print(matrix_c.shape)
        matrix_c_list = matrix_c.tolist()
        print(matrix_c_list)
        matrix_c_list.sort()
        print(matrix_c_list)
        with open("./ans_one.txt", "w") as f:
            for num in matrix_c_list:
                f.write("{}\n".format(int(num)))


if __name__ == '__main__':
	q1 = Q1()
	q1.create_matrix()
	q1.run_Q1()


"""
Reference:
[numpy文件存取](http://hyry.dip.jp/tech/book/page/scipy/numpy_file.html)
"""
