from PIL import Image
import numpy as np

def PIL_demo():
    # read an image.
    im = Image.open("./lena.jpg")
    width, height = im.size
    print("width:{0}\theight:{1}\n".format(width, height))	# 512, 512
    data = im.getdata()
    print("data:", data)
    np_data = np.asarray(data)
    print("np_data:", np_data)
    """
    for h in range(height):
        for w in range(width):
            rgb = im.getpixel((h, w))
            print(rgb, end=" ")
    """

    # write an image.
    im_w = Image.new("RGB", (width, height), "white")
    for h in range(height):
        for w in range(width):
            # im_w.putpixel((h, w), 129)    # red
            im_w.putpixel((h, w), (0, 255, 0))
    im_w.save("./result.png")


if __name__ == '__main__':
    main()