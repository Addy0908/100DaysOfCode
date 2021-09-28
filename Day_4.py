#Banker Rouletter- Who will pay the bill
import random
#split string method
names1 = input("Give me everybodys names:-")
names= names1.split(", ") 
num_items = len(names)

random_choice =random.randint(0, num_items-1)
person_who_will_pay_the_bill = names[random_choice]
print(person_who_will_pay_the_bill + " is going to pay the bill today")
