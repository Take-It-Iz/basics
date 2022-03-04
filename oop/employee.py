# class that inherits from Human
from human import Human

class Employee(Human):
    position = 'trainee'
    chef = 'anyone'
    experience = 0
    departament = 'basement dweller'
    duty = 'drop the production db'
    salary = 100

    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, age) # for the parent class to take all arguments 
                                               # given to the inherited class   
    
    # overriden methods
    def eat(self, food):
        return f"Employees eat {super.eat(food)}"

    # overloaded methods
    def set_bank_acc_password(self, password, crap = 'asdf1337'):
        if self.__bank_acc_password is not crap:
            self.__bank_acc_password = password
        else:
            self.__bank_acc_password = 'flgvjafghapofghfg'
        
    # methods
    def get_boss_mad(self):
        self.experience = 0
        self.salary = 0
        self.position = 'trainee'
        self.chef = 'anyone'
        self.departament = 'basement dweller'
        self.duty = 'drop the production db'        
        print('All your stats dropped to the very bottom')

    def get_promotion(self, position, departament, duty, salary):
        self.position = position
        self.departament = departament
        self.duty = duty
        self.salary = salary
        print('You got new benefits and obligations')
