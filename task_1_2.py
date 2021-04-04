number_list = []

for number in range(1, 1000):
    if number % 2 != 0:
        number_list.append(number ** 3)

new_number_list_a = [] #Список для записи конечного результата выполнения пункта a
new_number_list_b = [] #Список для записи конечного результата выполнения пунктов b и c

for number in number_list:
    sum_number = 0
    for element in str(number):
        sum_number += int(element)
    if sum_number % 7 == 0:
        new_number_list_a.append(number)

for number in number_list:
    new_number = number + 17
    sum_number = 0
    for element in str(new_number):
        sum_number += int(element)
    if sum_number % 7 == 0:
        new_number_list_b.append(number)

print(number_list)
print(new_number_list_a)
print(new_number_list_b)
