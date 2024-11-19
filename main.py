# print("bla bla bla")

# txts = "gmuhiuddin"

# for txt in txts: 
#     print(txt)

# Python data types

# 1. "" => str
# 2. 1 => int
# 3. 1.2 => float
# 4. True / False => bool

# txtsList = ["txt1", "txt2"]

# print(txtsList)

# print(txtsList.index("txt2"))

# print(txtsList)

# if False:
#     print("true")
# else:
#     print("false")

# Getting lowest num

# numList = [34, 24, 56, 52]
# lowestNum = numList[0]

# for num in numList:
#     if num < lowestNum:
#         lowestNum = num

# print("Lowest num", lowestNum)

# Getting highest num

# numList = [34, 24, 56, 52]
# highestNum = 0

# for num in numList:
#     if num > highestNum:
#         highestNum = num

# print("Highest num", highestNum)

# Python collections

# - list
# - dictionary
# - tuple
# - set

# List

students = ['bilal', "asad", "adnan", "nasir"]

students.append("Ghulam muhiuddin")

students.insert(6, "owais")

students_2 = ["ali", "ahmed"]

students.extend(students_2)

# create a combined copy of a lists

new_students_list = students_2 + students

print(students)

# Return index of argument

print(students.index("ali"))

# Nothing return anything

students.remove("Ghulam muhiuddin")

# Return popped value

print(students.pop(-2))

print(students)

# Remove list all values

students.clear()

print(students)

# print(10 + 2 * 2 - 4 // 8)

# Dictionary

student = {
    "name": "Ghulam muhiuddin",
    "age": 15,
    "course": "AI and Data Science"
}

student["email"] = "muhiuddinghulam825@gmail.com"

student_details = {
    "education": "Matric"
}

# Joining two dictionary

student.update(student_details)

# Delete a key and value pair by giving key

student.pop("email")

print(student)

# Very important concept
# Pass by value | Pass by refrence
# like if I create a one variable of list and assigning a second variable same variable the pass by refrence if I change value of first variable automatically second value was changed this was called pass by refrence for example:

list1 = ["ali", "ahmed", "bilal"]
list2 = list1

list1.append("nasir")

print("List1", list1, sep=" ")
print("List2", list2, sep=" ")

# And Pass by value example: 

list1 = ["ali", "ahmed", "bilal"]
list2 = list1.copy() # It will change a id (refrence) of list

list1.append("nasir")

print("List1", list1, sep=" ")
print("List2", list2, sep=" ")