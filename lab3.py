import random

gun = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


random.shuffle(gun)

print('Твоя ціль: набрати максимальну кількість очко за влучання(максимум 10).')

count = 0

shot = input("Для вистрелу введіть F \n")
if input == 'F':
    current = gun.pop()
    print('Ви влучили в %d' % current)
    count +=current
    if count >8:
        print('А ти молодчина!')
    elif count == 10:
        print('Воу воу, охолонь, ковбоє!')
    else:
        print('Та навіть моя бабця краще б вистрелила')
 
 
