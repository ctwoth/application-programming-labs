import csv


class ImageIterator:
    def __init__(self, csv_path: str) -> None:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            reader.__next__() # пропускаем заголовки
            self.path_list = [row[1] for row in reader] # берём абсолютный путь row[1]

        self.limit = len(self.path_list)  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return self.path_list[self.counter - 1]
        else:
            raise StopIteration

