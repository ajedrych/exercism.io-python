from typing import Counter


def square_of_sum(number):
    counter_square_of_sum = 0
    for i in range(1, number + 1 ):
        counter_square_of_sum += i
    return counter_square_of_sum ** 2


def sum_of_squares(number):
    counter_sum_of_squares = 0
    for i in range(number + 1):
        counter_sum_of_squares += i ** 2
    return counter_sum_of_squares


def difference_of_squares(number):
    counter_square_of_sum = 0
    counter_sum_of_squares = 0
    for i in range(number + 1):
        counter_square_of_sum += i
        counter_sum_of_squares += i ** 2
    return (counter_square_of_sum ** 2) - counter_sum_of_squares
    
