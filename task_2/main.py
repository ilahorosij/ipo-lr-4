#Каленик Илья
numbers = list(map(int,input('введите числа ').split()))#запрашиваем числa map int преобразовывет все слова в числа
squares = []
for i in numbers: # начинаем с 1 до n с шагом 1
    squares.append(i * i)# умножаем и выводим
print(numbers)
print(squares)
