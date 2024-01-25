#ICP 3 
#Employee Problem

class Employee:
   # Create a data member to count the number of Employees
    empcount = 0

    #Create a constructor to initialize name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        
        Employee.empcount += 1

    #Create a function to average salary
    def average_salary(employees):
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.empcount

#Create a Fulltime Employee class and it should inherit the properties of Employee class
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
    
        super().__init__(name, family, salary, department)

    

#Create the instances of Fulltime Employee class and Employee class and call their member functions.
employees = []
fullemp_1= FulltimeEmployee("Emp1", "FamName1", 156000, "Development")
employees.append(fullemp_1)

fullemp_2= FulltimeEmployee("Emp2", "FamName2", 173000, "Testing")
employees.append(fullemp_2)

emp_1 = Employee("Emp3", "FamName3", 191000, "Design")
employees.append(emp_1)

emp_2 = Employee("Emp4", "FaName4", 127000, "Project Lead")
employees.append(emp_2)

print("Average salary:", FulltimeEmployee.average_salary(employees))


print("Total number of employees:", Employee.empcount)
