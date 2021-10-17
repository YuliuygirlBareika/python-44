from abc import ABC, abstractmethod

Time_at_work = {'manager': 9, 'programmer': 24, 'businessAnalyst': 12, 'tester': 10}

class Humen(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    @abstractmethod
    def work_experience(self):
        pass
    
    @abstractmethod
    def year(self):
        pass    

    @abstractmethod
    def residence(self):
        pass
    
    @abstractmethod
    def profession(self):
        pass

    @abstractmethod
    def time_at_work(self):
        pass
    

class Manager(Humen):

    @property
    def work_experience(self):
        if (self.age - 18) > 0:
            return (self.age - 18)
        return 0

    def year(self):
        print(f'Age is: {self.age}')
    
    def residence(self, city):
        self.city = city
        print(f'Residence: {self.city}')

    def profession(self):
        print(f'Profession: Manager')

    def time_at_work(self):
        print(f'Work time is: {Time_at_work.get("manager")}')


class Programmer(Humen):
    
    @property
    def work_experience(self):
        if (self.age - 18) > 0:
            return (self.age - 18)
        return 0

    def year(self):
        print(f'Age is: {self.age}')
    
    def residence(self, city):
        self.city = city
        print(f'Residence: {self.city}')

    def profession(self):
        print(f'Profession: Programmer')

    def time_at_work(self):
        print(f'Work time is: {Time_at_work.get("programmer")}')

class BusinessAnalyst(Humen):
    
    @property
    def work_experience(self):
        if (self.age - 18) > 0:
            return (self.age - 18)
        return 0

    def year(self):
        print(f'Age is: {self.age}')

    def residence(self, city):
        self.city = city
        print(f'Residence: {self.city}')

    def profession(self):
        print(f'Profession: Business Analyst')

    def time_at_work(self):
        print(f'Work time is: {Time_at_work.get("businessAnalyst")}')

class Tester(Humen):
    
    @property
    def work_experience(self):
        if (self.age - 18) > 0:
            return (self.age - 18)
        return 0

    def year(self):
        print(f'Age: {self.age}')

    def residence(self, city):
        self.city = city
        print(f'Residence: {self.city}')

    def profession(self):
        print(f'Profession: Tester')

    def time_at_work(self):
        print(f'Work time is: {Time_at_work.get("tester")} hours')
    
    
L = Manager('Lisa', 16)
S = Programmer('Sasha', 32)
O = BusinessAnalyst('Olya', 30)
P = Tester('Pasha', 27)

group = [L, S, O, P]
for instance in group:
    print(f'   {instance.name}')
    instance.profession()
    instance.residence('Russia')
    instance.year()
    instance.time_at_work()
    print(f'Work experience: {instance.work_experience} years')
    
