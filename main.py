# # print("bla bla bla")

# # txts = "gmuhiuddin"

# # for txt in txts: 
# #     print(txt)

# # Python data types

# # 1. "" => str
# # 2. 1 => int
# # 3. 1.2 => float
# # 4. True / False => bool

# # txtsList = ["txt1", "txt2"]

# # print(txtsList)

# # print(txtsList.index("txt2"))

# # print(txtsList)

# # if False:
# #     print("true")
# # else:
# #     print("false")

# # Getting lowest num

# # numList = [34, 24, 56, 52]
# # lowestNum = numList[0]

# # for num in numList:
# #     if num < lowestNum:
# #         lowestNum = num

# # print("Lowest num", lowestNum)

# # Getting highest num

# # numList = [34, 24, 56, 52]
# # highestNum = 0

# # for num in numList:
# #     if num > highestNum:
# #         highestNum = num

# # print("Highest num", highestNum)

# # Python collections

# # - list
# # - dictionary
# # - tuple
# # - set

# # List

# students = ['bilal', "asad", "adnan", "nasir"]

# students.append("Ghulam muhiuddin")

# students.insert(6, "owais")

# students_2 = ["ali", "ahmed"]

# students.extend(students_2)

# # create a combined copy of a lists

# new_students_list = students_2 + students

# print(students)

# # Return index of argument

# print(students.index("ali"))

# # Nothing return anything

# students.remove("Ghulam muhiuddin")

# # Return popped value

# print(students.pop(-2))

# print(students)

# # Remove list all values

# students.clear()

# print(students)

# # print(10 + 2 * 2 - 4 // 8)

# # Dictionary

# student = {
#     "name": "Ghulam muhiuddin",
#     "age": 15,
#     "course": "AI and Data Science"
# }

# student["email"] = "muhiuddinghulam825@gmail.com"

# student_details = {
#     "education": "Matric"
# }

# # Joining two dictionary

# student.update(student_details)

# # Delete a key and value pair by giving key

# student.pop("email")

# print(student)

# # Very important concept
# # Pass by value | Pass by refrence
# # like if I create a one variable of list and assigning a second variable same variable the pass by refrence if I change value of first variable automatically second value was changed this was called pass by refrence for example:

# list1 = ["ali", "ahmed", "bilal"]
# list2 = list1

# list1.append("nasir")

# print("List1", list1, sep=" ")
# print("List2", list2, sep=" ")

# # And Pass by value example: 

# list1 = ["ali", "ahmed", "bilal"]
# list2 = list1.copy() # It will change a id (refrence) of list

# list1.append("nasir")

# print("List1", list1, sep=" ")
# print("List2", list2, sep=" ")

# tuple

# - immutable - connot be change without reassigning
# - itrable - you can get a single value

# tuple1 = (1,2,3)

# print(tuple1)

# If I create a normal variable with multiple values with comma "," the assigned as a tuple

# values = 1,2,3,4

# print(values)

# set

# set1 = {1,2,3,4}

# print(set1)

# guest_list = ("ali", "bilal", "owais", "imran")

# guest_name = input("Please add guest name").lower()

# if guest_name in guest_list:
    
#     if guest_name.startswith("a"):
#         print("You sit on a first row")
#     else:
#         print("You can sit except first row")

# else:
#     print("Your are not eligable for entering")

# or operator like js "||"

# print(False or False)

# and operator like js "&&"

# print(False and False)

# print("1" or 5)

# print("" or 5)

# print("1" and 5)

# print("" and 5)

# students_list = ({
#     "name": "Ghulam muhiuddin",
#     "age": 15,
#     "roll-no": 30001
# }, {
#     "name": "Bilal",
#     "age": 25,
#     "roll-no": 30002
# }, {
#     "name": "Ali",
#     "age": 35,
#     "roll-no": 30003
# })

# for student in students_list:
#     if student["name"].lower().startswith("a"):
#         print(student)

# name = "ghulam muhiuddin"

# print(name.capitalize())

# Destructuring or Unpacking

# name,age,rollNo = students_list[0]

# print(students_list[0][rollNo])

# Q.1 please print the dict or dict index of student_list my name "Ghulam muhiuddin"

# dict_index = -1
# name_of_student = "Ghulam muhiuddin"

# for i, student in enumerate(students_list):
#     if student["name"] == name_of_student:
#         dict_index = i
#         break

# print(dict_index)

# product_list = ({
#     "ear phones": 500
# }, {
#     "ear pods": 500
# }, {
#     "charger": 500
# })

# required_product = input("Please enter product name you want: ")

# Second way

# for i, product in enumerate(product_list):
#     if required_product in product:
#         print(f'{required_product} available')
#         break

#     if i == len(product_list)-1:
#         print(f'{required_product} not available')

# Second way

# for i, product in enumerate(product_list):
#     if required_product in product:
#         print(f'{required_product} available')
#         break
# else:
#     print(f'{required_product} not available')

# Destructuring or Unpacking

# dict_a = {
#     "name": "Ghulam muhiuddin",
#     "age": 15
# }

# for val_name,val_age in dict_a.items():
#     print(val_name, val_age)

# Not operator

# print(not False)

# computer_guessed_num = 55
# user_number = int(input("Please add number between 1 to 100: "))

# if computer_guessed_num 

# number = 5

# for num in range(10):
#     print(f"{number} x {num+1} = {number*(num+1)}")

# numbers = input("Please add number: ")
# sum = 0

# for num in numbers:
#     sum += int(num)

# print(f"Sum of your number: {sum}")

number_list = [33, 23, 24, 55, 12]
highest_num = 0

for num in number_list:
    if type(number_list[0]) != int : break

    if highest_num < num:
        highest_num = num

print(highest_num)

lowest_num = number_list[0]

for num in number_list:
    if type(number_list[0]) != int : break

    if lowest_num > num:
        lowest_num = num

print(lowest_num)