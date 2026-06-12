import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Royal Number Guesser", page_icon="👑", layout="centered")

# Custom HTML & CSS for Gold & Royal Login Page
login_html = """
<style>
    /* Streamlit ke default elements ko chupati hai jab login na ho */
    .stApp {
        background-color: #fcfbf7;
    }
    .login-container {
        background: #ffffff;
        padding: 35px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(197, 160, 89, 0.2);
        border: 2px solid #c5a059;
        text-align: center;
        font-family: 'Georgia', serif;
        max-width: 400px;
        margin: 40px auto;
    }
    .login-header {
        color: #1a1a1a;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }
    .login-subtitle {
        color: #c5a059;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }
    .gold-divider {
        height: 2px;
        background: linear-gradient(to right, transparent, #c5a059, transparent);
        margin: 15px 0;
    }
</style>

<div class="login-container">
    <div class="login-header">👑 ANEESH ROYAL GAME</div>
    <div class="gold-divider"></div>
    <div class="login-subtitle">Gamer Login Portal</div>
</div>
"""

# Session State for Login Tracking
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---- LOGIN SCREEN ----
if not st.session_state.logged_in:
    # Render Custom Gold & Royal Header
    st.markdown(login_html, unsafe_allow_html=True)
    
    # Input Fields inside Streamlit (Styled beautifully by CSS background)
    username = st.text_input("👤 Username", placeholder="Enter username...")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter password...")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Login Button
    if st.button("ENTER GAME 🚀"):
        # Yahan aap apna username aur password badal sakte hain
        if username == "Aneesh" and password == "4321":
            st.session_state.logged_in = True
            st.success("Access Granted! Loading Game...")
            st.rerun()
        else:
            st.error("Invalid Royal Credentials! Try Again.")

# ---- ACTUAL GAME SCREEN (Sirf login hone ke baad dikhega) ----
else:
    st.title("🎯 Guess The Secret Number!")
    st.write("Aneesh ne 1 se 100 ke beech ek number socha hai. Kya aap use pehchan sakte hain?")
    
    # Logout Button in Sidebar
    if st.sidebar.button("Logout 🚪"):
        st.session_state.logged_in = False
        st.rerun()

    st.write("---")

    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.lives = 5
        st.session_state.game_status = "PLAYING"

    if st.session_state.game_status == "PLAYING":
        st.subheader(f"Zindagi (Lives) bachi hain: {'❤️ ' * st.session_state.lives}")
        user_guess = st.number_input("Apna Guess chunein (1 se 100):", min_value=1, max_value=100, value=50)
        
        if st.button("Check Guess 🚀"):
            if user_guess == st.session_state.secret:
                st.session_state.game_status = "WON"
                st.rerun()
            else:
                st.session_state.lives -= 1
                if st.session_state.lives == 0:
                    st.session_state.game_status = "LOST"
                    st.rerun()
                elif user_guess < st.session_state.secret:
                    st.warning("📉 Thoda BADA (Higher) number socho!")
                else:
                    st.warning("📈 Thoda CHOTA (Lower) number socho!")

    if st.session_state.game_status == "WON":
        st.balloons()
        st.success(f"👑 MUBARAK HO! Sahi jawab tha **{st.session_state.secret}**. Aap jeet gaye! 🎉")

    if st.session_state.game_status == "LOST":
        st.error(f"😢 GAME OVER! Aapki saari lives khatam ho gayi. Sahi number tha: **{st.session_state.secret}**")

    if st.session_state.game_status != "PLAYING":
        if st.button("Dubara Khelein 🔄"):
            st.session_state.secret = random.randint(1, 100)
            st.session_state.lives = 5
            st.session_state.game_status = "PLAYING"
            st.rerun()
