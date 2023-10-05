import datetime
import sqlite3
class Employee():
    def __init__(self, fname, lname, age, salary, yearHired=None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary
        self.yearsEmployed = 0
        self.projects = []
        
        if yearHired == None:
            self.yearHired = datetime.date.today()
        else:
            self.yearHired = yearHired
            self.yearsEmployed = datetime.date.today().year - self.yearHired
        
    def updateYearsEmployed(self):
        self.yearsEmployed = datetime.date.today().year - self.yearHired.year
        
    def updateAge(self):
        self.age += self.yearsEmployed
        
    def isManager(self):
        return False
                
    def __str__(self):
        return self.fname + " " + self.lname + " " + str(self.age) + " " + str(self.salary) + " " + str(self.yearsEmployed)
    

class Manager(Employee):
    def __init__(self, fname, lname, age, salary, yearHired=None):
        super().__init__(fname, lname, age, salary, yearHired)
        self.teamList = []
        self.companyName = ""
          
    def addToTeam(self, employee):
        self.teamList.append(employee)
        
    def removeFromTeam(self, employee):
        self.teamList.remove(employee)
        
    def isManager(self):
        return True
    
    #create the team list and store it in the company database (companyName_database.db) for the manager
    def updateTeam(self):
        companyDB = sqlite3.connect(self.companyName+'_database.db')
        cursor = companyDB.cursor()
        cursor.execute("SELECT * FROM managers WHERE manager='True'")
        manager = cursor.fetchone()
        manager = Manager(manager[0].split()[0], manager[0].split()[1], manager[1], manager[2], manager[3])
        manager.teamList = self.teamList
        #create a new var and iterate over team list to make one string and remove comma on the last name
        tList = ""
        for employee in manager.teamList:
            tList += employee.fname + " " + employee.lname + ", "
        tList = tList[:-2]
        cursor.execute("UPDATE managers SET teamList='"+tList+"' WHERE name='"+manager.fname+" "+manager.lname+"'")
        companyDB.commit()
        cursor.close()
    
    def setcompanyName(self, companyName):
        self.companyName = companyName
        
    #find the employee in the company database (companyName_database.db) and give them a raise  
    def giveRaise(self, employee_fname, employee_lname, raisePercent, companyName):
        companyDB = sqlite3.connect(companyName+'_database.db')
        cursor = companyDB.cursor()
        cursor.execute("SELECT * FROM employees WHERE name='"+employee_fname+" "+employee_lname+"'")
        employee = cursor.fetchone()
        if employee == None:
            print("Employee not found or is a manager")
            return
        employee = Employee(employee[0].split()[0], employee[0].split()[1], employee[1], employee[2], employee[3])
        employee.salary += employee.salary * (raisePercent/100)
        cursor.execute("UPDATE employees SET salary="+str(employee.salary)+" WHERE name='"+employee_fname+" "+employee_lname+"'")
        companyDB.commit()
        cursor.close()
        
    #given a project name and number of employees, assign the project to the employees in the company database (companyName_database.db)
    #always assign the employee with the most years worked and least number of projects first
    def assignProject(self, project="Default Project", numEmployees=1):
        companyDB = sqlite3.connect(self.companyName+'_database.db')
        cursor = companyDB.cursor()
        cursor.execute("SELECT * FROM employees WHERE manager='False' ORDER BY yearsEmployed DESC, projects ASC")
        employees = cursor.fetchmany(numEmployees)
        for employee in employees:
            employee = Employee(employee[0].split()[0], employee[0].split()[1], employee[1], employee[2], employee[3])
            employee.projects.append(project)
            cursor.execute("UPDATE employees SET projects='"+employee.projects[0]+"' WHERE name='"+employee.fname+" "+employee.lname+"'")
        companyDB.commit()
        cursor.close()
    