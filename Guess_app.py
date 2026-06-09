import streamlit as st
import random
from streamlit_confetti import confetti
st.set_page_config(page_title ="Number Guesser", page_icon="🎯", layout="centered")
st.title("🎯 Guess The Secret Number!")
st.write("Aneesh ne 1 se 100 ke beech ek number socha hai. Kya aap use pehchan sakte hain?")
st.write("---")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.lives = 5
    st.session_state.game_status = "PLAYING" # PLAYING, WON, LOST

if st.session_state.game_status == "PLAYING":
    st.subheader(f"Zindagi (Lives) bachi hain: { '❤️' *st.session_state.lives}")
    user_guess = st.number_input("Apna Guess chunein (1, 100):", min_value= 1, max_value=100, value=00)

    if st.button("Check Guess🚀"):
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
                st.warning("📈Thoda CHOTA (Lower) number socho!")

if st.session_state.game_status == "WON":
    st.balloons()
    time.sleep(2)
    st.success(f"👑 MUBARAK HO! Sahi jawab tha **{st.session_state.secret}**. Aap jeet gaye!🎉")
    st.balloons()
    confetti()

if st.session_state.game_status == "LOST":
    st.error(f"😥 GAME OVER! Aapki saari lives khatam ho gayin. Sahi number tha: **{st.session_state.secret}**")

if st.session_state.game_status != "PLAYING":
    if st.button("Dubara Khelo 🔁"):
        st.session_state.secret = random.randint(1, 100)
        st.session_state.lives = 5
        st.session_state.game_status = "PLAYING"
        st.rerun()
