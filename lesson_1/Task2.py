# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600
time_seс = int(input("Введите время в секундах:"))
hour = time_seс // 3600
minute = (time_seс - hour * 3600) // 60
second = time_seс - (hour * 3600 + minute * 60)
print(f"Время в формате ч:м:с {hour}:{minute}:{second}")
