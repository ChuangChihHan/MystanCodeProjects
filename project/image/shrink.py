"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    This function is used to shrink the original image into 1/4 of its size by creating a blank image that is 1/4 of the
    original image size, replacing all the original image's pixels into the blank pixel, and then returning the canvas
    that includes the pixels of the original image.
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width//2, img.height//2)  # create a blank canvas that is 1/4 of the original image size
    for x in range(img.width):  # run through all the pixels in the original image
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)  # get the original image's pixels
            # get the blank image's pixel. need to divide x, y by 2 in order to match the pixels with the original ones.
            b_img_pixel = b_img.get_pixel(x//2, y//2)
            b_img_pixel.red = img_pixel.red
            b_img_pixel.green = img_pixel.green
            b_img_pixel.blue = img_pixel.blue
    return b_img


def main():
    """
    This program shows an image and then will show another image that are 1/4 of the original image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
