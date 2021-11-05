#definition of the parental class 
class Human:
    #attributes common for all instances; 
    #they can be changed dynamically using dot-notation 
    species = 'Homo Sapiens' 
    _citizenship = 'Citizen of the world' #protected field
    __bank_acc_password = 'qwerty1234' #private field

    #constructor
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    #methods
    def __str__(self):
        print('I think, therefore I am')

    def eat(self, food):
        return f"{self.name} just ate a spicy {food}"
    
    def sleep(self, hours):
        return f"{self.name} needs a healthy {hours} hour sleep"
    
    def work(self):
        return f"{self.name} must work until he is {self.age - 15} years old"

    def set_bank_acc_password(self, password):
        self.__bank_acc_password = password

    def change_citizenship(self, citizenship):
        self._citizenship = citizenship
