from PIL import Image
import numpy as np

def compare_2_imgs():
    # read an image.
    im1 = Image.open("./lena.png")
    width, height = im1.size
    print("width:{0}\theight:{1}\n".format(width, height))	# 512, 512
    data = im1.getdata()
    np_data_1 = np.asarray(data)
    print("np_data_1:", np_data_1)
    """
    """

    # read an image.
    im2 = Image.open("./lena_modified.png")
    width, height = im2.size
    print("width:{0}\theight:{1}\n".format(width, height))	# 512, 512
    data = im2.getdata()
    np_data_2 = np.asarray(data)
    print("np_data_2:", np_data_2)
    print("np_data_2.shape:", np_data_2.shape)
    """
    """

    """
    # Method 1(numpy)
    np_data_delta = np_data_2 - np_data_1
    print("np_data_delta: ", np_data_delta)
    print("np_data_delta.shape: ", np_data_delta.shape)
    np_data_delta = np_data_delta.reshape(height, width)

    im_result = Image.fromarray(np.uint8(np_data_delta))
    width, height = im_result.size
    print("width:{0}\theight:{1}\n".format(width, height))	# 512, 512
    """

    # Method 2(w/o numpy)
    # im_w = Image.new("RGBA", (width, height), "white")
    im_w = Image.new("RGBA", (width, height), "white")
    print(im1.mode)

    for h in range(height):
        for w in range(width):
            rgb1 = im1.getpixel((h, w))
            rgb2 = im2.getpixel((h, w))
            # print(rgb1, rgb2)
            if rgb1 != rgb2:
                print("not equal")
                im_w.putpixel((h, w), rgb2)
            else:
                im_w.putpixel((h, w), (0, 0, 0, 0))

    im_w.save("./ans2.png")


if __name__ == '__main__':
    compare_2_imgs()