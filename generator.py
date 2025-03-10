
import random
import string

def generate_password(strength: str, length: int) -> str:
    """Generates a password based on selected strength and length."""
    if strength == "Weak":
        chars = string.ascii_lowercase
    elif strength == "Medium":
        chars = string.ascii_letters + string.digits
    elif strength == "Strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid Strength"

    return ''.join(random.choice(chars) for _ in range(length))
