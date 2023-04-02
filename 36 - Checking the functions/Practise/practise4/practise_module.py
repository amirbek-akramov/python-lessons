def have_fibinacci(n, max_fibonacci):
    numbers = []

    for x in range(max_fibonacci):
        if x == 0 or x == 1:
            numbers.append(1)
        else:
            numbers.append(numbers[x-1] + numbers[x-2])

    if n in numbers:
        return True
    else:
        return False
