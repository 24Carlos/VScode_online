### LAMBDAS ###


sum_2_values = lambda first_value, second_value: first_value + second_value

print(sum_2_values(1, 2))


multiply_values = lambda first_value, second_value: first_value *  second_value - 3
print(multiply_values(2, 4))



def sum_three_values(value):
    return lambda firs_value, second_value: firs_value + second_value + value

print(sum_three_values(5)(2, 4))


