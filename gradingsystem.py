def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Grading System!")
    while True:
        try:
            score = float(input("Enter the student's score: "))
            if 0 <= score <= 100:
                grade = calculate_grade(score)
                print(f"The student's grade is: {grade}")
            else:
                print("Invalid score! Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

        choice = input("Do you want to calculate another grade? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the Grading System!")
            break

if __name__ == "__main__":
    main()
