import os

import parser
import cv
import pyplot


def main():
    pars = parser.parse()
    img = cv.image_read(pars.im_path, pars.gray) # считываем фото
    print("Ширина: ", img.shape[1], "\nВысота: ", img.shape[0])

    cv.show(os.path.basename(pars.im_path), img) # показываем фото

    pyplot.hist_display(img, pars.gray) # гисторгамма

    cv.reverse_colors(img, pars.gray) # фото в негатив
    cv.show('reversed_' + os.path.basename(pars.im_path), img)

    cv.save_image(pars.s_path, os.path.basename(pars.im_path), img, pars.gray) # сохранение негатива


if __name__ == '__main__': 
    main()