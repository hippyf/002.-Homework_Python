#На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной.

n = int(input('Введите количесиво монет '))
resh = 0
gerb = 0
for i in range(n):
    v = int(input('Введите 1 или 2 (1 - монета лежит вверх решкой, 0 - ввех гербом) '))
    if v == 1:
        resh += 1
    elif v == 0:
        gerb += 1
if resh > gerb: print(gerb)
else: print(resh)

