import os as os
import csv

import crawler
import iterator
import parser


def create_annotation(an_path: str, im_path: str) -> None:
    """
    создаём csv файл анотации, нам нужен путь к файлу
    и путь к директории с картинками
    """
    try: 
        with open(an_path, mode='w+', encoding='utf-8', newline='') as annotation_file:
            writer = csv.writer(annotation_file, delimiter= '\t')
            writer.writerow(['Relative path', 'Absolute path'])
            for file in os.listdir(im_path):
                relative_path = os.path.relpath(file, start=im_path)
                absolute_path = os.path.abspath(file)
                writer.writerow([relative_path[2:], absolute_path])

    except PermissionError as error:
        raise PermissionError("Permissiom error with csv file:\n", error)


def main():
    try:
        pars = parser.parse()

        crawler.download_images(pars.s_path, pars.word, pars.count)

        create_annotation(pars.a_path, pars.s_path)

        iter = iterator.ImageIterator(pars.a_path)

        for item in iter: # выводим строчки файла анотиции
            print(item)

    except Exception as exc:
        print("Error!\n", exc)


if __name__ == '__main__': 
    main()