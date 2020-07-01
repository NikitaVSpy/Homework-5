import divisor_master

number = int(input('Введите натуральное число от 1 до 1000: '))

while number < 1:
    print('Вы ввели число меньше 1')
    number = int(input('Введите натуральное число от 1 до 1000: '))
while number > 1000:
    print('Вы ввели число больше 1000')
    number = int(input('Введите натуральное число от 1 до 1000: '))

print('Проверка числа на простоту:', divisor_master.simple(number))

print('Список делителей числа:', divisor_master.divisor(number))

print('Список простых делителей числа:', divisor_master.simple_divisor(number))

print('Самый большой простой делитель числа (исключая само число):', divisor_master.max_simple_div(number))

print('Каноническое разложение числа:', divisor_master.canonical_decomposition(number))

print('Самый большой делитель числа (исключая само число):', divisor_master.max_div(number))




