n = int(input("Введите число: "))
rev_n = 0
while (n > 0):
    dig = n % 10
    rev_n = rev_n*10+dig
    n = n//10
print("Обратное число:", rev_n)
