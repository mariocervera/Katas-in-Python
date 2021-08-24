import re

def add(numbers_string):
    if not numbers_string:
        return '0'
    
    numbers = re.split(',|\n', numbers_string)
    error_message = __get_error_message_if_invalid(numbers)

    return __add_numbers(numbers) if error_message is None else error_message


def __get_error_message_if_invalid(numbers):
    negative_numbers = []
    
    for num in numbers:
        if not num:
            return 'Number expected but EOF found.'
        elif __is_negative(num):
            negative_numbers.append(num)

    return None if len(negative_numbers) == 0 else f'Negative not allowed : {negative_numbers}'


def __add_numbers(numbers):
    result = 0
    
    for num in numbers:
        result += __cast_to_number(num)
        
    return str(result)


def __cast_to_number(number_str):
    try:
        return int(number_str)
    except ValueError:
        return float(number_str)


def __is_negative(number):
    return __cast_to_number(number) < 0