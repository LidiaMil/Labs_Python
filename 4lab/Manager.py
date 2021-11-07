from classes import Worker
class Manager(Worker):
    def __init__(self, office, sur, pos, sal):
        self.__office = office
        Worker.__init__(self, sur, pos, sal)

    def display_info(self):
        s = Worker.display_info(self)
        s+=str(" Офис: "+str(self.__office))
        return s

    def assign(self):
        s = self.surname[:4]
        if(s == "Иван"):
            self.salary *= 5

    @property
    def office(self):
        return self.__office

    @office.setter
    def office(self, a):
        self.__office = a