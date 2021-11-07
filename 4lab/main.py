from classes import Worker
from Manager import Manager
from Chief import Chief
from Director import Director

w1 = Worker("Ива", "ghj", 40000)
w1.assign()
w1.display_info()
w1.increase_salary()
w2 = Worker("Иванов", "jfl", 24754)
w2.assign()
w2.increase_salary()



m1 = Manager("GJ", "yua", "msc", 5674)
m1.assign()
m1.increase_salary()
m2 = Manager("NY","Иван","roc", 648345)
m2.assign()


c1 = Chief("msc","fam","dir",453333,[w1, m1, w2, m2])
c1.assign()
c2 = Chief("hdsl", "Ивановичов", "глава отдела по продажам", 468168, [c1])
c2.assign()


d1 = Director("fgjer", "Серегешвили", "маркетинг", 478281, [c2], "CoCo")
d1.assign()
print(d1)
