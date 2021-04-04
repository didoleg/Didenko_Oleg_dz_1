duration = int(input('Введите число в секундах: '))

if duration < 60:
    print(f'{duration} сек')

elif 60 <= duration < 3600:
    print(f'{duration // 60} мин {duration % 60} сек')

elif 3600 <= duration < 86400:
    print(f'{duration // 3600} час {(duration % 3600) // 60} мин {(duration % 3600) % 60} сек')

else:
    print(f'{duration // 86400} дн  {(duration % 86400) // 3600} час {((duration % 86400) % 3600) // 60} мин {((duration % 86400) % 3600) % 60} сек')