
import re
from generator import generate_password 

COMMON_PASSWORDS = {"password", "123456", "password123", "admin", "qwerty", "letmein", "welcome"}

def check_password_strength(password):
    score = 0
    feedback = []

    # -> Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        return "Weak", 0, "❌ This password is too common! Please use a more secure password."

    # -> Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # -> Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # -> Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # -> Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # -> Scoring System 
    if score >= 4:
        return "Strong", score, "✅ Strong Password!"
    elif score == 3:
        return "Moderate", score, "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "Weak", score, f"❌ Weak Password - {', '.join(feedback)}. Try using a stronger password."

