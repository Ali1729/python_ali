def create_employee(id, name, salary):
    return {"id": id, "name": name, "salary": salary}

def add_employee(employees, employee):
    employees.append(employee)

def remove_employee(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return True
    return False

def display_all_employees(employees):
    for employee in employees:
        print("Employee ID:", employee["id"])
        print("Employee Name:", employee["name"])
        print("Employee Salary:", employee["salary"])

# Usage
employees = []

employee1 = create_employee(1, "John Doe", 50000)
employee2 = create_employee(2, "Jane Doe", 60000)

add_employee(employees, employee1)
add_employee(employees, employee2)

display_all_employees(employees)

remove_employee(employees, 1)

display_all_employees(employees)
