kalendar = {
	'year' : '2025',
	'month': '12',
	'day'  : '31', 
}
print (kalendar['year'], '-', kalendar['month'], '-', kalendar['day'])

spisok = [1, 2, 3, 4, 5, 6]
print(spisok[2 : 5])

word = 'word'
print(list(word))

print ('Введите первое число: ')
firstCount = input()
print ('Введите второе число: ')
secondCount = input()

if int(firstCount) % int(secondCount) == 0:
 print('Число ', firstCount, 'делится на', secondCount, 'без остатка' ) 
else:
 print('Число ', firstCount, 'не делится на', secondCount, 'без остатка' )

firstString = input('Введите слово: ')
firstStringLen = len(firstString)

if firstStringLen >= 2:
 print(firstString[firstStringLen - 2]) 
else:
 print(firstString)