import sqlite3
import employee as emp
class Company():
    def __init__(self, address, field, name="Default Company"):
        self.name = name
        self.address = address
        self.field = field
        self.companyDB = sqlite3.connect(name+'_database.db')
       
        cursor = self.companyDB.cursor()
        cursor.execute('''CREATE TABLE employees
                     (name text, age integer, salary real, yearsEmployed integer, projects text, manager text)''')
        cursor.execute('''CREATE TABLE managers
                     (name text, age integer, salary real, yearsEmployed integer, teamList text, manager text)''')
        self.companyDB.commit()
        cursor.close()
        
    def __str__(self):
        return self.name + " " + self.address + " " + self.field
    
    #add an employee to the database and check if they are a manager or not
    def addEmployee(self, employee):
        cursor = self.companyDB.cursor()
        if employee.isManager():
            cursor.execute("INSERT INTO managers VALUES ('"+employee.fname+" "+employee.lname+"', "+str(employee.age)+", "+str(employee.salary)+", "+str(employee.yearsEmployed)+", '"+str(employee.projects)+"', 'True')")
        else:
            cursor.execute("INSERT INTO employees VALUES ('"+employee.fname+" "+employee.lname+"', "+str(employee.age)+", "+str(employee.salary)+", "+str(employee.yearsEmployed)+", '"+str(employee.projects)+"', 'False')")
        self.companyDB.commit()
        cursor.close()
        