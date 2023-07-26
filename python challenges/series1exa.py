import math

def largest_product(string_of_digits, series_length):

    if series_length > len(string_of_digits) or series_length < 0:
        raise ValueError

    biggest_product = 1 if string_of_digits == "" else 0
    try:
        list_of_digits = [int(x) for x in string_of_digits]
    except:
        raise ValueError

    for index, digit in enumerate(list_of_digits[0:-(series_length - 1)]):
        slice = list_of_digits[index:index + series_length]
        product = math.prod(slice)
        biggest_product = product if product > biggest_product else biggest_product

    return biggest_product