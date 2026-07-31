first_name='Manasa'
last_name='Munnuri'
full_name=first_name +' '+ last_name
print(full_name)
address='52 Street Zaheerabad'
address+=',sangareddy'
print(address)
employee_age=22
employee_info = full_name+'is'+str(employee_age)+' years old'
print(employee_info)
experience_years = 2
experience_info = 'Experience:' + str(experience_years) + ' years'
print(experience_info)
position='ai engineer'
salary = 100000
employee_card= f'Employee: {full_name} | Age:{employee_age} | Position: {position} | Salary:{salary}'
print(employee_card)
employee_code = 'AI-2026-JD-001'
department = employee_code[0:2]
print(department)
year_code = employee_code[3:7]
print(year_code)
initials = employee_code[8:10]
print(initials)
last_three=employee_code[-3:]
print(last_three)