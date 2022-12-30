#required_age_at_school
usama_age=3
school_required_age=5
if usama_age==school_required_age:
     print("usama go to school")
else:
     print("Age is not complete for joining school")




usama_age=input("what is usama age? ")
school_required_age=5
usama_age=int(usama_age)
print(type(usama_age))
if usama_age == school_required_age:
    print("Usama has join the School")
elif usama_age>school_required_age:
    print("Usama should join higher secoundary School")
elif usama_age <= 2:
    print("Usama is still a baby")
else:
    print("Age is not complete for joining School")