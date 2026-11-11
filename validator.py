def is_valid_password(password):
    if len(password) >= 8 and "@" in password:
        return True
    else:
        return False

is_valid_password(hephzy@18)
print(password)