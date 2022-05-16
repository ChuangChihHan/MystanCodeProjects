"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:a blurry image
    This function is used to create a blurry image by replacing the original pixel with the average of its neighboring
    dots.
    There are 9 conditions in total and each conditions has its corresponding neighboring dots
    1. for (x,y) = (0, 0). They have 3 neighboring dots
    2. for (x, y) = (0, height). They have 3 neighboring dots
    3. for (x, y) = (width, 0). They have 3 neighboring dots
    4. for (x, y) = (width, height). They have 3 neighboring dots
    5. for cases that x (except x = 0, x = width) is on the border of the line where y = 0. (5 neighboring dots)
    6. for cases that y (except y = 0, y = height) is on the border of the line where x = 0 (5 neighboring dots)
    7. for cases that x (except x = 0, x = width) is on the border of the line where y = height (5 neighboring dots)
    8. for cases that y (except y = 0, y = height) is on the border of the line where x = width (5 neighboring dots)
    9. for general cases within the boundary that most (x, y) faces. They have 8 neighboring dots.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(new_img.width):
        for y in range(new_img.height):
            img_pixel = img.get_pixel(x, y)
            new_img_pixel = new_img.get_pixel(x, y)
            # for (x,y) = (0, 0). They have 3 neighboring dots
            if (x == 0) and (y == 0):
                img_pixel1 = img.get_pixel(x, y+1)
                img_pixel2 = img.get_pixel(x+1, y)
                img_pixel3 = img.get_pixel(x+1, y+1)
                # calculate the average for the blurry pixel
                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red) // 4
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green) // 4
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue) // 4
            # for (x, y) = (0, height). They have 3 neighboring dots
            elif (x == 0) and (y == new_img.height-1):
                img_pixel1 = img.get_pixel(x, y-1)
                img_pixel2 = img.get_pixel(x+1, y)
                img_pixel3 = img.get_pixel(x+1, y-1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red) // 4
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green) // 4
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue) // 4
            # for (x, y) = (width, height). They have 3 neighboring dots
            elif (x == new_img.width-1) and (y == new_img.height-1):
                img_pixel1 = img.get_pixel(x, y-1)
                img_pixel2 = img.get_pixel(x-1, y)
                img_pixel3 = img.get_pixel(x-1, y-1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red) // 4
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green) // 4
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue) // 4
            # for (x, y) = (width, 0). They have 3 neighboring dots
            elif (x == new_img.width-1) and (y == 0):
                img_pixel1 = img.get_pixel(x, y+1)
                img_pixel2 = img.get_pixel(x-1, y)
                img_pixel3 = img.get_pixel(x-1, y+1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red) // 4
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green) // 4
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue) // 4
            # for cases that x (except x = 0, x = width) is on the border of the line where y = 0. (5 neighboring dots)
            elif (x != 0 and x != new_img.width-1) and (y == 0):
                img_pixel1 = img.get_pixel(x-1, y)
                img_pixel2 = img.get_pixel(x+1, y)
                img_pixel3 = img.get_pixel(x-1, y+1)
                img_pixel4 = img.get_pixel(x, y+1)
                img_pixel5 = img.get_pixel(x+1, y+1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red + img_pixel4.red + img_pixel5.red) // 6
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green +img_pixel4.green + img_pixel5.green) // 6
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue +img_pixel4.blue + img_pixel5.blue) // 6

            # for cases that y (except y = 0, y = height) is on the border of the line where x = 0 (5 neighboring dots)
            elif (y != 0 and y != new_img.height-1) and (x == 0):
                img_pixel1 = img.get_pixel(x, y+1)
                img_pixel2 = img.get_pixel(x, y-1)
                img_pixel3 = img.get_pixel(x+1, y+1)
                img_pixel4 = img.get_pixel(x+1, y)
                img_pixel5 = img.get_pixel(x+1, y+1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red + img_pixel4.red + img_pixel5.red) // 6
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green +img_pixel4.green + img_pixel5.green) // 6
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue +img_pixel4.blue + img_pixel5.blue) // 6

            # for cases that x (except x = 0, x = width) is on the border of the line where y = height (5 neighboring dots)
            elif (x != 0 and x != new_img.width-1) and (y == new_img.height-1):
                img_pixel1 = img.get_pixel(x-1, y)
                img_pixel2 = img.get_pixel(x+1, y)
                img_pixel3 = img.get_pixel(x-1, y-1)
                img_pixel4 = img.get_pixel(x, y-1)
                img_pixel5 = img.get_pixel(x+1, y-1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red + img_pixel4.red + img_pixel5.red) // 6
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green +img_pixel4.green + img_pixel5.green) // 6
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue +img_pixel4.blue + img_pixel5.blue) // 6

            # for cases that y (except y = 0, y = height) is on the border of the line where x = width (5 neighboring dots)
            elif (y != 0 and y != new_img.height-1) and (x == new_img.width-1):
                img_pixel1 = img.get_pixel(x, y-1)
                img_pixel2 = img.get_pixel(x, y+1)
                img_pixel3 = img.get_pixel(x-1, y-1)
                img_pixel4 = img.get_pixel(x-1, y)
                img_pixel5 = img.get_pixel(x-1, y-1)

                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red + img_pixel4.red + img_pixel5.red) // 6
                new_img_pixel.green = (img_pixel.green + img_pixel1.green + img_pixel2.green + img_pixel3.green +img_pixel4.green + img_pixel5.green) // 6
                new_img_pixel.blue = (img_pixel.blue + img_pixel1.blue + img_pixel2.blue + img_pixel3.blue +img_pixel4.blue + img_pixel5.blue) // 6

            # for general cases within the boundary that most (x, y) faces. They have 8 neighboring dots.
            else:
                # get all the neighboring dots' pixels
                img_pixel1 = img.get_pixel(x - 1, y)
                img_pixel2 = img.get_pixel(x + 1, y)
                img_pixel3 = img.get_pixel(x - 1, y - 1)
                img_pixel4 = img.get_pixel(x, y - 1)
                img_pixel5 = img.get_pixel(x + 1, y - 1)
                img_pixel6 = img.get_pixel(x - 1, y + 1)
                img_pixel7 = img.get_pixel(x, y + 1)
                img_pixel8 = img.get_pixel(x + 1, y + 1)
                # calculate the average for the blurry pixel
                new_img_pixel.red = (img_pixel.red + img_pixel1.red + img_pixel2.red + img_pixel3.red + img_pixel4.red + img_pixel5.red + img_pixel6.red + img_pixel7.red + img_pixel8.red) // 9
                new_img_pixel.green = (img_pixel.green + img_pixel.green + img_pixel2.green + img_pixel3.green + img_pixel4.green + img_pixel5.green + img_pixel6.green + img_pixel7.green + img_pixel8.green) // 9
                new_img_pixel.blue = (img_pixel.blue + img_pixel.blue + img_pixel2.blue + img_pixel3.blue + img_pixel4.blue + img_pixel5.blue + img_pixel6.blue + img_pixel7.blue + img_pixel8.blue) // 9
    return new_img


def main():
    """
    This program is used to read in an image, show it, and then used blurred_img function to makes it look blurry, and
    and then display it.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
