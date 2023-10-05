import sqlite3
class Company():
    def __init__(self, name, address, field):
        self.name = name
        self.address = address
        self.field = field
        self.companyDB = sqlite3.connect(name+'_database.db')
       
        cursor = self.companyDB.cursor()
        cursor.execute('''CREATE TABLE employees
                     (name text, age integer, salary real, yearsEmployed integer, projects text, manager text)''')
        self.companyDB.commit()
        cursor.close()
        
    def __str__(self):
        return self.name + " " + self.address + " " + self.field
    
        