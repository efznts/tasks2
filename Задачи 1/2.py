a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


def is_prime(n):
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


sum = 0
for n in range(a, b + 1):
    if is_prime(n):
        sum += n
print(sum)
