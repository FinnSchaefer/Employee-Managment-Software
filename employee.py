import datetime
import company
class Employee(company.Company):
    def __init__(self, fname, lname, age, salary, dateHired=None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary
        self.yearsEmployed = 0
        self.projects = []
        self.cname = company.Company.name
        
        if dateHired == None:
            self.dateHired = datetime.date.today()
        else:
            self.dateHired = dateHired
            self.yearsEmployed = datetime.date.today().year - self.dateHired.year
        
    def updateYearsEmployed(self):
        self.yearsEmployed = datetime.date.today().year - self.dateHired.year
        
    def updateAge(self):
        self.age += self.yearsEmployed
                
    def __str__(self):
        return self.fname + " " + self.lname + " " + str(self.age) + " " + str(self.salary) + " " + str(self.yearsEmployed)
    

class Manager(Employee):
    def __init__(self, fname, lname, age, salary, dateHired=None):
        super().__init__(fname, lname, age, salary, dateHired)
        self.teamList = []
          
    def hireEmployee(self, employee):
        self.teamList.append(employee)
        
    def fireEmployee(self, employee):
        self.teamList.remove(employee)
        del employee
        
    #find the the employee in team list with the matching first name and last name and give them a raise of raisePercent    
    def giveRaise(self, employee_fname, employee_lname, raisePercent):
        for employee in self.teamList:
            if employee.fname == employee_fname and employee.lname == employee_lname:
                employee.salary += employee.salary * raisePercent
                print(employee.fname + " " + employee.lname + " received a raise of " + str(raisePercent * 100) + "%")
        print("Employee not found")
        print("Please check the spelling of the first and last name")
        
    #Given a project name and a number of employees assingn the project to a random employee in the team list but 
    #always give priority to the employee with the most years employed and the least amount of projects
    def assignProject(self, project="Default Project", numEmployees=1):
        if numEmployees > len(self.teamList):
            print("Not enough employees")
            return
        for i in range(numEmployees):
            employee = self.teamList[0]
            for emp in self.teamList:
                if emp.yearsEmployed > employee.yearsEmployed and len(emp.projects) < len(employee.projects):
                    employee = emp
            employee.projects.append(project)
            print(employee.fname + " " + employee.lname + " has been assigned to " + project)
            self.teamList.remove(employee)
    