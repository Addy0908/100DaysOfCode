## Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to tip Calculator")
bill=float(input("What is the total bill in $ ? "))
tip= int(input("What is the tip you will like to give-10$,12$ or 15$ ?"))
people = int(input("How many people are there to split the bill?"))
bill_with_tip= tip/100*bill + bill
print("Your bill with tip is : ",bill_with_tip)
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")