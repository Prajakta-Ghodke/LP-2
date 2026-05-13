# Employee Performance Evaluation System

print("----- Employee Performance Evaluation System -----")

# Input details
name = input("Enter Employee Name: ")

attendance = int(input("Enter Attendance Percentage: "))
project = int(input("Enter Project Completion Score (0-100): "))
communication = int(input("Enter Communication Skill Score (0-100): "))
teamwork = int(input("Enter Teamwork Score (0-100): "))

# New Criteria
leadership = int(input("Enter Leadership Skill Score (0-100): "))
punctuality = int(input("Enter Punctuality Score (0-100): "))

# Initial score
score = 0


# Attendance Criteria
if attendance >= 90:
    score += 20

elif attendance >= 75:
    score += 10

else:
    score += 5


# Project Criteria
if project >= 85:
    score += 30

elif project >= 70:
    score += 20

else:
    score += 10


# Communication Criteria
if communication >= 80:
    score += 20

elif communication >= 60:
    score += 10

else:
    score += 5


# Teamwork Criteria
if teamwork >= 80:
    score += 20

elif teamwork >= 60:
    score += 10

else:
    score += 5


# Leadership Criteria
if leadership >= 80:
    score += 20

elif leadership >= 60:
    score += 10

else:
    score += 5


# Punctuality Criteria
if punctuality >= 90:
    score += 10

elif punctuality >= 70:
    score += 5


# Dependency Conditions

# Bonus for excellent project work and teamwork
if project >= 85 and teamwork >= 80:
    score += 10
    print("\nBonus: Excellent Project-Team Coordination (+10)")


# Bonus for leadership and communication
if leadership >= 80 and communication >= 80:
    score += 10
    print("Bonus: Strong Leadership and Communication (+10)")


# Penalty for poor attendance
if attendance < 60:
    score -= 10
    print("Penalty: Low Attendance (-10)")


# Penalty for low punctuality and teamwork
if punctuality < 50 and teamwork < 50:
    score -= 5
    print("Penalty: Poor Discipline and Teamwork (-5)")


# Final Performance Evaluation
if score >= 100:
    performance = "Outstanding"

elif score >= 80:
    performance = "Excellent"

elif score >= 60:
    performance = "Good"

elif score >= 40:
    performance = "Average"

else:
    performance = "Poor"


# Display Result
print("\n----- Employee Evaluation Result -----")

print("Employee Name :", name)
print("Total Score   :", score)
print("Performance   :", performance)