print("Welcome to Employee Wage Computation on Master Branch")

import random
# UC1:
attendance = random.choice([0, 1])
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")
    
#uc2 : 
wage_per_hour = 20
full_day_hour = 8
daily_wage = wage_per_hour * full_day_hour
print(f"Daily Employee Wage: {daily_wage}")

# UC3: 
part_time_hour = 4
part_time_wage = wage_per_hour * part_time_hour
print(f"Part-time Employee Wage: {part_time_wage}")

# UC4:
def employee_wage(employee_type):
    switcher = {
        1: full_day_hour * wage_per_hour,  
        2: part_time_hour * wage_per_hour  
    }
    return switcher.get(employee_type, 0)  
employee_type = random.choice([0, 1, 2])  
print(f"Employee Wage (Switch Case): {employee_wage(employee_type)}")

# UC5:
working_days_per_month = 20
monthly_wage = working_days_per_month * daily_wage
print(f"Monthly Employee Wage: {monthly_wage}")

