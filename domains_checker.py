import re
import requests


VALID_DOMAIN_REGEX = r"^(?!-)([a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,}$"  # Регулярное выражение для поиска доменов в тексте
FIND_DOMAIN_REGEX = r"(?<!-)\"?([a-zA-Z0-9-]{1,63}\.[a-zA-Z]{2,})\"?"  # Регулярное выражение для поиска корректных доменов в тексте


def is_valid_domain(domain):
    return re.match(VALID_DOMAIN_REGEX, domain) is not None


def check_domains_in_file(file_path):
    # Открываем файл и читаем его содержимое
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Находим все возможные совпадения по регулярному выражению
    raw_domains = re.findall(FIND_DOMAIN_REGEX, text)

    # Фильтруем и оставляем только корректные доменные имена
    valid_domains = [
        domain for domain in raw_domains if is_valid_domain(domain)
    ]

    return valid_domains


def find_domains_in_text(file_path):

    # Открываем файл и читаем его содержимое
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Находим все совпадения по регулярному выражению
    domains = re.findall(FIND_DOMAIN_REGEX, text)

    return domains


def find_domains_in_url(url):
    try:
        # Получаем содержимое веб-страницы
        response = requests.get(url).text

        # Находим все возможные совпадения по регулярному выражению
        raw_domains = re.findall(FIND_DOMAIN_REGEX, response)

        # Убираем дубликаты и возвращаем уникальные домены
        unique_domains = list(set(raw_domains))
        return unique_domains

    except requests.RequestException as e:
        print(f"Ошибка при доступе к URL: {e}")
        return []


def check_domains_in_url(url):
    try:
        # Получаем содержимое веб-страницы
        response = requests.get(url).text

        # Находим все возможные совпадения по регулярному выражению
        raw_domains = re.findall(FIND_DOMAIN_REGEX, response)

        # Фильтруем и оставляем только корректные доменные имена
        valid_domains = [
            domain for domain in raw_domains if is_valid_domain(domain)
        ]

        return valid_domains

    except requests.RequestException as e:
        print(f"Ошибка при доступе к URL: {e}")
        return []
