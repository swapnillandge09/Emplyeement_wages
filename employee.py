print("Welcome to Employee Wage Computation on Master Branch")

import random
# UC1: Check Employee Attendance
attendance = random.choice([0, 1])
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")
    
#uc2 : daily Wages
wage_per_hour = 20
full_day_hour = 8
daily_wage = wage_per_hour * full_day_hour
print(f"Daily Employee Wage: {daily_wage}")

# UC3: Part-Time Employee Wage
part_time_hour = 4
part_time_wage = wage_per_hour * part_time_hour
print(f"Part-time Employee Wage: {part_time_wage}")
