#Password Validation 

# Store the user's input in the password variable.
print("Please enter your password to validate.")

# Store the user's input in the password variable.
password = input()

# Function to validate the password
def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) <= 8:
        print("Password must be at least 8 characters long.")
        return False
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    # Check if the password contains at least one special character
    special_characters = "!@#$%^&*-"
    if not any(char in special_characters for char in password):
        return False
    # Check if the password is in the list of common passwords
    common_passwords = ["Passw0rd!", "Welcome123", "Admin@123", "Qwerty!23", "Summer2023", "Winter2024", "Autumn@2022", "Spring_21",
    "Abc123!@", "1234qwer@", "Test@1234", "User#2020", "Love@123", "Hello@123", "Letmein!23", "Monkey@2020",
    "Football@7", "Sunshine1!", "Dragon_88", "Princess#1", "Shadow99!", "Michael@12", "Baseball!23", "Hunter#99",
    "Superman1!", "Batman@123", "Tigger@77", "Buster!23", "Jordan_23", "Computer1!", "Internet@2", "Ginger#2020",
    "Hannah!21", "Ashley123!", "Maggie#7", "Taylor@55", "Mustang!1", "Cheese@123", "Freedom!88", "Soccer2022!",
    "Pokemon1@", "Naruto!99", "Jesus@777", "Matrix_09", "Trustme#1", "Whatever@8", "Access123!", "Loveme@22",
    "Cookie!12", "Tiger@888", "Qaz@1234", "Zaq1@zaq1", "Blink@182", "Starwars!9", "Pass1234@", "Magic@456",
    "1234!Abcd", "IloveYou@1", "Secret@12", "Galaxy@88", "Marvel#12", "Ironman@3", "Spiderman@4", "Captain@1",
    "Thor!2020", "Hulk@smash1", "Wakanda#4", "Panther!7", "BlackWidow@1", "Vision!909", "Scarlet@Witch",
    "Admin2024!", "Qwerty2023@", "Update@123", "System#2021", "Python@3.9", "Code@2022", "Developer!88",
    "Debug@001", "Linux#Mint1", "Ubuntu!20", "Windows@11", "Stack@123", "Overflow!9", "Github@999", "Terminal@3",
    "Hack3r@007", "Root@1234", "Shell!_2023", "AdminRoot@", "Coder@101", "Scripts@22", "Firewall#33", "Ping@88",
    "Router_01!", "Gateway@1", "Network!45", "Cloud@AWS1", "Azure@_123", "Google@12", "Yahoo@09", "Gmail!88",
    "Email@pass1", "Password@Me", "Secure!123"]
    if password in common_passwords:
        print("Password is too common. Try again.")
        return False
    # If all criteria are met, return True
    return True    
# If all criteria are met, print a success message and break out of the loop.
if validate_password(password):
    print("Password is valid.")
else:
    print("Password was not successfully created or is too common. Try again.")
  
# If the password is not valid, prompt the user to enter another password.
password = input()


# Check if the password is in the list of common passwords
# List of common passwords
# List of common passwords
# common_passwords = ["password", "123456", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "iloveyou"]
# Check if the password is valid
# List of common passwords
# Check if the password is valid
# Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character

    
    
    