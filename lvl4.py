print('Введите число А')
a = int(input())
print('Введите число Б')
b = int(input())

if a < b: 
    sum = 0
    for i in range(a, b+1, 1):
     if i % 3 == 0:
      sum += i     
    print ('Сумма всех целых чисел в диапазоне от ', a, ' до ', b, ' = ', sum)
else:
 print ('Число А ,больше числа Б, повторите попытку ввода: ')