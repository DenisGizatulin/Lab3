from domains_checker import is_valid_domain, check_domains_in_file, find_domains_in_text
from domains_checker_TEST import *

def user_menu():
    print("Выберите действие:")
    print("1. Проверить доменное имя")
    print("2. Проверить домены в файле")
    print("3. Найти домены в тексте")
    print("4. Выйти")

    while True:
        choice = input("Введите номер действия: ")
        if choice == '1':
            user_input = input("Введите доменное имя: ")
            if is_valid_domain(user_input):
                print(f"{user_input} корректно.")
            else:
                print(f"{user_input} некорректно.")
        elif choice == '2':
            filename = input("Введите имя файла: ")
            try:
                valid_domains = check_domains_in_file(filename)
                print("Корректные домены:", valid_domains)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '3':
            filename = input("Введите имя файла: ")
            try:
                valid_domains = find_domains_in_text(filename)
                print("Корректные домены:", valid_domains)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '4':
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    user_menu()
    unittest.main() # unit-тесты запускаются после того как пользовательзаканчивает работу с меню т.е. выбирает в меню "4. Выйти"

