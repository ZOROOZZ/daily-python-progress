def even_number_list(numberlist):
    for number in numberlist:
        if number % 2 == 0:
            print(f"{number} is an Even Number")
        else:
            print(f"{number} is an Odd Number")

first_batch = [12, 35, 43, 56, 23]
second_batch = [13, 36, 44, 57, 24]

print("Checking First Batch: ")
even_number_list(first_batch)

print("Checking Second Batch: ")
even_number_list(second_batch)