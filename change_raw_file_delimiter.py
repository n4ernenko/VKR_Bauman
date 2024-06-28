import csv

raw_csv_path = 'D://VKR/VKR_Project/'  # путь до папки с обрабатываемым файлом(в данном случае файл помещен в папку проекта)
raw_csv_name = 'raw_fz.csv'  # имя оригинального файла
new_csv_name = 'new_del.csv'  # имя нового файла

row = []  # список для манипуляций со строками файлов
total_row_count = 0

# подсчет общего числа строк в файле и запись строк с количеством элементов больше 27 в файл с именем 'bad_rows.csv'.
# При проверке гипотезы о влиянии символа экранирования '\', в объекты reader и writer передаем escapechar = '\\'. Можно написать диалект и передавать его.
with (open(raw_csv_path+raw_csv_name, 'r', encoding='utf-8', newline='') as infile,
      open(raw_csv_path+new_csv_name, 'w', encoding='utf-8', newline='') as outfile):
    infile.seek(0)  # указатель в начало файла
    reader = csv.reader(infile, escapechar='\\', delimiter=',')  # объект для чтения
    outfile.seek(0)  # указатель в начало файла
    writer = csv.writer(outfile, escapechar='\\', delimiter='|')  # объект для записи
    for row in reader:  # перебор строк в объекте чтения
        total_row_count += 1  # увеличиваем на 1, пока не закончатся строки
        writer.writerow(row)  # и пишем строку в файл 'bad_rows.csv'