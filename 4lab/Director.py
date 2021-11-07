from Chief import Chief
from Manager import Manager

class Director(Chief):

    def __init__(self, office, sur, pos, sal, people, comp_name):
        self.__comp_name = comp_name
        Chief.__init__(self, office, sur, pos, sal, people)

    @property
    def comp_name(self):
        return self.__comp_name

    @comp_name.setter
    def comp_name(self, a):
        self.__comp_name = a

    def display_info(self):
        s = "Название компании: " + self.__comp_name + "\n "
        s += Manager.display_info(self)+"\n -----------Подчиненные----------- \n"
        for i in self.people:
            s+="    " +str(i)+" \n"
        s+="---------------------------------"
        return s

    def assign(self):
        s = self.surname[:4]
        if (s == "Сере"):
            self.office = "Москва"