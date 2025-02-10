import os
import shutil


def print_help():
    help_text = """
    Доступные команды:
    - ls                : Показать содержимое текущего каталога.
    - cd <path>        : Перейти в указанный каталог.
    - cp <src> <dst>   : Скопировать файл или каталог.
    - mv <src> <dst>   : Переместить файл или каталог.
    - rm <path>        : Удалить файл или каталог.
    - help             : Показать это сообщение.
    - exit             : Выйти из программы.
    """
    print(help_text)


def list_directory():
    print("Содержимое текущего каталога:")
    for item in os.listdir():
        print(f" - {item}")
