import argparse
import os as os


def validate_args(args: argparse.Namespace) -> None:
    if (args.count < 50 or args.count > 1000): 
        raise ValueError("count bigger 1000 or less 50")
    if not(os.path.isdir(args.s_path)): 
        raise ValueError("incorrect directory path")
    if not(os.path.isfile(args.a_path)): 
        raise ValueError("incorrect anotation path")


def parse() -> argparse.Namespace:
    """
    создаём парсер с обязательными аргументами в виде пути к папке для сохранения фото
    и с путём до .csv файла-аннотации дополнительно имеется два аргумента: count и word,
    где count - кол-во скаченных фото, word - слово для поиска фото
    программа кинет ошибку если не существует указанной папки, или .csv файла
    """
    parser = argparse.ArgumentParser(description="path to save directory and download word")

    parser.add_argument("-c", "--count", type=int, default= 50, help="number of images") # необязательный аргумент кол-ва изображений
    parser.add_argument("-w", "--word", type=str, default= "Horse", help="word for GoogleImageCrawler") # необязательный аргумент слова
    parser.add_argument("s_path", type=str, help = "save path fo images") # обязательный аргумент пути для скачивания
    parser.add_argument("a_path", type=str, help = "images anotation path") # обязательный аргумент пути для анотации
    
    args = parser.parse_args()
    
    validate_args(args)

    return args