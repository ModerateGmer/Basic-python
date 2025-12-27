def find_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

my_list = [1, 2, 3, 4, 5, 6]
print(find_even_numbers(my_list))