def percentage_to_letter(score=0):
    grade = "N/A"
    if score < 60:

        grade = "D"
    if score >= 70:
        grade = "C"
    if score >= 80:
        grade = "B"
    if score >= 90:
        grade = "A"
    if grade < 60:
        grade = "F"
    return grade


number_grade = int(input("Please enter your grade as a percentage:"))
grade = percentage_to_letter(number_grade)
print(grade)
