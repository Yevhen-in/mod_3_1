import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    clean_number = re.sub(r'[^0-9\+]', '', phone_number)
    clean_number = '+' + clean_number if clean_number.startswith('380') else clean_number
    clean_number = '+38' + clean_number if clean_number.startswith('0') else clean_number
    return clean_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)