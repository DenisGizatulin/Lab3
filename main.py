from domains_checker import (
    is_valid_domain,
    check_domains_in_file,
    find_domains_in_text,
    find_domains_in_url,
    check_domains_in_url,
)
from domains_checker_TEST import *


def user_menu():
    print("Выберите действие:")
    print("1. Проверить доменное имя")
    print("2. Найти домены в тексте")
    print("3. Проверить домены на корректность в файле")
    print("4. Найти домены на странице по URL")
    print("5. Проверить домены на корректность на странице по URL")
    print("0. Выйти")

    while True:
        choice = input("Введите номер действия: ")
        if choice == "1":
            user_input = input("Введите доменное имя: ")
            if is_valid_domain(user_input):
                print(f"{user_input} корректно.")
            else:
                print(f"{user_input} некорректно.")
        elif choice == "2":
            filename = input("Введите имя файла: ")
            try:
                domains = find_domains_in_text(filename)
                print("Найденные омены:", domains)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == "3":
            filename = input("Введите имя файла: ")
            try:
                valid_domains = check_domains_in_file(filename)
                print("Корректные домены:", valid_domains)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == "4":
            url = input("Введите URL: ")
            domains = find_domains_in_url(url)
            print("Найденные домены:", domains)
        elif choice == "5":
            url = input("Введите URL: ")
            domains = check_domains_in_url(url)
            print("Корректные домены:", domains)
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    user_menu()
    unittest.main()  # unit-тесты запускаются после того как пользовательзаканчивает работу с меню т.е. выбирает в меню "4. Выйти"
