n = int(input("Введите количество элементов: "))
num = [1, (-0.5), 0.25, (-0.125)]
sum_l = []
for i in num[:n]:
    sum_l.append(i)
print(sum(sum_l))
