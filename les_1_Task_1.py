#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


a = int(input('Введите целове трехзначное число:'))

hundred = a // 100
dozen = (a // 10) % 10
unit = a % 10

summa = hundred + dozen + unit
mult = hundred * dozen * unit

print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифл в числе: {mult}')