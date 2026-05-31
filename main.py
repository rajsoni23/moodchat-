import streamlit as st
import os




st.set_page_config(
    layout = "centered",
    page_title = " Moodbot",
    page_icon = "😺"
)
st.title("🐱MoodBot")

col2, col3 = st.columns([1,1])
with col3:
    st.image(os.path.join(os.getcwd(), "images","catbot.png" ))
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Irish+Grover&family=Press+Start+2P&display=swap');

    .loading{
        font-family: "Press Start 2P";
        text-align: center;
        font-size: 50px;
    }
    .dots::after{
            content: '...';
            display: inline-block;
            animation: dots 1.2s steps(4,end) infinite;
            }
        @keyframes dots{
            0% {content: '.';}
            25% {content: '..';}
            50% {content: '...';}
            75% {content: '..';}
            100% {content: '...';}}
    </style>
    <p class="loading">Your MoodBot is loading<span class="dots"></span></p>
""", unsafe_allow_html= True)
import streamlit as st

# Force an HTML container block to stay static on screen
st.html("""
<style>
    
    .stMainBlockContainer, .stAppViewContainer {
        background: transparent !important;
    }

    
    .mobile-glow-bg {
        position: fixed;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 207, 255, 0.35) 0%, rgba(0, 207, 255, 0) 65%);
        filter: blur(40px);
        z-index: -1;
        pointer-events: none;
    }
</style>
<div class="mobile-glow-bg"></div>
""")




details_page = st.Page("views/details.py", title = "Profile", icon = "👤")
chat_page = st.Page("views/chat.py", title = "Chat", icon = "💬")
pg = st.navigation([details_page , chat_page])
pg.run()
