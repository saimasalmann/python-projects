import re
import streamlit as st

def password_strength(password):
    score = 0
    messages = []  # List to store messages

    # Password length checking
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    # Upper and Lower case checking
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Password should contain both upper and lower case characters.")

    # Digit checking
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Password should contain at least one digit.")

    # Special character checking
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Password should contain at least one special character (!@#$%^&*).")
    
    # Display messages in the Streamlit UI
    if messages:
        st.write("---")
        st.markdown("##### *Improvement Suggestions:*")
        st.write("---")
    for message in messages:
        st.write(message)

    # Final score checking
    if score == 4:
        st.success("✅ Password is strong.")
    elif score == 3:
        st.info("🟡 Password is medium, try adding more security features.")
    else:
        st.error("❗ Password is weak, try adding more security features.")
    
# Streamlit UI setup
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔒 Password Strength Checker")
st.markdown("##### *Enter your password to check its strength and suggestions for more secured password.*")

password = st.text_input("Enter your password:", type="password", key="password")

if st.button("Check Password"):
    password_strength(password)
