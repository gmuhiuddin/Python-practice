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