#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

N = int(input("Введите целое число N "))
flag = True
i = 1
while flag:
    i += 1
    if N % i == 0:
        flag = False
print (i)

