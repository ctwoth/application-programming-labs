import matplotlib.pyplot as plt
import numpy as np


def get_pixels_count(img: np.ndarray, is_grayscale: bool) -> tuple:
    """
    получаем массив размером 256, где каждый элемент - яркость, а значение
    этемента - кол-во пикселей с такой яркостью
    """
    hist_info = [0 for x in range(256)]

    if is_grayscale:
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                hist_info[img[y,x]] += 1
    
    else:
        for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    lum = int(img[y, x][0]*0.299 + img[y, x][1]*0.587 + img[y, x][2]*0.114)

                    hist_info[lum] += 1

    return hist_info


def hist_display(img: np.ndarray, is_grayscale: bool) -> None:
    """
    создание гистограммы фото
    """

    try:
        x = [x for x in range(256)]
        y = get_pixels_count(img, is_grayscale)

        plt.plot(x, y, label='Histogram', color='blue')
        plt.title('Гистограмма фото')  # заголовок графика
        plt.xlabel('яркость пикселя')  # подпись оси x
        plt.ylabel('кол-во пикселей')  # подпись оси y
        plt.axhline(0, color='black',linewidth=0.5, ls='--')  # линия по оси x
        plt.axvline(0, color='black',linewidth=0.5, ls='--')  # линия по оси y
        #plt.legend()  # легенда
        
        plt.show()
    
    except Exception as ex:
        raise Exception("histogram is not created: ", ex)
