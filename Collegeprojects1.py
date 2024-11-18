
name=input("ENTER YOUR GOOD NAME:\t")

def greet(name):
    print(f"Welcome {name} ,personalized adventure guide")

def adventure():
    while True:
        destination=input("Enter the destination where do you want to go:\n\n").strip().lower()
        if destination  == "mountain":
          
            return destination
        elif destination =="beach":
            return destination
        else:
            print("you have not selected any know destination:\n\n")
def Budget():
    while True:   
        budget=int(input("ENTER OUR BUDGET:\n\n"))         
        if(budget>500):
            print("Luxury")
            return budget
        elif(budget<=200):
            print("good") 
            return budget
        elif(budget>0):
            print("budget frindly")
            return budget
        else:
            print("invalid budget")
def days():
    while True:
        try:
            day=int(input("ENTER DAYS:\n\n"))
            return day
        except ValueError:
            print("INVALID DAY! ENTER AGAIN:\n\n")

def totalCost(budget,day):
    return budget*day  
    
greet(name)
destination=adventure()
budget=Budget()
day=days()
TotalCost=totalCost(budget,day)
print(f"YOU HAVE SELECTED:{destination}\n\nBUDGET IS: {budget}\n\nDAYS:{day}\n\nTOTALCOST IS:{TotalCost}")

