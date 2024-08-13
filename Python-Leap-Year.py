def check_leap_year(user_year):
    if (user_year %4==0 and user_year % 100 !=0) or (user_year %400 ==0):
        return True
    else:
        return False

user_year = int(input("Enter a year: "))
if check_leap_year(user_year) == True:
    print("Its Learp Years")
else:
    print("Its not leap years")
