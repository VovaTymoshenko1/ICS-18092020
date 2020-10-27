
import os
import random
from collections import Counter
import collections

#Завдання 1
first_list = ['Monday', 'Tuesday', 'Wendesday', ]
second_list = ['rainy', 'sunny', 'cloudy']
third_list = ['day', 'evening', 'morning', ]

list_of_strings_list = [first_list, second_list, third_list]

def random_phrase():
     result_string = ""
     for i in range(0, 3):
        random_index = random.randrange(0, 3)
        result_string = result_string + \
            list_of_strings_list[i][random_index] + " "

     return result_string

#print(random_phrase())

#Завдання 2

#кількість слів з пробілами
book = 'lastkid.txt'
filename = book
 
def counting_chars_with_space():
    
    file = open(filename, 'r')
    data = file.read()
    amount = len(data)
    
    file.close()

    return amount


#Кількість слів без пробіів
def counting_amout_of_chars_without_spaces():

 num_chars = 0

 with open(filename, 'r') as f:
    for line in f:
        for letter in line:
            for i in letter:
                 if(i != ' ' and i != '\n'):
                    num_chars += 1

 return num_chars



#Завдання 3 Варіант 11

book = open('lastkid.txt')
data = book.read()
s = data.split()

s1 = [len(i) for i in s]

s2 = s1.count(1)
s3= s1.count(2)
s4= s1.count(3)
s5= s1.count(4)
s6= s1.count(5)
s7= s1.count(6)
s8= s1.count(7)
s9= s1.count(8)
s10= s1.count(9)
s11= s1.count(10)
s12= s1.count(11)
s13= s1.count(12)
s14= s1.count(13)
s15= s1.count(14)
s16= s1.count(15)
s17= s1.count(16)
print('1:'+ str(s2))
print('2:'+ str(s3))
print('3:'+ str(s4))
print('4:'+ str(s5))
print('5:'+ str(s6))
print('6:'+ str(s7))
print('7:'+ str(s8))
print('8:'+ str(s9))
print('9:'+ str(s10))
print('10:'+ str(s11))
print('11:'+ str(s12))
print('12:'+ str(s13))
print('13:'+ str(s14))
print('14:'+ str(s15))
print('15:'+ str(s16))
print('16:'+ str(s17))
print('Кількість символів з пробілами:' + str(counting_chars_with_space()))
print('Кількість символів без пробілів:' + str(counting_amout_of_chars_without_spaces()))
