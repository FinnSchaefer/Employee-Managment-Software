from company import Company as comp
from employee import Employee as emp
from employee import Manager as mng

#Create a company
company = comp("1234 Main St", "Technology", "Company 1")

#Create some employees
employee1 = emp("John", "Smith", 25, 50000)
employee2 = emp("Jane", "Doe", 30, 60000, 2020)

#Add the employees to the company
company.addEmployee(employee1)
company.addEmployee(employee2)

#Create a manager
manager1 = mng("Bob", "Smith", 35, 70000)
manager1.setcompanyName("Company 1")

#Add the manager to the company
company.addEmployee(manager1)

#Give the manager a raise
manager1.giveRaise("Bob", "Smith", 10, "Company 1")
manager1.giveRaise("John", "Smith", 10, "Company 1")

#Assign a project to the employee
manager1.assignProject("Project 1", 1)

#Update the manager's team list
manager1.addToTeam(employee1)
manager1.addToTeam(employee2)
manager1.updateTeam()

