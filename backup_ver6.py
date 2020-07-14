import time
import zipfile
import os
# файлы и каталоги, которые необходимо скопировать, собираются в список
source = ['D:\\python\test', 'D:\\python\test2']
# Для имен содержащих пробелы необходимо указывать двойные кавычки внутри строки

# резервные копии хранятся в основном каталоге резерва.
target_dir = 'D:\\backup'

# помещаем файлы в зип архив.
today = target_dir + time.strftime ('%Y%m%d')
# текущее время служит именем архива
now = time.strftime ('%H%M%S')

# запрашиваем комментарий пользователя для имени файла
comment = input ('Введите коментарий -->')
if len (comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace ( ' ', '_') + '.zip'

# создаем каталог если его нет
if not os.path.exists (today):
	os.mkdir (today) # создание каталога
print ('каталог создан', today)

# используем команду зип для помещения файлов в зип архив
z = zipfile.ZipFile (target, 'w')
for folder, subfolder, files in os.walk (source):
	for file in files:
		z.write (os.paht.join (folder, file), os.path.relpath (os.path.join (folder, file), target_dir))
# запускаем создание резервной копии
if  z (zipfile.ZipFile)  == 0:
	print('резервная копия успешно создана в', target)
else:
	print('создание резервной копии не удалось')