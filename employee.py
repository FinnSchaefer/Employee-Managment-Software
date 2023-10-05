import datetime
class Employee():
    def __init__(self, fname, lname, age, salary, dateHired=None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary
        self.yearsEmployed = 0
        
        if dateHired == None:
            self.dateHired = datetime.date.today()
        else:
            self.dateHired = dateHired
            self.yearsEmployed = datetime.date.today().year - self.dateHired.year
        
    def giveRaise(self, percentRaise):
        self.salary += self.salary * (percentRaise / 100)
        
    def updateYearsEmployed(self):
        self.yearsEmployed = datetime.date.today().year - self.dateHired.year
          
    def fireEmployee(self):
        del self
        
    def __str__(self):
        return self.fname + " " + self.lname + " " + str(self.age) + " " + str(self.salary) + " " + str(self.yearsEmployed)
    
    