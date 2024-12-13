import re


VALID_DOMAIN_REGEX = r'^(?!-)([a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,}$' # Регулярное выражение для поиска доменов в тексте

def is_valid_domain(domain):
    return re.match(VALID_DOMAIN_REGEX, domain) is not None


