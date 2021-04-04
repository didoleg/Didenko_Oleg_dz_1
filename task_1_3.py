number = int(input('Введите число от 1 до 20: '))

if 4 < number <= 20:
    print(f'{number} процентов')

elif 1 < number < 5:
    print(f'{number} процента')

else:
    print(f'{number} процент')
