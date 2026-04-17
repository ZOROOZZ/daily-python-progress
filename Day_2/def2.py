def even_list(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even
            
first = [23, 45, 67, 34, 89]
second = [8, 17, 26, 29, 37]

batch_first = even_list(first)
batch_second = even_list(second)

print(batch_first)
print(batch_second)