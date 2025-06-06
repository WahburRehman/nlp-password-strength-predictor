import numpy as np

# Har password ki length nikalnay wala function
def get_length(password):
    return len(password)

# Har password mein lowercase letters ki ratio
def check_lower_freq(password):
    return round(len([char for char in password if char.islower()]) / len(password), 3)

# Har password mein uppercase letters ki ratio
def check_upper_freq(password):
    return round(len([char for char in password if char.isupper()]) / len(password), 3)

# Har password mein digits ki ratio
def check_numeric_freq(password):
    return round(len([char for char in password if char.isdigit()]) / len(password), 3)

# Har password mein special characters ki ratio
def check_special_char_freq(password):
    return round(len([char for char in password if not char.isdigit() and not char.isalpha()]) / len(password), 3)
