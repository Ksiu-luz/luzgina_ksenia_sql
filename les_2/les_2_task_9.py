# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_sum = 0
result = 0
x = int(input('Введите первое натуральное число последовательности. Для остановки последовательности введите 0: '))

while x != 0:
    tmp_x = x
    tmp_sum = 0
    while tmp_x > 0:
        tmp_sum += tmp_x % 10
        tmp_x = tmp_x // 10
    if tmp_sum > max_sum:
        max_sum = tmp_sum
        result = x
    x = int(input())

print(f'Число с наибольшей суммой его цифрр: {result}, сумма цифр: {max_sum}')
