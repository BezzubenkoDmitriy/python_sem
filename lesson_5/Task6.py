import random
n = random.randint(0, 100)
print('Попробуйте угадать загаданное число от 0 до 100. У вас есть 10 попыток')
for i in range(10):
    a = int(input(f'Попытка №{i + 1}. Введите число: '))
    if a < n and i < 9:
        print('Загаданное число больше')
    elif a > n and i < 9:
        print('Загаданное число меньше')
    elif a == n:
        print('Вы угадали!')
        break
    else:
        print('Вы не угадали')

print(f'Загаданное число - {n}')
