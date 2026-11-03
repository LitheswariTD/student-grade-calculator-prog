#student mark percentage and grade
name = input("Enter student name: ")
n=int(input("Enter number of subjects: "))
total=0
for i in range(1,n+1):
    mark=float(input("Enter marks for subject {}: ".format(i)))
    total += mark

percentage = (total / (n * 100)) * 100

if percentage >= 90:
    grade = 'A+'
    performance='outstanding'
elif percentage >= 80:
    grade = 'A'
    performance = "Excellent"
elif percentage >= 70:
    grade = 'B'
    performance = "very good"
elif percentage >= 60:
    grade = 'C'
    performance = "good"
elif percentage >= 50:
    grade = 'D'
    performance = "average"
else:
    grade = 'F'
    performance = "needs improvement"

print("---ACADEMIC PERFORMANCE---")
print("Student Name:", name)
print("Total Marks:",total)
print("Percentage: ",round(percentage, 2))
print("grade:",grade)
print("Performance:",performance)