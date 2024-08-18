## Email Slicer by Nilesh HCF02PYAUG1025

email_id = input("Enter your Email ID: ")

## Extract the username and domain and display the result

try:
    user_name, user_domain = email_id.split('@')
    print(f"\nYour Username is: \n{user_name} \nDomain is: \n{user_domain}")
except ValueError:
    print("Invalid Email Format try entering a valid email !!")
