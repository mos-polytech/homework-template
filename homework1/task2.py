print('Введите число: ')
f = float(input())
print('Введите число: ')
s = float(input())
print('Введите "+" или "-": ')
symbol = input()

if symbol == '+':
    print('Сумма', f + s)
elif symbol == '-':
    print('Разницу', f - s)
else:
    print('Ошибка!')
