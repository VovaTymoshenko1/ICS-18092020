#@copyright Тимошенко_Володимир_Назарійович_ФІТ_1КУРС_4ГРУПА
import sys
import pdfminer.high_level

with open('zad8.pdf', 'rb') as file:
    pdfminer.high_level.extract_text_to_fp(file, sys.stdout)