import os
import glob
import csv
import sys

#запис тексту
def func1():
    file = open('firstgroup.txt', 'w', encoding='utf-8')
    f1 = input('Введіть текст для запису:')
    file.write(f1)
    file.close()

#дозапис тексту
def func2():
    file = open('firstgroup.txt', 'a+', encoding='utf-8')
    f2 = input('Введіть текст для дозапису:')
    file.write(f2)

    print("Введіть stopWriting для того щоб зупити процес дозапису")

    while True:
        new_line = input("Введіть новий рядок \n")

        if new_line != "stopWriting":
            file.write("\n"+new_line)
        else:
            return
    file.close()

#читання файлу
def reading():
    filename = 'firstgroup.txt'
    file = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(file, delimiter="\t") 
    for row in reader:
        print(row)
    file.close()

def sort():
    filename = 'firstgroup.txt'
    dict = {}
    file = open(filename, "r+")
    reader = file.readlines()
    for row in reader:
        split_row_by_coma = row.split(',')
        dict[int(split_row_by_coma[1].strip())] = split_row_by_coma[0].strip()


    sorted_keys = list(dict.keys())
    for key in range(0, len(sorted_keys)):

        for j in range(0, len(sorted_keys) - key - 1):

            if sorted_keys[j] > sorted_keys[j+1]:
                sorted_keys[j], sorted_keys[j+1] = sorted_keys[j+1], sorted_keys[j]

    sorted_dict_by_key = {}
    for sorted_key in sorted_keys:
        sorted_dict_by_key[sorted_key] = dict[sorted_key]
    print(sorted_keys)
    print(sorted_dict_by_key)

    write_to_file_sorted_dict(filename, sorted_dict_by_key)

    file.close()
def write_to_file_sorted_dict(filename, dict):

    file = open(filename, "w")
    
    student_mark_strings_list = []

    for key in dict:
        student_mark_strings_list.append(f'{dict[key]}, {key}')

    write_string = ""

    for new_text_item in student_mark_strings_list:
        write_string = write_string + new_text_item.strip() + "\n"

    file.write(write_string)

    file.close()

#пошук тексту у файлі
def search():
    file = open('firstgroup.txt', 'r', encoding='utf-8')
    strings = file.read()
    searchname = input("Введіть потрібний вам текст: \n")
    if (searchname in strings):
        print ('Такий текст присутній у базі данних.')
    else:
        print("Такого тексту не знайдено в базі данних:")
    file.close()

    

#print(func1())
#print(func2())
#print(reading())
#print(sort())
print(search())