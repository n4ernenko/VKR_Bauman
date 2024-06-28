# определяем диалект
import csv

main_path = 'D://VKR/VKR_Project/'  # путь до папки с обрабатываемым файлом(в данном случае файл помещен в папку проекта)
orig_csv_name = 'fz.csv'  # имя самого файла

with open(main_path+orig_csv_name, 'r', encoding='utf-8', newline='') as infile:
    dialect = csv.Sniffer().sniff(infile.read(1024))
print(
    "detected delimiter = %s\n"
    "detected doublequote = %s\n"
    "detected escapechar = %s\n"
    "detected lineterminator = %s\n"
    "detected quotechar = %s\n"
    "detected quoting = %s\n"
    "detected skipinitialspace = %s\n" %(
        dialect.delimiter, dialect.doublequote, dialect.escapechar, repr(dialect.lineterminator), dialect.quotechar, dialect.quoting,
        dialect.skipinitialspace))