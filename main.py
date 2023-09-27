# Information Security Awareness Training Program

def password_strength(password):
    # Check the strength of a password
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    elif not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    else:
        return "Strong: Password meets all security criteria."

def main():
    print("Welcome to Information Security Awareness Training!")
    print("Please create a password for your account.")
    user_password = input("Enter your password: ")
    
    result = password_strength(user_password)
    print(result)

if __name__ == "__main__":
    main()
