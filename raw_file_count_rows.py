# подсчет общего числа строк в файле и запись строк с количеством элементов больше 27 в файл с именем 'bad_rows.csv'.
# При проверке гипотезы о влиянии символа экранирования '\', в объекты reader и writer передаем escapechar = '\\'.
# Можно написать диалект и передавать его.
import csv

main_path = 'D://VKR/VKR_Project/'  # путь до папки с обрабатываемым файлом(в данном случае файл помещен в папку проекта)
orig_csv_name = 'fz.csv'  # имя оригинального файла
new_csv_name = 'bad_rows.csv'  # имя нового файла

total_row_count = 0
good_row_count = 0
bad_row_count = 0

with (open(main_path+orig_csv_name, 'r', encoding='utf-8', newline='') as infile,
      open(main_path+new_csv_name, 'w', encoding='utf-8', newline='') as outfile):
    infile.seek(0)  # указатель в начало файла
    reader = csv.reader(infile)  # объект для чтения
    outfile.seek(0)  # указатель в начало файла
    writer = csv.writer(outfile)  # объект для записи
    for row in reader:  # перебор строк в объекте чтения
        total_row_count += 1  # увеличиваем на 1, пока не закончатся строки
        if len(row) > 27:  # проверяем количество строк с списке
            bad_row_count += 1  # если строка - список с кол-вом элементов > 27, то увеличиваем счетчик на 1
            writer.writerow(row)  # и пишем строку в файл 'bad_rows.csv'
        else:
            good_row_count +=1
# Делаем дополнительные вычисления
bad_row_percentage = bad_row_count * 100/total_row_count
# Выводим их
print(f"TOTAL number of rows in the CSV file: {total_row_count}")
print(f"Number of GOOD rows in the CSV file: {good_row_count}")
print(f"Number of BAD rows in the CSV file: {bad_row_count}")
print(f"Percentage of BAD rows in the CSV file: {bad_row_percentage}")
