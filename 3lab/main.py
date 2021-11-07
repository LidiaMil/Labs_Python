# Напишите функцию, которая выводит первые n строк треугольника Паскаля.

def pas(row):
    if row>0:
        trio = [[1]]
        row-=1
        for i in range(row):
            trio.append(rowpas(trio[i]))
        return trio
    else:
        n = int(input("введите число = "))
        print(pas(n))
        # return "введи целое число больше 0 :)"


def rowpas(rowex):
    nrow = [1]
    for i in range(1,len(rowex)):
        nrow.append(rowex[i]+rowex[i-1])
    nrow.append(1)
    return nrow

n = int(input("введите число = "))
print(pas(n))