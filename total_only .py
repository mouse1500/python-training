def total(initial = 5, *numbers, extra_number):
	count = initial
	for number in numbers:
		count += number
	count += extra_number
	print(count)
total(10, 1, 2, 3, extra_number)
total(10, 1, 2, 3)

# вызывает ошибку поскольку не указанно значение
# аргумена по умолчанию 'extra_number'
	