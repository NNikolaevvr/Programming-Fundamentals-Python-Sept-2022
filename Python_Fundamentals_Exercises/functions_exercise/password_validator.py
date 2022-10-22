def valid_password(pass1):
    is_password_valid = True
    digit_counter = 0
    if len(pass1) < 6 or len(pass1) > 10:
        print("Password must be between 6 and 10 characters")
        is_password_valid = False

    if not pass1.isalnum():
        print("Password must consist only of letters and digits")
        is_password_valid = False

    for current_num in pass1:
        if current_num.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        is_password_valid = False

    return is_password_valid


password = input()

is_password_valid = valid_password(password)

if is_password_valid:
    print("Password is valid")
