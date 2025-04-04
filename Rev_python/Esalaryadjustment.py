employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
# Define a function to calculate the average salary of employees with a certain rating
  
adjust_salary = lambda emp: {
    "name": emp["name"],
    "salary":
        emp["salary"]*(
            0.1 if emp["rating"] == 4 or 5
            else 0.05 if emp["rating"] == 3
            else 0.01
        ), "rating": emp["rating"]
}

updated_salaries = list(map(adjust_salary, employees))
print(updated_salaries)