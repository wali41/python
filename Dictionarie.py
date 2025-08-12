student={
    "name":"wali",
    "age":10,
    "grade":5,
}
print (student)

#add

student["subject"]="math"
print (student)

#update
student["subject"]="english"
print (student)

#remove
student.pop("grade")
print(student)

student.clear()
print(student)




