#Каленик Илья
numbers = list(map(int, input('введите числа ').split()))#запрашиваем числa map int преобразовывет все слова в числа
squares = [i * i for i in numbers] # генератор списков и выводим
print(numbers)
print(squares)