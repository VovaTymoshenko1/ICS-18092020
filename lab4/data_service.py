from dataclasses import dataclass

code = [110, 120, 130, 140, 150]
name = ["ІНКО", "АЖІО", "Градобанк", "Відродження", "Укрінбанк"]

@dataclass
class dovidnik:
   code:int
   name:str


data_array = [dovidnik(110, "ІНКО"), dovidnik(120,"АЖІО"), dovidnik(130,"Градобанк"), dovidnik(140, "Відродження"), dovidnik(150,"Укрінбанк")]

def printdovidnik(dovidnik):
    '''printdovidnik function prints with names and values'''
    print("Код {code}, Назва {name}" .format(code = dovidnik.code, name = dovidnik.name))

for data in data_array:
    printdovidnik(data)

    
