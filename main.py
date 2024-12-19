import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

from iter import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Вызов инициализатора QMainWindow
        self.setWindowTitle("Просмотр датасета")

        self.image_label = QLabel(self) #для текста и фото
        self.image_label.setFixedSize(800, 600)

        self.next_button = QPushButton("Следующее изображение", self)
        self.next_button.clicked.connect(self.show_next_image) 

        self.open_button = QPushButton("Выбрать папку датасета", self)
        self.open_button.clicked.connect(self.open_dataset_folder)

        # Создаем вертикальный макет и добавляем в него кнопки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.open_button)

        # Создаем виджет-контейнер и устанавливаем для него макет
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.iterator = None

    def open_dataset_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с датасетом")
        if folder_path:
            self.iterator = ImageIterator(folder_path)
            if self.iterator.image_cnt == 0:
                self.image_label.setText("Изображения отстутвуют")
                return None

            self.show_next_image()
    
    def show_next_image(self) -> None:
        if not(self.iterator):
                self.image_label.setText("Папка не выбрана")
        elif self.iterator.image_cnt > 0:
            try:
                image_path = next(self.iterator)
                pixmap = QPixmap(image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1)) #aspectRatioMode - сохраняет пропорции
            except StopIteration:
                self.image_label.setText("Больше изображений нет")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_()) # Закрытие окна после нажатия на крестик

    except Exception as error:
        print(f"Произошла ошибка: {error}")


if __name__ == "__main__":
    main()