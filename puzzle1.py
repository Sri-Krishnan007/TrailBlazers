import pandas as pd
employee_file = r'C:\Users\linux.WINSERVER\Desktop\Trailblazers\Puzzle1\DepartmentData.csv'
department_file = r'C:\Users\linux.WINSERVER\Desktop\Trailblazers\Puzzle1\EmployeeData.csv'
employee_data = pd.read_csv(employee_file)
department_data = pd.read_csv(department_file)

merged_data = pd.merge(employee_data, department_data, how='left', on='department_id')
# Calculate total salary after tax
merged_data['total_salary_after_tax'] = (merged_data['bonus'].fillna(0) + merged_data['base_salary'].fillna(0)) * (1 - merged_data['tax_rate'].fillna(0))

average_salaries = merged_data.groupby('department_name')['total_salary_after_tax'].mean().reset_index()

sorted_departments = average_salaries.sort_values(by='total_salary_after_tax', ascending=False)

top_departments = sorted_departments.head(10)

clue = ''.join(top_departments['department_name'].str[0])

print("Sorted Departments by Average Salary:")
print(sorted_departments)
print(f"Scooby's clue from top departments: {clue}")