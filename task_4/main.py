squares = []
for i in range(0,21): # перебираем числа от 0 до 21
    if i%2 == 0:# если число четное то выводим его квадрат
        squares.append(i * i)
print(squares)
