def power(num, index):
    if index == 0:
        return 1
    if index < 0:
        num = 1 / num
        index = -index
    if index % 2 == 0:
        half_power = power(num, index // 2)
        return half_power * half_power
    else:
        return num * power(num, index - 1)


n = 2
i = 10
result = power(n, i)
print(result)
