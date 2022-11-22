def binary_number(number):
    remainder = number % 2
    divide = int(number / 2)
    if divide == 0:
        return str(remainder)
    else:
        return str(remainder) + str(binary_number(divide))


def consecutive_one(string):
    maximum = 0
    counter = 0
    for x in range(len(string)):
        if string[x] == "1":
            counter += 1
            if counter > maximum:
                maximum = counter
        else:
            counter = 0
    return maximum


result = binary_number(5)
print(consecutive_one(result))