from datetime import date

user_input = input('enter user(male/female) : ')

if user_input == 'male':
    reqired_age = 22
    reqired_height = 165
elif user_input == 'female':
    reqired_age = 20
    reqired_height = 150
else :
    print('envalid user')

day = int(input('enter birth day :'))
month = int(input('enter birth month :'))
year = int(input('enter birth year :'))

today = date.today()
dob = date(year,month,day)

age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

user_height = float(input('enter your height : '))
user_unit = input('enter height unit (cm/inch/foot) : ')


if user_unit == 'cm':
    user_cm = user_height
    user_foot = user_height*0.0328084
    user_inch = user_height*0.3937008
elif user_unit == 'inch':
    user_cm = user_height*2.54
    user_foot = user_height*0.08
    user_inch = user_height
elif user_unit == 'foot':
    user_cm = user_height*30.48
    user_foot = user_height
    user_inch = user_height*12
else:
    print('envalid height unit :')

print(user_cm)
print(user_foot)
print(user_inch)

if (age)< int(reqired_age):
    print(f"Not Eligible  (Reason: Age is low → {reqired_age}, Required → {reqired_age})")

elif user_cm< reqired_height:
    print("Not Eligible  (Reason: Height is low)")

else:
    print(f"Eligible  (Age: {age}, Height: {round(user_cm, 1)} cm)")