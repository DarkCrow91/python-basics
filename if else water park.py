print("welcome to the rolercoaster")
height=int(input("what is your height ? = "))
bill=0
if height >=125:
    print("you can enter the ride")
    age=int(input("what is your age = "))
    if age<=12:
        print("child ticket is = 50rs\t")
        bill=50
    elif age <=18:
        print(" youth ticket is 75")
        bill=75
    elif age>=45 and age<=55:
        print("everything will be great , bills on us")
    else:
        print("adult ticket is = 100rs")
        bill=100
    

    wants_photo=input("do you want the photo take ? type Y for yes and N for no=").lower()
    if wants_photo=="y":
        bill += 15
    
    print(f"your final bill is {bill}")
else:
    print("sorry , you can't enjoy the ride")