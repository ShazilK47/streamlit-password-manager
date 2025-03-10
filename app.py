
import streamlit as st
import pyperclip
from generator import generate_password  
from password_checker import check_password_strength


st.set_page_config(page_title="Password Manager", layout="wide")

# Sidebar 
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to:", ["Generate Password", "Check Password Strength"])

def load_css():
    with open("styles.css", "r") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

load_css()

if page == "Generate Password":

    st.title("🔒 Password Generator")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.subheader("Password Strength")
        strength = st.radio("Choose Strength:", ["Weak", "Medium", "Strong"], index=1)

        st.subheader("Customize Length")
        length = st.slider("Select Password Length:", 6, 32, 12)

    with col2:
        st.subheader("Generated Password")

        if st.button("🔄 Generate Password"):
            password = generate_password(strength, length)
            st.session_state["password"] = password

        password = st.session_state.get("password", "******")

        # Password visibility toggle
        show_password = st.checkbox("👁 Show Password", value=True)
        display_password = password if show_password else "•" * len(password)

        st.markdown(
            f"""
            <div class="password-box">
                <span class="password-text">{display_password}</span>
            </div>
            
            """,
            unsafe_allow_html=True,
        )
        # if st.button('Copy'):
        #     pyperclip.copy(password)
        #     st.success('Text copied successfully!')
     

    with col3:
        st.subheader("Strength Level")
        strength_color = strength.lower()
        st.markdown(f"<div class='strength-indicator {strength_color}'> {strength} </div>", unsafe_allow_html=True)

elif page == "Check Password Strength":
    # -> page 2: Password Strength Checker 
    st.title("🔑 Password Strength Checker")

    password = st.text_input("Enter your password to check strength:", "")

    if password:
        strength_level, score, feedback = check_password_strength(password)
        st.markdown(f"**🔹 Strength:** {strength_level} ({score}/4)")

        if strength_level == "Weak":
            st.error(feedback)

            # -> Suggestion 
            if st.button("🔄 Suggest a Strong Password"):
                suggested_password = generate_password("Strong", 12)
                st.success(f"Suggested Password: `{suggested_password}`")

        elif strength_level == "Moderate":
            st.warning(feedback)
        else:
            st.success(feedback)