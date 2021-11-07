# Напишите функцию, которая принимает на вход два целых числа
# a, b и возвращает кортеж из чисел в промежутке [a:b], имеющих наибольшее
# количество делителей.

def delit(a,b):
    res = []
    max = 0
    for i in range(a,b):
        count = 0
        for de in range(1,i):
            if i%de==0:
                count+=1
        if count>max:
            res.clear()
            max = count
        if count>=max:
            res.append(i)
    return tuple(res)

ab = int(input("введите число a = "))
ba = int(input("введите число b = "))
print(delit(ab,ba)) 