
from image import Image
import numpy as np

def adjust_brighteness(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels=image.array.shape #represents the x and y pixels and channels (R,G,B colours)
    #make an empty image so that we won't mess up the original image
    new_im=Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    #non-vectorized version
    #for x in range(x_pixels):
    #   for y in range(y_pixels):
    #       for c in range(num_channels):
    #           new_im.array[x, y, c] = image.array[x, y, c] * factor

    #vectorized version
    new_im.array=image.array*factor
    return new_im

def adjust_contrast(image, factor, mid=0.5):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels=image.array.shape
    new_im=Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

    #vectorized version
    #new_im.array = (image.array - mid) * factor + mid

    return new_im
    pass

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                #using naive implementation of searching through elements and summing up
                total=0

    return new_im           
    pass

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    pass

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    pass
    
if __name__ == '__main__':
    lake = Image(filename ='lake.png')
    city = Image(filename ='city.png')

    #brightening the lake image!
    #brightened_im = adjust_brighteness(lake,1.7)
    #brightened_im.write_image('brightened.png')

    #darkening the image !
    #darkened_im=adjust_brighteness(lake,0.4)
    #darkened_im.write_image('darkened.png')
    
    #increase contrast
    incr_contrast = adjust_contrast(lake, 2, mid=0.5)
    incr_contrast.write_image('increased_contrast.png')

    #decrease contrast
    decr_contrast = adjust_contrast(lake, 0.5, mid=0.5)
    decr_contrast.write_image('decreased_contrast.png')
