def fibonacci(num):
    if (num <= 1):
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

print(f'5 : {fibonacci(5)}')
print(f'7 : {fibonacci(7)}')
print(f'10 : {fibonacci(10)}')

print(f'4 : {fibonacci(4)}')
