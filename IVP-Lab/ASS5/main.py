import cv2 as cv
import numpy as np


def compress_image(img, quality):
    h,w = img.shape
    new_h = h + (8 - h % 8) if h % 8 != 0 else h
    new_w = w + (8 - w % 8) if w % 8 != 0 else w
    resized_img = cv.resize(img, (new_w, new_h))

    dct_img = cv.dct(np.float32(resized_img))
    quality = max(1, min(quality, 100))
    threshold = (101 - quality) / 100

    mask = np.zeros_like(dct_img)
    mask[:int(new_h * threshold), :int(new_w * threshold)] = 1

    compressed_dct = dct_img * mask
    compressed_img = cv.idct(compressed_dct)
    compressed_img = np.clip(compressed_img, 0, 255).astype(np.uint8)
    return compressed_img


image = cv.imread('./cameraman.png', cv.IMREAD_GRAYSCALE)
c = compress_image(image, quality=50)
cv.imshow('original image', image)
cv.imshow('compressed Image', c)
cv.imwrite('compressed_cameraman.jpg',c)
cv.waitKey(0)