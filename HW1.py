#DZ-1
#a = 1
#b = 5
#print("Переменные a и b - ", a, b)
#string1 = input("Введите первую строку ")
#number1 = int(input("Введите первое число "))
#print((string1, number1))


#DZ-2
#time = int(input("Введите время в секундах "))
#hours = time // 3600
#minutes = (time - hours * 3600) // 60
#seconds = time - (hours * 3600 + minutes * 60)
#print(f"{hours} : {minutes} : {seconds}")




#DZ-3
#number = int(input("Введите число от 1 до 9: "))

#if number >= 10:
    #print("Ошибка!!")

#else:
   #res = number + (number * 11) + (number *111)
   #print (res)



#DZ-4
#number = int(input("Введите целое число: "))

#max = 0

#while number > 0:
    #n = number % 10
    #if n >= max:
        #max = n
    #number //= 10

#print(max)



#DZ-5

#proc = int(input("Выручка составила: "))
#cons = int(input("Расход составил: "))

#if proc > cons:
    #print("Выручка больше расходов")

#elif cons > proc:
    #print("Расходы больше выручки")


#DZ-6
#a = int(input("Введите результаты пробежки спортсмена в 1й день в км "))
#b = int(input("Введите желаемый результат в км "))
#result_days = 1
#result_km = a

#while result_km < b:
       #a = a + ( a * 0.1 )
        #result_km = result_km + a



