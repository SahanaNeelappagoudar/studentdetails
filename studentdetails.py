import sys

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

def main():
    if len(sys.argv) < 6:
        print("Usage: python student.py <name> <dept> <sem> <m1> <m2> <m3>")
        print("Example: python student.py Sahana CSE 5 90 85 88")
        return

    name = sys.argv[1]
    dept = sys.argv[2]
    sem = sys.argv[3]

    try:
        m1 = float(sys.argv[4])
        m2 = float(sys.argv[5])
        m3 = float(sys.argv[6])
    except ValueError:
        print("Error: Marks must be numbers.")
        return

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("---- Student Result ----")
    print("Name:", name)
    print("Department:", dept)
    print("Semester:", sem)
    print("Average:", avg)
    print("Grade:", grade)

if __name__ == "__main__":
    main()