# Grade Calculator
# Take marks of 5 subjects, calculate percentage and grade
# 90+ : A+, 80-89: A, 70-79: B, 60-69: C, 50-59: D, <50: F
print("Grade Calculator")
m1 = float(input("Enter the marks of subject 1:"))
m2 = float(input("Enter the marks of subject 2:"))
m3 = float(input("Enter the marks of subject 3:"))
m4 = float(input("Enter the marks of subject 4:"))
m5 = float(input("Enter the marks of subject 5:"))
total = m1 + m2 + m3 + m4 + m5
percentage = total/5

if percentage >= 90:
    print("Grade is A+")
elif percentage >= 80:
    print("Grade is A")
elif percentage >= 70:
    print("Grade is B")
elif percentage >= 60:
    print("Grade is C")
elif percentage >= 50:
    print("Grade is D")
else:
    print("Grade is F")
