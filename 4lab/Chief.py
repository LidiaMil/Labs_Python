from Manager import Manager
class Chief(Manager):

    def __init__(self, office, sur, pos, sal, people):
        self.__people = people
        Manager.__init__(self, office, sur, pos, sal)

    def display_info(self):
        s = Manager.display_info(self) + "\n Рабочие: \n"
        for i in self.__people:
            s +="    "+ str(i) + "\n"
        return s

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, a):
        self.__people = a
