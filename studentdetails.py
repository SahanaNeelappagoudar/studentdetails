# Student Grade Calculator (No User Input)

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"


# Predefined student details
student = {
    "name": "Sahana",
    "department": "Computer Science",
    "semester": 5,
    "marks": [85, 90, 88]
}

# Calculate average
average = sum(student["marks"]) / len(student["marks"])

# Assign grade
grade = calculate_grade(average)

# Display result
print("--- Student Result ---")
print("Name:", student["name"])
print("Department:", student["department"])
print("Semester:", student["semester"])
print("Marks:", student["marks"])
print("Average Marks:", round(average, 2))
print("Grade:", grade)

