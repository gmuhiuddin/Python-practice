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

# number_list = [33, 23, 24, 55, 12]
# highest_num = 0

# for num in number_list:
#     if type(number_list[0]) != int : break

#     if highest_num < num:
#         highest_num = num

# print(highest_num)

# lowest_num = number_list[0]

# for num in number_list:
#     if type(number_list[0]) != int : break

#     if lowest_num > num:
#         lowest_num = num

# print(lowest_num)

# def start_quiz ():

#     quiz_data = [
#         {
#             "question": "What is the capital of France?",
#             "options": ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],
#             "answer": "C"
#         },
#         {
#             "question": "Which programming language is known as the language of AI?",
#             "options": ["A) Python", "B) Java", "C) C++", "D) Ruby"],
#             "answer": "A"
#         },
#         {
#             "question": "What is the smallest planet in our solar system?",
#             "options": ["A) Earth", "B) Mars", "C) Mercury", "D) Venus"],
#             "answer": "C"
#         }
#     ]

#     # in enumerate second argement is val number is starts with
#     total_score = 0
    
#     print("Welcome to the Quiz Game!")
#     print("-" * 40)
    
#     for i, val in enumerate(quiz_data, 1):
        
#         print(f"Q({i}): {val["question"]}")
#         print("options:")

#         for opt in val["options"]:
#             print(opt)
        
#         user_input = input("Please add your answer in A/B/C/D: ").upper()

#         if(val["answer"] == user_input):
#             total_score += 10

#     print(f"Total of {total_score}/{len(quiz_data)*10}")

# start_quiz()

def print_some_thing(txt, *args):
    print(txt, args)

def remove_value_from_txt(txt="", removing_value=" "):
    # function outline
    """
    the take two arguments one was txt second one was removeing value
    """
    
    if removing_value not in txt:
        return "removeing value not found"
        
    value = txt.replace(removing_value, "")
    return value

def remove_value_from_txt_and_add_value(txt="", removing_value=" ", adding_value=""):
    # function outline
    """
    the take there arguments one was txt second one was removeing value third one is adding value
    """
    
    if removing_value not in txt:
        return "removeing value not found"
        
    value = txt.replace(removing_value, adding_value)
    return value

    
# print_some_thing("Ghulam muhiudddin", "Asd")

# a = 1

# while 10 >= a:
#     print("Ghulam muhiuddin")
#     a+=1

import random as rd

def generateUniqueAccNo (allAccNo):
    acc_no = 000000000

    if len(allAccNo):
        acc_no = allAccNo[0]
    else:
        allAccNo.append(000000000)

    while acc_no in allAccNo:
        acc_no = ""
        for i in range(9):
            random_no = str(rd.randint(0, 9))
            acc_no += random_no
    
    return acc_no

def apna_bank():
    try:
        banking_file=open("banking_file.txt", "r")
        file_content_str = banking_file.read() or "[]"
        file_d = eval(file_content_str)
        
        first_response = input("""
Hey, how may I help you:
press 1: for account opening
press 2: for checking account balance
press 3: for send money: """)

        if not first_response.isdigit():
            return print("Please enter only digit")

        first_response = int(first_response)

        # It`s my own logic for checking reponse was an string or not
        
        # for num in first_response:
        #     if num not in "1234567890":
        #         break
        # else:
        #     first_response = int(first_response)

        # if type(first_response) == str:
        #     return print("Please enter number")
        
        if first_response not in range(1, 4):
            return print("Please enter dedicated option")
    
        if first_response == 1:
            acc_title = input("Please enter your account title")
            acc_cnic = input("Please enter your cnic")

            if len(acc_cnic) < 13 or not acc_cnic.isdigit():
                return print("Cnic must be 13 characters" if len(acc_cnic) < 13 else "Cnic must be in numbers")

            allAccNo = []
            
            for acc in file_d:
                allAccNo.append(acc["accNo"])

            acc_no = generateUniqueAccNo(allAccNo)
            
            file_d.append({
                "name": acc_title,
                "cnic": acc_cnic,
                "accNo": acc_no,
                "balance": 0
            })
            
            banking_file=open("banking_file.txt", "w")
            banking_file.write(f"{file_d}")

            print("Congrates your account was created in apna bank")
            
        elif first_response == 2:
            acc_no = input("Please enter your account")
            account = {}
    
            for acc in file_d:
                if acc["accNo"] == acc_no:
                    account = acc
                    break

            if len(account) > 0:
                print(f"Your account balance is {account.get("balance")}")
            else:
                print(f"Account not found is this account no: {acc_no}")
                    
        elif first_response == 3:
            user_acc_no = input("Please enter your account no: ")
            account = {}
    
            for acc in file_d:
                if acc["accNo"] == user_acc_no:
                    account = acc
                    break

            if len(account) > 0:
                receiver_acc_no = input("Please enter receiver account no: ")

                receiver_account = {}

                for acc in file_d:
                    if acc["accNo"] != user_acc_no and acc["accNo"] == receiver_acc_no:
                        receiver_account = acc
                        break

                if len(receiver_account) > 0:
                    amount = float(input("Please enter a amount"))

                    if account["balance"] >= amount:
                        sender_acc_index = file_d.index(account)
                        
                        file_d[sender_acc_index]["balance"] -= amount
                        
                        receiver_acc_index = file_d.index(receiver_account)
                        
                        file_d[receiver_acc_index]["balance"] += amount
                        
                        banking_file=open("banking_file.txt", "w")
                        
                        banking_file.write(f"{file_d}")

                        print("Amount was sended successfully")
                    else:
                        print("You don`t have sufficient balance")
                else:
                    print(f"Receiver account not found is this account no: {receiver_acc_no}")
            else:
                print(f"Account not found is this account no: {user_acc_no}")

    except Exception as error:
        print("error: ", error, sep="")
    else:
        print("Thanks for contacting apna bank")
    finally:
        banking_file.close()

# apna_bank()

# Object Oriented Programming (OOP)

# Classes

# 1. Class is a blueprint of object

# First we create a class

# Normal Class

# class Car ():
#     model = "civic"
#     make = 2009
#     company = "Honda"

# car1 = Car()

# print(car1.model)

# Class with initilizer: like we assign a dynamically values

# class Car ():
#     def __init__(self, company, model, make):
#         self.company = company
#         self.model = model
#         self.make = make

# car1 = Car("honda", "city", 2009)

# print(car1.model)

def calculate_balance(transactions):
    balance = 0

    for transaction in transactions:
        if transaction["status"] == "active":
            if transaction["type"] == "credit":
                balance += transaction["amount"]
            else:
                balance -= transaction["amount"]

    return balance

def apna_bank_with_transaction():
    try:
        banking_file=open("banking_file_transactions.txt", "r")
        file_content_str = banking_file.read() or "[]"
        file_d = eval(file_content_str)
        
        first_response = input("""
Hey, how may I help you:
press 1: for account opening
press 2: for checking account balance
press 3: for send money:
press 4: for transactions history: """)

        if not first_response.isdigit():
            return print("Please enter only digit")

        first_response = int(first_response)

        # It`s my own logic for checking reponse was an string or not
        
        # for num in first_response:
        #     if num not in "1234567890":
        #         break
        # else:
        #     first_response = int(first_response)

        # if type(first_response) == str:
        #     return print("Please enter number")
        
        if first_response not in range(1, 5):
            return print("Please enter dedicated option")
    
        if first_response == 1:
            acc_title = input("Please enter your account title")
            acc_cnic = input("Please enter your cnic")

            if len(acc_cnic) < 13 or not acc_cnic.isdigit():
                return print("Cnic must be 13 characters" if len(acc_cnic) < 13 else "Cnic must be in numbers")

            allAccNo = []
            
            for acc in file_d:
                allAccNo.append(acc["accNo"])

            acc_no = generateUniqueAccNo(allAccNo)
            
            file_d.append({
                "name": acc_title,
                "cnic": acc_cnic,
                "accNo": acc_no,
                "transactions": "[]"
            })
            
            banking_file=open("banking_file_transactions.txt", "w")
            banking_file.write(f"{file_d}")

            print("Congrates your account was created in apna bank")
            
        elif first_response == 2:
            acc_no = input("Please enter your account")
            account = {}
    
            for acc in file_d:
                if acc["accNo"] == acc_no:
                    account = acc
                    break

            acc_balance = calculate_balance(eval(account.get("transactions")))

            if len(account) > 0:
                print(f"Your account balance is {acc_balance}")
            else:
                print(f"Account not found is this account no: {acc_no}")
                    
        elif first_response == 3:
            user_acc_no = input("Please enter your account no: ")
            account = {}
    
            for acc in file_d:
                if acc["accNo"] == user_acc_no:
                    account = acc
                    break

            if len(account) > 0:
                receiver_acc_no = input("Please enter receiver account no: ")

                receiver_account = {}

                for acc in file_d:
                    if acc["accNo"] != user_acc_no and acc["accNo"] == receiver_acc_no:
                        receiver_account = acc
                        break

                if len(receiver_account) > 0:
                    amount = float(input("Please enter a amount"))

                    acc_balance = calculate_balance(eval(account.get("transactions")))

                    if acc_balance >= amount:
                        sender_acc_index = file_d.index(account)
                        
                        sender_acc_transactions = eval(file_d[sender_acc_index]["transactions"])

                        sender_acc_transactions.append({
                            "amount": amount,
                            "type": "debit",
                            "status": "active"
                        })

                        file_d[sender_acc_index]["transactions"] = f"{sender_acc_transactions}"
                        
                        receiver_acc_index = file_d.index(receiver_account)
                        
                        receiver_acc_transactions = eval(file_d[receiver_acc_index]["transactions"])

                        receiver_acc_transactions.append({
                            "amount": amount,
                            "type": "credit",
                            "status": "active"
                        })

                        file_d[receiver_acc_index]["transactions"] = f"{receiver_acc_transactions}"
                        
                        banking_file=open("banking_file_transactions.txt", "w")
                        
                        banking_file.write(f"{file_d}")

                        print("Amount was sended successfully")
                    else:
                        print("You don`t have sufficient balance")
                else:
                    print(f"Receiver account not found is this account no: {receiver_acc_no}")
            else:
                print(f"Account not found is this account no: {user_acc_no}")
        
        elif first_response == 4:
            user_acc_no = input("Please enter your account no: ")
            account = {}
    
            for acc in file_d:
                if acc["accNo"] == user_acc_no:
                    account = acc
                    break

            if len(account) > 0:
                account_transactions = eval(account["transactions"])
                acc_balance = calculate_balance(account_transactions)

                print("  Your transactions history  ")
                print("-"*29)
                for transaction in account_transactions:
                    print(f"type: {transaction["type"]} | {transaction["status"]} | {transaction["amount"]}")
                print(f"Active Balance: {acc_balance}")
            else:
                print(f"Account not found is this account no: {user_acc_no}")

    except Exception as error:
        print("error: ", error, sep="")
    else:
        print("Thanks for contacting apna bank")
    finally:
        banking_file.close()

# apna_bank_with_transaction()

class Person:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"name: {self.__name}"

p1 = Person("Ghulam muhiuddin")

# print(p1)

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.__roll_no = roll_no
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_roll_no(self):
        return self.__roll_no
    
    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

s1 = Student("Ghulam muhiuddin", 333451)

print(s1)
