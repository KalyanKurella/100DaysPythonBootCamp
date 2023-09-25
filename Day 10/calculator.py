import os
def add(n1, n2):
    return n1+n2
def substract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
flag = True
while(flag):
    first_num = int(input("Enter the first number : "))
    second_num = int(input("Enter the second number : "))
    dict = {
        "add":add(first_num,second_num),
        "substract" : substract(first_num,second_num), 
        "multiply":multiply(first_num,second_num), 
        "divide":divide(first_num,second_num)
    }
    op = input("Enter the operation type '+ ', '- ' , '* ' ,'/ ','exit' : ")
    if(op == "+"):
        print(dict["add"])
    elif op=="-":
        print(dict["substract"])
    elif(op=="*"):
        print(dict["multiply"])
    elif(op == "/"):
        print(dict["divide"])
    else :
        break
    check = input("Y to continue....N to exit").lower()
    if check == "y":
        flag = True
    elif check == "n":
        flag == False
    else:
        pass
    os.system('cls')