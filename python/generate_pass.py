import random
import string

def generate_master_key_password(length=32):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    all_characters = lowercase + uppercase + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

master_key_password = generate_master_key_password(32)
print(master_key_password)