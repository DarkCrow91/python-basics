import random

print("welcome to the password Generator")
letters=["B","c","h","t","Y","q","r"]
symbols=["!","&","#","*","+","$","@"]
numbers=["1","2","3","4","5","6","7","8","9","0"]

question_first=int(input("how many letters would you like in your password, letters\n"))
question_second=int(input("how many symbols would you like \n"))
question_third=int(input("how many numbers you would like \n"))

#easy level

#password=""
#for letter in range(0,question_first):
#    password+=random.choice(letters)

#for symbol in range(0,question_second):
#    password+=random.choice(symbols)

#for number in range(0,question_third):
#    password+=random.choice(numbers)
    
#print("your generated password is =" + password)

#hard level

 
password_list=[]
for letter in range(0,question_first):
    password_list.append(random.choice(letters))

for symbol in range(0,question_second):
    password_list.append(random.choice(symbols))

for number in range(0,question_third):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""

for char in password_list:
    password+=char

print(f"your password is :{password}")



