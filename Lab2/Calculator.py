#какькулятор Тимошенка Володимира



what= input("Виберіть дію (+;-;*;/):")



a = float(input("Запишіть перше число:"))
b = float(input("Запишіть друге число:"))

if what == "+":
    c = a+b
    print("Результат:" + str(c) )

elif what == "-":
    c = a-b
    print("Результат:" + str(c) )
    
elif what == "*":
    c = a*b
    print("Результат:" + str(c))
elif what == "/":
    c = a/b
    print("Результат:" + str(c))
else:
    print("Вибрана невірна операція")

    
input()
