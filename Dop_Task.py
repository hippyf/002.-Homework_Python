# Клубника растет на круглой грядке, причем кусты высажены только по окружности 
# У каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
#  собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input('Введите количесиво кустов от 3 до 1000 '))
count_berries = []
for i in range(N):
    count_berries.append(int(input(f'Введите количество ягод на кусте №{i+ 1} ')))

if count_berries[0] + count_berries[1] + count_berries[-1] > count_berries[0] + count_berries[-1] + count_berries[-2]:
    max = count_berries[0] + count_berries[1] + count_berries[-1]
else: max = count_berries[0] + count_berries[-1] + count_berries[-2]

for i in range(N-2):
     new_max = count_berries[i] + count_berries[i+1] + count_berries[i+2]
     if new_max > max:
        new_max = max
        max = count_berries[i] + count_berries[i+1] + count_berries[i+2]
print(f'Максимальное число ягод, которое может собрать собирающий модуль равно {max}')

