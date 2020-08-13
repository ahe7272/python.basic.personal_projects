last_semester_gradebook = [("Math", 90), ("Korean", 75), ("Art", 87), ("Science", 89)]

subjects = ["Physics", "History", "English", "Geology"]
grades = [98, 97, 85, 88]
subjects.append("Computer science")
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(("Visual arts", 93))
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)