count = int(input('Введите число: '))

while int(count ** 0.5) != count ** 0.5:
  count = int(input('Число не является полным квадратом. Введите другое число:'))
print(f'Число {count} является полным квадратом')