import argparse
import os


def validate_args(args: argparse.Namespace) -> None:
    if (args.max_height < 0): 
        raise ValueError("height filter less 0")
    if (args.max_width < 0): 
        raise ValueError("width filter less 0")
    if not(os.path.isfile(args.csv_path)): 
        raise ValueError("incorrect anotation path")


def parse() -> argparse.Namespace:
    """
    Парсим путь к csv файлу, необязательно оставляем возможность
    менять аргументы для фильтра изображений
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument("-mh", "--max_height", type=int, default= 600, help="max height for filter")
    parser.add_argument("-mw", "--max_width", type=int, default= 600, help="max width for filter")
    parser.add_argument('csv_path', type=str, help='path to the csv file')
    args = parser.parse_args()
    
    validate_args(args)

    return args
