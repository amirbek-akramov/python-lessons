def sort_the_numbers(min, max, evenNumber = True):
    numbers = list(range(min,max))
    even_numbers_list = []
    odd_numbers_list = []

    if evenNumber:
        for number in numbers:
            if number%2 == 0:
                even_numbers_list.append(number)
            
        # return f"Even number(s) between {min} and {max}: {even_numbers_list}"
        return even_numbers_list

    else:
        for number in numbers:
            if number%2 != 0:
                odd_numbers_list.append(number)
        
        # return f"Odd numbers between {min} and {max}: {odd_numbers_list}"
        return odd_numbers_list



print(sort_the_numbers(0, 11))