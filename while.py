number = 25
running = True

while running:
	gays = int ( input ('Введите число:'))
	
	if gays == number:
		print ('Вы угодали.')
		running = False
	elif gays < number:
		print ('Это не верное число, оно немного больше.')
	else:
		print ('Это не верное число, оно немного меньше.')
print ('Конец.')
	 
