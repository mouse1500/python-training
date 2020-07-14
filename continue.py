while True:
	s = input ('Введите что угодно: ')
	if s == 'выход':
		break
	if len(s) < 3:
		print ('Слишком коротко')
		continue
print ('Строка оптимальной длинны.')
