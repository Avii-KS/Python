def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        half_power = power(x, n // 2)
        return half_power * half_power
    else:
        return x * power(x, n - 1)

x = float(input())
n = int(input())

result = power(x, n)
print(result)