import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Aneesh Royal SPS ", page_icon="🧱", layout="centered")

# --- 1. CUSTOM CSS FOR ROYAL THEME ---
design_css = """
<style>
    .stApp { background-color: #fcfbf7; }
    .main-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(197, 160, 89, 0.2);
        border: 2px solid #c5a059;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-text { color: #1a1a1a; font-family: 'Georgia', serif; font-size: 32px; font-weight: bold; }
    .gold-line { height: 2px; background: linear-gradient(to right, transparent, #c5a059, transparent); margin: 15px 0; }
    .score-box {
        font-size: 24px;
        font-weight: bold;
        color: #1a1a1a;
        background: #fdfaf0;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #c5a059;
    }
    .round-text { color: #c5a059; font-size: 18px; font-weight: bold; text-transform: uppercase; }
</style>
"""
st.markdown(design_css, unsafe_allow_html=True)

# --- 2. JS CONFETTI EFFECT ---
confetti_js = """
<canvas id="confetti" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:9999;pointer-events:none;"></canvas>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<script>
    var count = 200;
    var defaults = { origin: { y: 0.7 } };
    function fire(particleRatio, opts) {
      confetti(Object.assign({}, defaults, opts, {
        particleCount: Math.floor(count * particleRatio)
      }));
    }
    fire(0.25, { spread: 26, startVelocity: 55 });
    fire(0.2, { spread: 60 });
    fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
    fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
    fire(0.1, { spread: 120, startVelocity: 45 });
</script>
"""

# --- 3. SESSION STATE SETUP ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "u_score" not in st.session_state:
    st.session_state.u_score = 0
    st.session_state.c_score = 0
    st.session_state.round_num = 1
    st.session_state.history = []
    st.session_state.match_over = False

# ---- LOGIN SCREEN ----
if not st.session_state.logged_in:
    st.markdown('<div class="main-card"><div class="header-text">👑 ANEESH SPS GAME</div><div class="gold-line"></div><p style="color:#c5a059; letter-spacing:2px;">GAMER LOGIN</p></div>', unsafe_allow_html=True)
    
    user = st.text_input("👤 Username", placeholder="Enter name...")
    pwd = st.text_input("🔑 Password", type="password", placeholder="Enter password...")
    
    if st.button("ENTER GAME 🚀"):
        if user == "Aneesh" and pwd == "43214":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Credentials!")

# ---- GAME SCREEN ----
else:
    # Sidebar Logout & Reset
    if st.sidebar.button("Logout 🚪"):
        st.session_state.logged_in = False
        st.rerun()
    
    if st.sidebar.button("Reset Match 🔄"):
        st.session_state.u_score = 0
        st.session_state.c_score = 0
        st.session_state.round_num = 1
        st.session_state.history = []
        st.session_state.match_over = False
        st.rerun()

    # Header Card
    st.markdown(f'<div class="main-card"><div class="round-text">Round {st.session_state.round_num} of 5</div><div class="header-text">Stone Paper Scissors</div><div class="gold-line"></div></div>', unsafe_allow_html=True)

    # Score Board
    col1, col2 = st.columns(2)
    col1.markdown(f'<div class="score-box">👤 Aap: {st.session_state.u_score}</div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="score-box">🤖 Aneesh: {st.session_state.c_score}</div>', unsafe_allow_html=True)

    st.write("---")

    # Match in Progress
    if not st.session_state.match_over:
        st.subheader("Apna Choice Chuniye:")
        b_col1, b_col2, b_col3 = st.columns(3)
        
        user_choice = None
        if b_col1.button("🧱 Stone"): user_choice = "stone"
        if b_col2.button("📄 Paper"): user_choice = "paper"
        if b_col3.button("✂ Scissors"): user_choice = "scissors"

        if user_choice:
            options = ["stone", "paper", "scissors"]
            Aneesh_choice = random.choice(options)
            
            # Logic
            if user_choice == Aneesh_choice:
                result = "Tie"
            elif (user_choice == "stone" and Aneesh_choice == "scissors") or \
                 (user_choice == "paper" and Aneesh_choice == "stone") or \
                 (user_choice == "scissors" and Aneesh_choice == "paper"):
                result = "User"
                st.session_state.u_score += 1
            else:
                result = "Aneesh"
                st.session_state.c_score += 1
            
            # Feedback
            st.info(f"Aapne chuna: **{user_choice.upper()}** | Aneesh ne chuna: **{Aneesh_choice.upper()}**")
            if result == "User": st.success("🎉 Aapne yeh round jeeta!")
            elif result == "Aneesh": st.warning("😥 Aneesh yeh round jeet gaya!")
            else: st.write("🤝 Yeh round Tie raha!")

            # Update Round
            if st.session_state.round_num < 5:
                st.session_state.round_num += 1
            else:
                st.session_state.match_over = True
            
            st.button("Next Round ➡️")

    # Final Match Result
    else:
        st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
        st.header("🏆 FINAL RESULT 🏆")
        
        if st.session_state.u_score > st.session_state.c_score:
            st.balloons()
            st.components.v1.html(confetti_js, height=0)
            st.success(f"👑 MUBARAK HO! Aap Match jeet gaye! ({st.session_state.u_score}-{st.session_state.c_score})")
        elif st.session_state.c_score > st.session_state.u_score:
            st.error(f"🎮 Aneesh Match jeet gaya! ({st.session_state.c_score}-{st.session_state.u_score})")
        else:
            st.write("🤝 Match Tie ho gaya!")
            
        if st.button("New Match Khelein 🔄"):
            st.session_state.u_score = 0
            st.session_state.c_score = 0
            st.session_state.round_num = 1
            st.session_state.match_over = False
            st.rerun()
