students = {
    "Alice": [85, 90, 78, 92],
    "Bob": [60, 65, 70, 75],
    "Charlie": [40, 45, 50, 55],
    "David": [95, 100, 98, 92]
}

# Function to calculate average grade
def average_grade(grades):
    return sum(grades) / len(grades)

# Find average for each student
averages = {name: average_grade(grades) for name, grades in students.items()}

# Find student with highest average
highest_avg_student = max(averages, key=averages.get)

# Count students who passed
passed_students = sum(1 for avg in averages.values() if avg >= 50)

# Output results
print("Dictionary of students and their grades:", students)
print("Average grade for Bob:", averages["Bob"])
print("Student with the highest average grade:", highest_avg_student)
print("Number of students who passed:", passed_students)
