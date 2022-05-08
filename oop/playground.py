from employee import Employee as emp
from employee import Developer as dev
from employee import Manager as mng
import datetime as dt


# creating objects
# regular employees
john_smith = emp("John", "Smith", 60)
john_doe = emp("John", "Doe", 404)


# calling methods
print(john_smith.pay)
john_smith.apply_raise()
print(john_smith.pay)

print(john_smith.__dict__)  # in all properties listed there's no class variable
print(emp.__dict__)  # there's a class variable


# class variables in action
print(
    "Class variable value inside class before changes: " + str(emp.raise_amount)
)  # hardcoded value
print(
    "Class variable value inside an object before changes: "
    + str(john_smith.raise_amount)
)  # hardcoded value
john_smith.raise_amount = 2.34
print(
    "Class variable value inside class after changes: " + str(emp.raise_amount)
)  # hardcoded value
print(
    "Class variable value inside an object after changes: "
    + str(john_smith.raise_amount)
)  # 2.34


# class methods in action
emp.set_raise_amount(1.56)
print(emp.raise_amount)
print(john_smith.raise_amount)


# creating a new object using class method as an altrnative constructor
elsa_porter = emp.from_string("Elsa-Porter-90")
print(elsa_porter.email)
print(elsa_porter.pay)


# useing static methods
# check if date is a workday of a weekend
my_date = dt.date(2022, 5, 1)
print("It's a workday") if emp.is_workday(my_date) == True else print("It's a weekend")


# inheritance in action
# new developers
john_carmack = dev("John", "Carmack", 666, "Edgy C++")
john_romero = dev("John", "Romero", 666, "Blood & Heavy Metal")
print(str(john_carmack.pay) + " for some " + john_carmack.programming_lang + " code")
john_carmack.apply_raise()
print(john_carmack.pay)


phil_spencer = mng("Phil", "Spencer", 999, [john_carmack])
phil_spencer.add_employee(john_romero)
phil_spencer.print_employees()
phil_spencer.remove_employee(john_romero)
phil_spencer.print_employees()


# dunder methods in action
print(john_smith)  # __repr__() works by default if __str__ is not implemented
print(repr(john_doe))  # calling __repr__() specifically
print(str(john_doe))  # calling __str__() specifically

# same calls, but different approach
# print(john_smith.__repr__())
# print(john_smith.__str__())

print(john_smith + john_doe)  # calling __add__() method
print(len(john_smith))


# properties in action
print(john_doe.fullname)
print(john_smith.email)


# setters in action
john_doe.fullname = "Anonymous Hacker"
print(john_doe.fullname)
print(john_doe.email)


# deleters in action
del john_doe.fullname
print(john_doe.fullname)
print(john_doe.email)
