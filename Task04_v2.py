number_of_pupls = int(input('Введите количество учеников от 1 до 100 '))
petya_height = int(input('Введите рост Пети '))
number_in_line = 1
for i in range(number_of_pupls):
    height = int(input(f'Введите рост ученика №{i+1} в см '))
    if height >= petya_height: number_in_line += 1
print(f"Номер Пети в шеренге учеников - {number_in_line}")

