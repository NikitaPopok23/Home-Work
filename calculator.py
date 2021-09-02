listA = ['+', '-', '/', '*','//','**']
while True:
        a = input (" Что будем делать (+ ,* ,- ,/ ,** ,//) : " )
        if a.lower() == 'exit':
            break
        if not a in listA:
            print("Вы не правильно ввели действие, повторите.")
            continue
        b = float(input ("Введите число: "))
        c = float(input ("Введите число: "))
        if a == "+":
            g = b + c
            print (" Число равняется : " + str(g))
        elif a == "*":
            g = b * c
            print (" Число равняется : " + str(g))
        elif a == "-":
            g = b - c
            print (g)
        elif a == "/":
            g = b / c
            print (g)
            ZeroDivisionError: divisionbyzero
            print("На ноль делить нельзя")
        elif a == "**":
            g = b ** c
            print (g)
        elif a == "//":
            g = b // c
            print (g) 
        question = input ('продолжаем y/n ? ')
        if question == 'y':
            continue
        else:
            print ('До свидания')
            break    
