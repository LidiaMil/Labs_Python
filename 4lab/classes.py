class Worker:
    def __init__(self, surname, position, salary):
        self.__surname = surname
        self.__position = position
        self.__salary = salary

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, a):
        self.__surname = a

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, a):
        self.__position = a

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, a):
        self.__salary = a

    def display_info(self):
        return str("Фамилия: "+ self.surname+ "  Должность: "+self.position+"  Оклад: "+ str(self.salary))

    def __del__(self):
        print(self.surname, "удален из памяти")

    def increase_salary(self):
        self.salary += (self.salary * 0.15)
        print(self.salary)

    def assign(self):
        s = self.surname[:4]
        if (s=="Иван"):
            self.position = "Инженер"
    def __str__(self):
        return self.display_info()
