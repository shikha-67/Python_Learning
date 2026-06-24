one=int(input("Enter your hostel/flat rent: "))
food=int(input("Enter amount for food ordered: "))
ele_spent=int(input("Enter total of electricity spent: "))
per=int(input("Enter the charge per unit: "))
person=int(input("Enter number of person living in the room: "))

total_electricity_cost=ele_spent*per
x=(one+food+total_electricity_cost)/person
print(f"Each person will pay: {x}Rs ")