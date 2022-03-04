# import employee
# import human
import sys
from employee import Employee
from human import Human
import stuff
from stuff import module_method 

sys.path.append(".") #call list.append(dir), with dir as "." to add 
                     #the current directory as a path to search for modules;
                     

if __name__ == '__main__':
    
    baby = Human('Little', 'Boy', 1)
    Isaac_Clarke = Employee('Isaac', 'Clarke', 36)
    
    # section works if only modules are imported; though it started working only 
    # after adding directory to PYTHONPATH with sys.path.append(".")
    # baby = human.Human('Little', 'Boy', 1)
    # Isaac_Clarke = employee.Employee('Isaac', 'Clarke', 36)
    
    print(Isaac_Clarke.age)

    sth_object = stuff.DifferentClass()
    sth_object.class_method()
    module_method()