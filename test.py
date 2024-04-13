#Ввод числа пользователем
minusInt = input('Введите число \n')

#Проверка положительности
if int(minusInt) < 0:
 print ('Отрицательное \n')
else:
 print ('Положительное\n')

#Проверка чётности
if int(minusInt)%2 == 0:
 print ('Чётное\n')
else:
 print ('Нечётное\n')

#Ввод строки пользователем
firstWord = input ('Введите строку\n')
#Длина строки
lengthFirstWord = len(firstWord)
#Вывод длины и последнего символа строки
print ('Количество символов: ', len(firstWord))

if firstWord[lengthFirstWord - 1] == 'ь':
 print ('Последний символ: ', firstWord[lengthFirstWord - 2])
else:
 print ('Последний символ: ', firstWord[lengthFirstWord - 1])

secondWord = input ('Введите строку\n')

if firstWord[0] == secondWord[0]:
 print (firstWord[0], ' = ', secondWord[0])
else:
 print (firstWord[0], ' != ', secondWord[0])