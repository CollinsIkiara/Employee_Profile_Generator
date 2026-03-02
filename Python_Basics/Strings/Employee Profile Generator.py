# In lines below, I tried to use string concatenation to create a full name and print it out together with the employee's age. I also converted the age to a string to avoid any type errors.
first_name = 'Collins'
last_name = 'Ikiara'
full_name = first_name + ' ' + last_name
employee_age = 33
print(full_name + ' is ' + str(employee_age) + ' years old')

# In lines below, I used string concatenation again to create a string that describes the employee's experience in years. I also converted the experience years to a string to avoid any type errors.
experience_years = 1
print('Experience: ' + str(experience_years) + ' years')

# In lines below, I used an f-string to create a string that describes the employee's full profile, including their name, age, position, and salary. I also formatted the salary to include a dollar sign and pipeline separators for better readability.
position = 'Backend Developer'
salary = 50000
employee_info = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_info)

# In the lines below, I implemented string slicing on the 'employee_code' to extract specific information such as the department, year joined, initials, and department number.
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(f'Department: {department}')
year_code = employee_code[4:8]
print(f'Year joined: {year_code}')
initials = employee_code[9:11]
print(f'Initials: {initials}')
department_number = employee_code[-3:]
print(f'Department Number: {department_number}')