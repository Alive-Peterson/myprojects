
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
    
    neighbour_range=kernel_size // 2 #how many neighbours to one side we need to look at

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                #using naive implementation of searching through elements and summing up
                total=0
                for x_i in range(max(0, x-neighbour_range), min(x_pixels -1, x + neighbour_range) + 1):
                    for y_i in range(max(0, y-neighbour_range), min(y_pixels -1, y + neighbour_range) + 1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size**2)
    return new_im          


#note: this blur implemented above is a kernel of size n, where each value is l/n^2
#for eaxmple k=3, kernel would be
#[1/3  1/3  1/3]
#[1/3  1/3  1/3]
#[1/3  1/3  1/3]

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)
    
    kernel_size = kernel.shape[0]
    neighbour_range=kernel_size // 2 #how many neighbours to one side we need to look at

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total=0
                for x_i in range(max(0, x-neighbour_range), min(x_pixels -1, x + neighbour_range) + 1):
                    for y_i in range(max(0, y-neighbour_range), min(y_pixels -1, y + neighbour_range) + 1):
                        #we need to find which of the value this kernel corresponds to
                        x_k = x_i + neighbour_range - x
                        y_k = y_i + neighbour_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x,y,c] = total
    return new_im

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
    #incr_contrast = adjust_contrast(lake, 2, mid=0.5)
    #incr_contrast.write_image('increased_contrast.png')

    #decrease contrast
    #decr_contrast = adjust_contrast(lake, 0.5, mid=0.5)
    #decr_contrast.write_image('decreased_contrast.png')

    #blur with kernel 3
    #blur_3 = blur(city,3)
    #blur_3.write_image('blur_k3.png')
    
    #blur with kernel 15
    #blur_15 = blur(city,15)
    #blur_15.write_image('blur_k15.png')

    #sobel edge detection kernel
    sobel_x_kernel = np.array(
        [[1, 2, 1],
         [0, 0, 0],
         [-1, -2, -1]]
    )

    sobel_y_kernel = np.array(
        [[1,0,-1],
         [2,0,-2],
         [1,0,-1]]
    )

    sobel_x = apply_kernel(city,sobel_x_kernel)
    sobel_x.write_image('edge_x.png')

    sobel_y = apply_kernel(city,sobel_y_kernel)
    sobel_y.write_image('edge_y.png')