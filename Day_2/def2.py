even_numbers_only = []
def even_list(numbers):
    for number in numbers:
        if number % 2 == 0:
            even_numbers_only.append(number)

first = [23, 45, 67, 34, 89]
second = [8, 17, 26, 29, 37]
even_list(first)

even_list(second)

print(even_numbers_only)   