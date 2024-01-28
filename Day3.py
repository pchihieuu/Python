def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    has_lowercase = False
    has_digit = False
    has_uppercase = False
    has_special = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True

    return has_lowercase and has_digit and has_uppercase and has_special


input_passwords = input("Nhập chuỗi mật khẩu: ")
passwords = input_passwords.split(",")

valid_passwords = []
for password in passwords:
    if is_valid_password(password):
        valid_passwords.append(password)

print(",".join(valid_passwords))
