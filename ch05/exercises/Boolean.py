def percentage_to_letter(score=0):
    grade = "F"
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    return grade


def is_passing(grade):
  return grade in "ABC"


number_grade = int(input("Please enter your grade as a percentage:"))
grade = percentage_to_letter(number_grade)
print(grade)
passing = is_passing(grade)
print(passing)
