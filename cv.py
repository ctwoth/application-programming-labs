import os

import cv2
import numpy as np


def image_read(path: str, is_grayscale: bool):
    """
    считывем фото с учётом параметра grayscale
    """
    if is_grayscale: 
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return cv2.imread(path, cv2.IMREAD_ANYCOLOR)


def reverse_colors(img: np.ndarray, is_grayscale: bool) -> None:
    """
    меняет цвет каждого пикселя по всем его каналам на
    противоположное значение по формуле цвет_в_канале = 255 - цвет_в_канале
    """
    if is_grayscale:
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                img[y, x] = 255 - img[y, x]
    else:
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                img[y, x][0] = 255 - img[y, x][0]
                img[y, x][1] = 255 - img[y, x][1]
                img[y, x][2] = 255 - img[y, x][2]


def save_image(directory: str, im_name: str, img: np.ndarray, is_grayscale: bool) -> None:
    """
    сохраняем фото:
    сначала меняем директорию на необходимую
    сохраняем файл с фото и меняем директорию обратно
    """
    cur = os.getcwd()
    os.chdir(directory)

    name = 'reversed_' + im_name 
    if is_grayscale: 
        name = 'gray_' + name

    cv2.imwrite(name, img)
    os.chdir(cur)


def show(im_name: str, img: np.ndarray) -> None:
    """
    показываем фото
    """
    cv2.imshow(im_name, img)
    cv2.waitKey(0)