import cv2
import pandas as pd
import matplotlib.pyplot as plt


def get_shape(path: str) -> tuple:
    '''
    Функция для получения размеров и глубины изображения
    '''
    image = cv2.imread(path)
    height, width, depth = image.shape
    if len(image.shape) == 2:
        depth = 1

    return height, width, depth


def add_columns(df: pd.DataFrame) -> None:
    '''
    Добавление столбцов с размерами изображения
    '''
    heights, widths, depths = [], [], []
    
    for path in df['Absolute path']:
        height, width, depth = get_shape(path)
        heights.append(height)
        widths.append(width)
        depths.append(depth)

    df['height'] = heights
    df['width'] = widths
    df['depth'] = depths


def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    '''
    оставляем картинки подходящие по длине и ширине
    '''
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]


def create_histogram(df: pd.DataFrame) -> None:
    """
    Функция создания гистограммы распределения площадей изображений
    """
    plt.hist(df['area'], label="Histogram", edgecolor='blue',bins=50)
    plt.title('Распределение площадей')
    plt.xlabel('Площадь')
    plt.ylabel('Количество изображений')
    plt.show()
