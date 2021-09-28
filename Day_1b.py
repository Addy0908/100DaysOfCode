# How many days are left to die

age=int(input("Enter your age: "))
years_remaining = 90- age
days_remaining = years_remaining *365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12

message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left in your hand so work hard and enjoy your life to the fullest "
print(message)