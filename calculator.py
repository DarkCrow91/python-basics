def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
 
# first_number=float(input("whats the first number= "))
# for symbol in operations:
#     print(symbol)
# choose_operation=input("pick an operation ")
# second_number=float(input("whats the second number= "))

# answer=operations[choose_operation](first_number,second_number)

# print(f"{first_number} {choose_operation} {second_number} = {answer}")
 
# asked_question=input(f"type 'y' to continue calculating with {answer}, or type 'n'to start a new calculation")

def calculator():

    calculation_process=True
    first_number=float(input("whats the first number= "))



    while calculation_process:
        
        for symbol in operations:
            print(symbol)
        choose_operation=input("pick an operation ")
        second_number=float(input("whats the second number= "))

        answer=operations[choose_operation](first_number,second_number)

        print(f"{first_number} {choose_operation} {second_number} = {answer}")
        
        asked_question=input(f"type 'y' to continue calculating with {answer}, or type 'n'to start a new calculation")

        if asked_question == "y":
            first_number=answer
            
        else:
            calculation_process=False    
            print("\n"*50)  
            calculator()

calculator()
