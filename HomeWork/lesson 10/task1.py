pets ={}

while (True):
    k=input("Введите имя питомца  (клавиша enter - выход): ")
    if k=='':
        break
    else:
        pets2={}
        k1=input('Вид питомца: ')
        k2=int(input('Возраст питомца: '))
        year_case = ''
        if k2 % 10 == 1 and k2 != 11 and k2 % 100 != 11:
            year_case = 'год'
        elif 1 < k2 % 10 <= 4 and k2 != 12 and k2 != 13 and k2 != 14:
            year_case = 'года'
        else:
            year_case = 'лет'
        k3=input('Имя владельца:  ')
        pets2={'Вид питомца:':k1, 'Возраст питомца:':k2, 'Имя владельца:':k3  }
        pets[k]=pets2

for k, v in pets.items():
    print("Это", v['Вид питомца:'], "по кличке", k, ". Возраст питомца:", v['Возраст питомца:'], year_case, "Имя владельца:", v['Имя владельца:'])