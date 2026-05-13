# Employee Performance Evaluation System

print("Employee Performance Evaluation System")

# Input details
name = input("Enter Employee Name: ")
attendance = int(input("Attendance Percentage: "))
project = int(input("Project Completion Score (0-100): "))
communication = int(input("Communication Skill Score (0-100): "))
teamwork = int(input("Teamwork Score (0-100): "))

# Initial score
score = 0

# Attendance criteria
if attendance >= 90:
    score += 20

elif attendance >= 75:
    score += 10

# Project criteria
if project >= 85:
    score += 30

elif project >= 70:
    score += 20

else:
    score += 10

# Communication criteria
if communication >= 80:
    score += 20

elif communication >= 60:
    score += 10

# Teamwork criteria
if teamwork >= 80:
    score += 20

elif teamwork >= 60:
    score += 10

# Dependent condition
if project >= 85 and teamwork >= 80:
    score += 10

# Penalty for low attendance
if attendance < 60:
    score -= 10

# Final Result
if score >= 80:
    performance = "Excellent"

elif score >= 60:
    performance = "Good"

elif score >= 40:
    performance = "Average"

else:
    performance = "Poor"

# Display result
print("\nEmployee Name:", name)
print("Total Score:", score)
print("Performance:", performance)