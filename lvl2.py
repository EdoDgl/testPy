firstCount = input ( "Введите число: ")

firstCountLength = len(firstCount)
#Длина числа
a = int(firstCountLength)
#Первый символ
b = int(firstCount[0])
#Последний символ
c = int(firstCount[firstCountLength - 1])

secondCount = input ( "Введите число: ") 

secondCountLength = len(secondCount)
#Длина числа
a2 = int(secondCountLength)
#Первый символ
b2 = int(secondCount[0])
#Последний символ
c2 = int(secondCount[secondCountLength - 1])

print('Количество символов: ', a)
print('Первый символ: ', b)
print('Последний символ: ', c)
print('Сумма первого и последнего числа: ', b + c)

if (b == b2):
 print(b, ' = ', b2)
else:
 print(b, '!=', b2)
