number=input("enter the number?\n")
def arm_strong(number):
    sum=0
    for i in number:
        sum+=int(i)**len(number)
    return "is armstrong number" if int(number)==sum else "is not a arm strong number"
print(arm_strong(number))