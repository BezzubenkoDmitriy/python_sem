def print_task(strs_data):
    for s in strs_data:
        print(f'Тип:{type(s)} Значение:{s}')


strs = ['разработка', 'cокет', 'декоратор']
print_task(strs)

strs_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430']
print_task(strs_unicode)
