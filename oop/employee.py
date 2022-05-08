class Employee:
    # class variable (available for all class instances);
    #
    # each object contains a copy of this variable, so changing its value for an
    # object won't affect its value for the class;
    #
    # but changing its value on the class level will change the value for all objects
    raise_amount = 1.23

    # class constructor
    def __init__(self, first_name, last_name, pay):
        # __init__() function is called every time an object is created from a class.
        # The __init__ method lets the class initialize the object's attributes
        # and serves no other purpose. It is only used within classes.
        #
        # 'self' is used as 'this' in C#, for example;
        # it represents the instance of the class.
        # By using the “self”  we can access the attributes and methods
        # of the class in python. It binds the attributes with the given arguments.

        # properties
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = first_name + "." + last_name + "@companydomain.com"

    # property decorators (getters & setters analogue)
    # property decorators allow to define a method, but access it like a property
    @property
    def email(self):
        return "{} {}@companydomain.com".format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    # setters
    @fullname.setter
    def fullname(self, new_name):
        first, last = new_name.split(" ")  # split the new name by space
        self.first_name = first
        self.last_name = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first_name = None
        self.last_name = None

    # regular methods (automaically take class instance as the first argument)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # dunder methods (special methods)
    #
    # if __repr__ is defined, and __str__ is not, the object will behave as though __str__=__repr__;
    #
    # __repr__() - unambiguous representation of the object (is meant to be used for
    # logging/debugging etc.)
    def __repr__(self):
        # print a string by that it is possible to recreate the object
        return "Employee('{}', '{}', '{}')".format(
            self.first_name, self.last_name, self.pay
        )

    # __str__() - readable representation of the object (is meant to be used
    # as a display to an end user)
    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.email)

    # calculate total salary by adding 2 employees' salaries
    def __add__(self, other):
        return self.pay + other.pay

    # calculate employee email length
    def __len__(self):
        return len(self.email)

    # class methods (take class as the first argument instead of instance);
    # according to naming convention, the first argument must be named 'cls'
    # (as 'self' for regular methods)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor
    @classmethod
    def from_string(cls, employee_str):
        # in case wewant to create a new object from Employee data string
        # that looks like 'John-Doe-404'
        first_name, last_name, pay = employee_str.split("-")
        return cls(first_name, last_name, int(pay))

    # static methods (don't take class or its instance as the first argument);
    # best practice is to use static methods if there's no need to use class
    # or object inside the method
    @staticmethod
    def is_workday(day):
        if day.weekday() in range(6, 7):
            return False  # it is a weekend
        return True  # it is a workdy


class Developer(Employee):
    raise_amount = 1.5

    def __init__(self, first_name, last_name, pay, programming_lang):
        # make base class constructor set the same values without code duplication
        super().__init__(first_name, last_name, pay)
        # alternative way
        # Employee.__init__(self, first_name, last_name, pay)
        self.programming_lang = programming_lang


class Manager(Employee):
    # best practice is not to pass mutable data types as
    # constructor arguments; so 'None' instead of 'List' or 'Set' etc.
    def __init__(self, first_name, last_name, pay, empployees=None):
        super().__init__(first_name, last_name, pay)
        if empployees is None:
            self.employees = []
        else:
            self.employees = empployees

    # add a new employee for manager to supervise
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    # remove an employee
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print("---" + emp.first_name + " " + emp.last_name)
