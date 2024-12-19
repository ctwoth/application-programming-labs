import os


class ImageIterator:
    def __init__(self, im_folder: str) -> None:
        self.path_list = []
        
        print(im_folder)
        for file in os.listdir(im_folder):
            if file.endswith(('jpg', 'jpeg', 'png')):
                self.path_list.append(im_folder + '/' + file)

        self.image_cnt = len(self.path_list)  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.image_cnt:
            self.counter += 1
            return self.path_list[self.counter - 1]
        else:
            raise StopIteration