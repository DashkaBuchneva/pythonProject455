#задача
#напиши тестовые сценарии для данной функции и протестируйте ее


def is_even(number: int) -> bool:
    return number % 2 == 0

#чётные числа: 2, 4, 6, 8, 10, 12...
print(is_even(4))
#нечётные числа: 1, 3, 5, 7, 9, 11...
print(is_even(3))

#test case 1: -> passed
# expected result: is_even(16)) - True
# actual result: is_even(16)) - True
print(is_even(16))

#test case 2: -> passed
# expected result: is_even(1)) - False
# actual result: is_even(1)) - False
print(is_even(1))

