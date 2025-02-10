import os
import shutil
import func


def main():
    print("Добро пожаловать в файловый менеджер! Введите 'help' для получения списка команд.")
    while True:
        command = input(f"{os.getcwd()}> ").strip().split()

        if not command:
            continue

        cmd = command[0]

        if cmd == 'help':
            func.print_help()


if __name__ == "__main__":
    main()
