#!/usr/bin/env python3
# coding: utf-8
# File: Q2.py
# Author: lxw
# Date: 7/12/17 21:30 PM


from PIL import Image
import numpy as np


def compare_2_imgs_method1():
    """
    w/o numpy
    """
    # read an image.
    im1 = Image.open("./lena.png")
    width, height = im1.size
    # print("width:{0}\theight:{1}".format(width, height))	# 512, 512

    # read an image.
    im2 = Image.open("./lena_modified.png")
    width, height = im2.size
    # print("width:{0}\theight:{1}".format(width, height))  # 512, 512

    im_w = Image.new("RGBA", (width, height))
    # im_w = Image.new("RGBA", (width, height), "white")    # OK
    for h in range(height):
        for w in range(width):
            rgb1 = im1.getpixel((h, w))
            rgb2 = im2.getpixel((h, w))
            if rgb1 != rgb2:
                # print(rgb1, rgb2)
                im_w.putpixel((h, w), rgb2)
            else:
                # print(id(rgb1), id(rgb2))   # id(rgb1) != id(rgb2) but rgb1 == rbg2
                im_w.putpixel((h, w), (0, 0, 0, 0))

    im_w.save("./ans_two.png")


def compare_2_imgs_method2():
    """
    numpy
    这种方法太麻烦,而且结果不对,只看看numpy和PIL的用法就行
    """
    im1 = Image.open("./lena.png")
    width, height = im1.size
    # print("width:{0}\theight:{1}\n".format(width, height))  # 512, 512
    data = im1.getdata()
    np_data_1 = np.asarray(data)
    """
    print("np_data_1: ", np_data_1)
    print("np_data_1.shape: ", np_data_1.shape)
    """

    # read an image.
    im2 = Image.open("./lena_modified.png")
    width, height = im2.size
    # print("width:{0}\theight:{1}\n".format(width, height))	# 512, 512
    data = im2.getdata()
    np_data_2 = np.asarray(data)
    """
    print("np_data_2: ", np_data_2)
    print("np_data_2.shape: ", np_data_2.shape)
    """

    np_data_delta = np_data_2 - np_data_1
    """
    print("np_data_delta: ", np_data_delta)
    print("np_data_delta.shape: ", np_data_delta.shape)
    """
    np_data_delta = np_data_delta.reshape(height, width, 4)
    """
    print("np_data_delta: ", np_data_delta)
    print("np_data_delta.shape: ", np_data_delta.shape)
    """

    im_result = Image.fromarray(np.uint8(np_data_delta))
    print(im_result.getdata())
    width, height = im_result.size
    # print("width:{0}\theight:{1}\n".format(width, height))	# 512, 512
    for h in range(height):
        for w in range(width):
            rgb1 = im_result.getpixel((h, w))
            if rgb1 != (0, 0, 0, 0):
                rgb = rgb1[0:3] + (255,)
                im_result.putpixel((h, w), rgb)
    im_result.save("./ans_two.png")


if __name__ == '__main__':
    compare_2_imgs_method1()
    # compare_2_imgs_method2()
