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
    
def calculate_balance(transactions):
    balance = 0

    for transaction in transactions:
        if transaction["status"] == "active":
            if transaction["type"] == "credit":
                balance += transaction["amount"]
            else:
                balance -= transaction["amount"]

    return balance