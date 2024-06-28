import csv
import operator

main_path = 'D://VKR/VKR_Project/'  # путь до папки с обрабатываемым файлом(в данном случае файл помещен в папку проекта)
orig_csv_name = 'fz.csv'  # имя оригинального файла
new_csv_name = 'selected_rows.csv' # имя нового файла

categories_to_filter=['71.1','41.1', '41.2', '42.1', '42.2', '42.9', '43.1', '43.2', '43.3', '43.9']
selected_row_count = 0
other_row_count = 0
total_row_count = 0

with (open(main_path+orig_csv_name, 'r', encoding='utf-8', newline='') as infile,
      open(main_path+new_csv_name, 'w', encoding='utf-8', newline='') as outfile):
    # если захочется записать остаток в отдельный файл
    # open(main_path+'other_cat.csv', 'w', encoding='utf-8', newline='') as outfile2):
    infile.seek(0)  # указатель в начало файла
    reader = csv.reader(infile, escapechar='\\', delimiter=',')  # объект для чтения
    outfile.seek(0)  # указатель в начало файла
    writer = csv.writer(outfile, escapechar='\\', delimiter='|')  # объект для записи
    # outfile2.seek(0)  # указатель в начало файла
    # writer_other = csv.writer(outfile2, escapechar='\\', delimiter='|')  # объект для записи
    for row in reader:
        row_ = operator.itemgetter(-1)(row)
        if row_ in categories_to_filter:
            selected_row_count += 1
            writer.writerow(row)
        else:
            other_row_count += 1
            # writer_other.writerow(row)
total_row_count = selected_row_count + other_row_count

print(f"Number of rows SELECTED: {selected_row_count}")
print(f"Number of OTHER rows in the CSV file: {other_row_count}")
print(f"TOTAL number of rows: {total_row_count}")

