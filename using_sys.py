import sys

print ('аргументы командной строки')
for i in sys.argv:
	print (i)
print ('\n\nПеременная PYTHONPATH СОДЕРЖИТ', sys.path,'\n')