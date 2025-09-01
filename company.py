from employees import Employee, SalaryEmployee, HourlyEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(f"{emp.fname} {emp.lname}: ${emp.salary}")

    def pay_employees(self):
        print("Paying employees...")

        for i in self.employees:
            print(f"Paying : {i.fname} {i.lname}")
            print(f"Amount : ${i.calculate_paycheck():,.2f}")

def main():
    company = Company()
    emp1 = SalaryEmployee("John", "Doe", 52000)
    emp2 = HourlyEmployee("Jane", "Smith", 40, 15)

    company.add_employee(emp1)
    company.add_employee(emp2)
    company.display_employees()
    company.pay_employees()

main()