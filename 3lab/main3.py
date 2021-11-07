# Напишите функцию, которая принимает в качестве аргумента
# список и возвращает True, если все значения внутри данного списка уникальны,
# иначе возвращает False.

def unic(ls):
    srav = []
    for i in ls:
        if i not in srav:
            srav.append(i)
        else:
            return False
    return True


print(unic([1,2,3,4]))
print(unic([4,3,2,3,5]))
arr=input("введите число массив ")
print(unic(list(map(int, arr.split()))))
