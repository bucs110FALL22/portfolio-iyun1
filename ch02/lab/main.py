import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week ($):", cost_per_week)
classes_per_week=3
cost_per_class=(cost_per_week/classes_per_week)
print("Cost Per Class ($):", cost_per_class)
#Part B
random_list=["Explosion", "5248964", "Wyoming", "-0", "E-Grade"]
print ("Random List Choice:", random.choice(random_list))