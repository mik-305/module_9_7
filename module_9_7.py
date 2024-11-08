def is_prime(func):
    def wrapper(s1, s2, s3):
        sum = s1 + s2 + s3
        def IsPrime(sum):               # Определяем - простое или нет
            j = 2
            while sum % j != 0:
                j += 1
            return j == sum

        if IsPrime(sum):
            print('Простое')
        else:
            print('Не является простым')
        return sum
    return wrapper

@is_prime
def sum_three():
    pass
    return

result = sum_three(2, 3, 6)
print(result)
result = sum_three(1, 5, 6)
print(result)
