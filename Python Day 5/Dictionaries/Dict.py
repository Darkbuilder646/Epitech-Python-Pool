#Task_01
student = {"name": "Paul",
           "academic_year": "2022"}

#Task_02
"""
name => Web Development / Network and System Administration / Java
credit => +int
grade => A to E
"""
student["units"] = {"name": "Java",
                    "credits": 1,
                    "grades": "A"}

#Task_03
grade_weight_mapping = {"A": 4,
                        "B": 3,
                        "C": 2,
                        "D": 1,
                        "E": 0}

totalCredit = 0
if 'units' in student and 'credits' in student['units']:
    credits = student['units']['credits']
    totalCredit = credits
    
student["total_credit"] = totalCredit
print(student)