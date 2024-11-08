def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        def IsPrime(resul):               # Определяем - простое или нет
            j = 2
            while resul % j != 0:
                j += 1
            return j == resul

        if IsPrime(result):
            print('Простое')
        else:
            print('Не является простым')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

result = sum_three(2, 3, 6)
print(result)
result = sum_three(1, 5, 6)
print(result)
