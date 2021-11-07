# Напишите функцию, которая принимает произвольное число
# аргументов (каждый аргумент – список) и возвращает True если пересечение
# списков пустое, иначе возвращает False.

def peres(*params):
    l = set(params[0])
    for i in params:
        l= l.intersection(i)
    answ=len(l)>0
    return not answ

print(peres([1,2,3],[2,5,7],[32,5,2])) 
print(peres([1,2,3],[4,5,6],[7,8,9]))
print(peres([9,11,3],[32,5,2]))
print(peres([1,3,2],[2,5,3]))
