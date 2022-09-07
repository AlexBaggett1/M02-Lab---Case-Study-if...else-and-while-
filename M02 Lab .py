
Last_Name = input("What is your last name (Type ZZZ to quit): ")

if Last_Name == "ZZZ":
    quit()

First_Name = input("What is your first name: ")

GPA = float(input("What is your GPA: "))

if GPA >= 3.2:
    print("You've made it to Honor Roll")
    
if GPA >= 3.5:
    print("You've made to the Dean's list")

