myage = input("Enter your age : ")

age = int(myage)
if age >= 18:
    print("You are an adult.")
    print("You can vote.")
elif age < 18 and age > 3:
    print("You should be in school.")
else :
    print("You are a child.")
print("Thank you")