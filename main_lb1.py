import argparse
import re


def parse() -> argparse.Namespace:
    """
    расширим возможности программы))
    создаём парсер с обязательным аргументов виде пути к файлу
    и с необязательным аргументом в виде кода телефона
    при этом если нам ввели неверный код (т.е не 3 цифры написанные слитно)
    программа кинет ошибку
    """
    parser = argparse.ArgumentParser(description="path and telephon number code")  # создание экземпляра парсера
    
    parser.add_argument("-c", "--code", type=str, default= "927",
                        help="телефонный код, первые 3 цифры после 8") # добавляем необязательный аргумент
    parser.add_argument("path", type=str, help = "путь до файла с анкетами") # добавляем обязательный аргумент пути
    
    args = parser.parse_args()
    if (args.code.isdigit()) and (len(args.code) == 3): # проверка что строка состроит из 3-х цифр
        return args
    else: 
        raise ValueError("Incorect code numder") # если код неверен отправляем исключение


def file_read(path: str) ->list[str]:
    """
    функция чтения файла, вернёт массив всех строчек
    """
    with open(path, "r", encoding="Utf8") as file: # открываем файл
            text = file.readlines() # разбиваем весь файл по строчкам
    
    return text


def search_anks(text: list[str], pattern: str) -> list[str]:
    """
    ищет анкеты по указаному паттерну. Если в строчке найден паттерн
    добавляет в результирующий массив анкету, путём склеивания строк
    """
    rez = [];
    for i in range (len(text)): # цикл прохода по всем строчкам файла
        if re.search(pattern, text[i]):                # если в i-й строчке нашли нужный паттерн то
            rez.append("".join(text[i-5 : i+2]))  #  добавляем в результат анкету, склеивая строки от i-5 до i+2  
  
    return rez;


def main():
    try:
        parser = parse()  # парсинг кода телефона

        text = file_read(parser.path)
        if len(text) == 0:
            print("файл пуст\n")
            return
        
        pattern = r"\s" + parser.code + r"\s" # нужен паттер вида: "пробел телефонный_код пробел"
        
        anks = search_anks(text, pattern)

        if len(anks) == 0:  print(f"Анкеты с кодом \"{parser.code}\" не найдены") #если массив анкет пуст то ничего не найдено
        else:
            for ank in anks: print(ank) #иначе выводим найденные анкеты

    except Exception as exc: # если в программе произошла ошибка выводим сообщение
        print(f"Error!\n {exc}")


if __name__ == "__main__":
    main()