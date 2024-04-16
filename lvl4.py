#Дано целое число n. Найти сумму 1 + 2 + 4 + 8 + 16 + ... + 2**n
#где 2**n - это 2*2*2*...*2 раз. Таким образом, 2**4 = 2*2*2*2. Операция ** называется операцией возведения в степень.
number = int(input())
result = 1
summa = 1

for i in range(1, number+1):
 result = result * 2
 summa += result
 print (result, ' ', summa)
endSummma = summa + 2**number
print(endSummma)

n = int(input())
summa = 0

for i in range(1, n+1):
 result = 1/i
 summa += result
 print('1 /', i, '=', result)
print (summa)

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