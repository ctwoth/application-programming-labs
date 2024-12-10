import argparse
import os


def validate_args(args: argparse.Namespace) -> None:
    if not(os.path.isfile(args.im_path)): 
        raise ValueError("incorrect path to image or image not exists")
    if not(os.path.isdir(args.s_path)): 
        raise ValueError("incorrect safe direcroty path")


def parse() -> argparse.Namespace:
    """
    создаём парсер с обязательными аргументами в виде пути к фото и для сохранения фото
    также добавим необязательный аргумент в виде grayscale представления
    программа кинет ошибку если не существует указанного файла, или папик для сохранения
    """
    parser = argparse.ArgumentParser(description="path to image and path to convert result")

    parser.add_argument("im_path", type=str, help = "path fo image") # обязательный аргумент пути до фото
    parser.add_argument("s_path", type=str, help = "convert image path") # обязательный аргумент пути сохранения
    parser.add_argument("-g", "--gray", type=bool, default=False, help = "image in grayscale") # необязательный аргумент представления в виде grayscale

    args = parser.parse_args()

    validate_args(args)

    return args