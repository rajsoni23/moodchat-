import streamlit as st
import sqlite3
st.set_page_config(
    layout="centered",
    page_title="Moodbot - Details"
)
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


conn = sqlite3.connect("moodbot.db")
cursor = conn.cursor()
cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                base_mood TEXT NOT NULL
            )
            """)

conn.commit()
st.title("Set up your MoodBot Profile")
name = st.text_input("Name" , placeholder = "Type your name here..")
st.number_input("Age", min_value = 18, max_value = 100)
option = st.selectbox(
    "Please select you country",["Afghanistan", "Argentina", "Australia","Bangladesh", "Brazil", "Canada", "China", "Egypt", "France", "Germany","India", "Indonesia", "Italy", "Japan", "Kenya", "Mexico", "Nepal", "Netherlands", "Nigeria", "Pakistan", "Russia", "Saudi Arabia", "South Africa", "South Korea", "Spain", "Sri Lanka", "Switzerland", "Thailand"],
    index= None,
    placeholder="Select your country",
)
default_mood = st.selectbox(
    "How are you feeling today?", 
    ["Energetic" , "Happy", "Sad" , "Calm" , "Anxious" , "Tired" , "Overwhelmed" ]

)    
if st.button("Save Profile"):
    if name.strip():
        if "user_name" in st.session_state:
            st.success(f"Welcome, {name}. Head over to the Mood Chat tab ✨" )
        else:
            st.warning("Please enter your name to save your profile.")

cursor.execute("INSERT INTO users (name , base_mood) VALUES (? ,?)", (name , default_mood))
conn.commit()
st.session_state["user_name"] = name
st.session_state["base_mood"] = default_mood

conn.close()
