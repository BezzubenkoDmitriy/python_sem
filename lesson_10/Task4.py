
strs = ['разработка', 'администрирование', 'protocol']

for s in strs:

    encoded_s = s.encode('utf-8')
    print(f'Байтовое: {encoded_s}')
    decoded_s = encoded_s.decode('utf-8')
    print(f'Преобрзованное байтовое: {decoded_s}')
