import random

min = 0
max = 0
quantity = 0

def get_numbers_ticket(min, max, quantity):
    try:
        min = int(input("Enter the minimum number: "))
        max = int(input("Enter the maximum number: "))
        quantity = int(input("Enter quantity of numbers to choose: "))
    except ValueError:
        print("It`s not a number")

    rand_numbers = set()
    if 1 <= min < max <= 1000 and quantity <= max - min + 1:
        while len(rand_numbers) < quantity:
            rand_numb = random.randint(min, max)
            rand_numbers.add(rand_numb)
    rand_numbers = list(rand_numbers)
    rand_numbers.sort()
    return rand_numbers

print(get_numbers_ticket(min, max, quantity))




    