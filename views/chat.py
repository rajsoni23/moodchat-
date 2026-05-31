import streamlit as st
import os
import random
st.set_page_config(
    layout="wide",
    page_title = "Moodbot- Chat"
)


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
st.title("MoodBot Chat")
st.image(os.path.join(os.getcwd(), "images", "catprofile.png"))

if "user_name" not in st.session_state:
    st.warning("⚠ Please fill out your profile details on the MoodBot Profile Details first!")
    st.stop()

user_name = st.session_state["user_name"]
base_mood = st.session_state["base_mood"]

#-----------------------------------EMOTION BASED KEYWORD/PHRASE LIST-------------------------

# ---------------- SADNESS ----------------
all_sad_phrases = ["im sad","i'm sad","feeling sad","not feeling good lately","i feel down","feeling low","i feel empty","i feel numb","i feel broken","i feel hopeless","i feel hurt","i want to cry","crying","cant stop crying","nothing feels right","i feel lost","i feel bad","not doing well","i dont feel good","bad day","emotionally drained"]
# ---------------- STRESS / ANXIETY ----------------
all_anxious_phrases = ["stressed","so stressed","feeling stressed","overwhelmed","too much pressure","under pressure","anxious","worried","nervous","panic","cant focus","can't focus","my mind is racing","studies and exams","exam stress","my exams","falling behind","too much going on"]
# ---------------- LONELINESS ----------------
all_lonely_phrases = ["im lonely","i'm lonely","feel alone","i feel alone","sad and lonely","nobody understands me","i feel invisible","i feel ignored","i feel left out","i miss someone","wish someone cared","nobody talks to me","i got nobody","i feel unwanted"]
# ---------------- ANGER ----------------
all_anger_phrases = ["angry","mad","frustrated","annoyed","irritated","fed up","i hate this","so done","done with everything","this sucks","this is frustrating","im pissed","cant deal with this"]
# ---------------- EXHAUSTION / BURNOUT ----------------
all_burnout_phrases = ["im tired","i'm tired","tired lately","feeling tired","feeling a bit tired ","exhausted","mentally exhausted","emotionally exhausted","drained","burned out","burnt out","no energy","running on empty","so tiring","overwhelming and tiring","i need rest","my brain is fried","too tired","just tired"]
# ---------------- HAPPINESS ----------------
happy_phrases = ["happy","feeling happy","excited","great","amazing","good day","productive","motivated","confident","proud","things are going well","doing well","feeling great"]
# ---------------- GRATITUDE ----------------
thankyou_phrases = ["thanks","thank you","thankyou","tysm","thanks a lot","thank you so much","really appreciate it","appreciate it","that helped","means a lot"]
# ---------------- AFFIRMATION ----------------
affirmation_phrases = ["yes","yeah","yep","yup","sure","absolutely","please","go on","continue","tell me more","okay continue"]
# ---------------- NEGATIVE / REFUSAL ----------------
negative_phrases = ["nope","nah","not now","maybe later","i dont want to","i don't want to","rather not","id rather not","don't ask","leave it"]
#=========================Ending
exit_phrases = ["bye", "goodbye", "see you", "ttyl", "talk later", "exit", "leave"]
# ---------------- FALLBACK / SOFT-ENDING PHRASES---------------
soft_end_phrases = ["ok", "okay", "hmm", "idk", "alright"]

#-------------------------------Response style sets to add conversational depth-----------------------------
#-------------------------------sad--------------------
sad_listening = [
    "I'm really sorry you're feeling this way.",
    "I'm listening. Whatever you're feeling matters.",
    "I'm here with you.",
    "That sounds really heavy. You don't have to carry it alone",
    "That sounds really tough to sit with"
]

sad_reflective = [
    "It sounds like this sadness has been sitting with you for a while.",
    "It seems like something has been weighing on your heart.",
    "Sometimes  difficult feelings quietly build up over time."
    "That kind of sadness can feel really heavy to carry around alone."
]

sad_clarifying = [
    "Do you know what triggered this feeling today?",
    "Has something specific been making today harder?",
    "What feels heaviest right now?"
]
sad_guidance = [
    "It's okay to feel low sometimes.Remember that feelings are temporary and they don't define you.",
    "Be gentle with yourself right now. Often we are our own harshest critics.",
    "You don't have to figure everything out all at once. Just take it moment by moment."
]
#-----------------------stress-----------------
stress_listening = [
    "That sounds exhausting to carry.",
    "You've been dealing with a lot.",
    "That kind of pressure can feel overwhelming."
]

stress_reflective = [
    "It sounds like things have been piling up for a while.",
    "It seems like this pressure has been slowly building.",
    "That kind of stress can make everything feel harder."
]

stress_clarifying = [
    "What's stressing you out the most right now?",
    "Is it the workload, deadlines, or expectations?",
    "What part feels hardest to manage?"
]
stress_guidance = [
    "Take things one step at a time. Trying to solve everything at once can make it feel more overwhelming.",
    "It's okay to pause for a moment. This will help you reset and approach things with a clearer mind.",
    "You've been pushing hard — don't forget to reset."
]
#-----------------------loneliness-----------------
lonely_listening = [
    "I'm here with you.",
    "That sounds really heavy. But I'm glad you're sharing it.",
    "You deserve to feel heard and understood. It's okay to feel this way, and you don't have to go through it alone."
]

lonely_reflective = [
    "It sounds like you've been feeling disconnected lately.",
    "Feeling unseen can weigh heavily over time.",
    "That kind of loneliness can feel deeply isolating."
]

lonely_clarifying = [
    "Has something made you feel more distant lately?",
    "Do you feel this way around everyone or someone specific?",
    "What feels most isolating right now?"
]
lonely_guidance = [
    "You don't have to sit with this feeling alone.",
    "Your feelings matter.",
    "Sometimes opening up, even a little, can help."
]

#-----------------------anger------------------
anger_listening = [
    "That sounds really frustrating.",
    "I can understand why that would upset you.",
    "That sounds like a lot to deal with."
]

anger_reflective = [
    "It sounds like this has been building for a while.",
    "It seems like you've been holding in a lot of frustration.",
    "Sometimes repeated pressure turns into anger."
]

anger_clarifying = [
    "What triggered this frustration most?",
    "Is this about one moment or something ongoing?",
    "What part of this feels most unfair?"
]
anger_guidance = [
    "It helps to let frustration out instead of bottling it up.",
    "Taking a pause might help you reset.",
    "You don't have to solve this while overwhelmed."
]
#-------------------------------Exhaustion/burnout------------------
exhaustion_listening = [
    "You sound really drained.",
    "That sounds exhausting.",
    "You've been pushing yourself hard."
]

exhaustion_reflective = [
    "It sounds like your energy has been running low for a while.",
    "It seems like this exhaustion has been building over time.",
    "Sometimes burnout creeps in quietly."
]

exhaustion_clarifying = [
    "What's been draining you most lately?",
    "Do you think this is physical tiredness or mental exhaustion?",
    "Have you been giving yourself enough time to rest?"
]
exhaustion_guidance = [
    "Rest isn't laziness — it's necessary.",
    "It's okay to slow down.",
    "Your mind might be asking for a break."
]
#---------------------------------Happiness--------------------
happy_listening = [
    "That's really good to hear.",
    "I'm glad things are feeling better.",
    "That sounds wonderful."
]

happy_reflective = [
    "It sounds like things are moving in a positive direction.",
    "That energy really shows through.",
    "It seems like something is going right for you."
]

happy_clarifying = [
    "What's been making you feel this way?",
    "What’s been the highlight of your day?",
    "What do you think contributed most to this?"
]
happy_guidance = [
    "You should feel proud of yourself.",
    "Keep that momentum going.",
    "Take a moment to appreciate your progress."
]

#-------------------------------bot responses based on keywords-----------------------------------
greeting_responses = ["Hey there! How are you feeling today?","Hi! What's been on your mind lately?","Hello ✨ How's your day going?","Hey! I'm here to listen.","Hi there 💙 How are you feeling right now?","Yo, How's it going?", "Hello, how are you today?"]
thankyou_responses = ["You're very welcome 💙","Anytime — I'm glad I could help.","I'm happy to be here for you.","Of course. That's what I'm here for.","You're always welcome to talk.","Glad I could help even a little.","No need to thank me — I'm here for you."]
fallback_responses = ["Tell me a little more about how you're feeling.","I'm listening.","I'm here for you — what's going on?","Want to talk more about that?"]
affirmation_responses = ["I'm listening — tell me more.","Go ahead, take your time.","I'm here for whatever you'd like to share.","Okay, tell me what's on your mind.","Whenever you're ready, I'm listening.","Feel free to say whatever you're feeling."]
negative_responses = ["That's okay. I'm here if you ever feel like talking.","That's completely okay — take your time.","I understand. I'm here whenever you're ready.","That's fine. You don't have to talk unless you want to.","No worries. Sometimes silence is okay too.","Whenever you feel ready, I'll be here."]
closing_responses = ["I'm really glad you talked with me today. Take care of yourself 💙","I’m here whenever you need to talk again.","Rest well. You’ve done enough for today.","I hope things feel a little lighter soon. See you later 🌿"]
soft_end_response = ["Alright, I’ll be here if you need me.","Take your time. No rush to continue.","Got it. I'm here whenever you feel like talking again."]
#-------------------------------------------------------------------------------------------------------------------
mood_map = {
    "sad" : {
        "phrases": all_sad_phrases,
        "listening" : sad_listening,
        "reflective" : sad_reflective,
        "clarifying" : sad_clarifying,
        "guidance" : sad_guidance

    },
    "lonely" : {
        "phrases" :  all_lonely_phrases,
        "listening" : lonely_listening,
        "reflective" : lonely_reflective,
        "clarifying" : lonely_clarifying,
        "guidance" : lonely_guidance

    },
    "burnout" :{
        "phrases" : all_burnout_phrases,
        "listening" : exhaustion_listening,
        "reflective" : exhaustion_reflective,
        "clarifying" : exhaustion_clarifying,
        "guidance" : exhaustion_guidance

    },
    "anxious" : {
        "phrases" : all_anxious_phrases,
        "listening" : stress_listening,
        "reflective" : stress_reflective,
        "clarifying" : stress_clarifying,
        "guidance" : stress_guidance
    },
    "anger" : {
        "phrases" : all_anger_phrases,
        "listening" : anger_listening,
        "reflective" : anger_reflective,
        "clarifying" : anger_clarifying,
        "guidance" : anger_guidance

    },
    "happy" : {
        "phrases" : happy_phrases,
        "listening" : happy_listening,
        "reflective" : happy_reflective,
        "clarifying" : happy_clarifying,
        "guidance" : happy_guidance
    },
}
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_mood_detected" not in st.session_state:
    st.session_state.last_mood_detected = None

if "greeted" not in st.session_state:
    st.session_state.greeted = False

if "chat_stage" not in st.session_state:
    st.session_state.chat_stage  = "intro"

if "last_bot_reply" not in st.session_state:
    st.session_state.last_bot_reply = None



if not st.session_state.greeted:
    base_mood = base_mood.lower()

    greeting_map = {
        "energetic" : f"Hey there {user_name}! ⚡ Your energy is fantastic today!Let's channel that into talking about what's going right!",
        "happy" : f"Hi {user_name}! 😊 Wonderful to see you in such a great headspace. What's bringing you joy today?",
        "sad" : f"Hi {user_name}! 😊 Wonderful to see you in such a great headspace. What's bringing you joy today?",
        "calm" : f"Hi {user_name}, 🧘🏻‍♀️ Steady, peaceful energy is a wonderful place to be. How is your day flowing",
        "anxious" :f"Hi {user_name}, 😰 Take a slow, deep breath. You are safe here. Let's tale things one small step at a time. What's causing the racing thoughts?" ,
        "tired" : f"Hey {user_name}, 😴 It sounds like your tank is running low. No pressure to perform here. What's been draining your battery?"
    }
    greeting = greeting_map.get(
        base_mood,
        f"Hello {user_name}!, I'm tuned to your profile. How can i help you today?"
    )
    st.session_state.messages.append({"role" : "assistant" , "content" : greeting})
    
    st.session_state.greeted = True
    st.session_state.chat_stage = "explore"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def detect_mood(text):
    for mood, data in mood_map.items():
        if any(p in text for p in data["phrases"]):
            return mood
    return None
def pick_response(response_list):
    available = [
        r for r in response_list
        if r != st.session_state.last_bot_reply
    ]
    if not available:
        available = response_list
    
    reply = random.choice(available)
    
    st.session_state.last_bot_reply = reply
    return reply

if user_input := st.chat_input("Talk to MoodBot..."):
    clean_text = user_input.lower().strip()
    st.session_state.messages.append({"role": "user" , "content" : user_input})
    with st.chat_message("user"):
            st.write(user_input)
    if any(phrase in clean_text for phrase in exit_phrases):
        bot_reply = pick_response(closing_responses)
    elif any(phrase in clean_text for phrase in thankyou_phrases):
        bot_reply = pick_response(thankyou_responses)
    elif any(phrase in clean_text for phrase in soft_end_phrases):
        bot_reply = pick_response(soft_end_response)
    elif any(phrase in clean_text for phrase in affirmation_phrases):
            if st.session_state.last_mood_detected:
                mood = st.session_state.last_mood_detected
                if st.session_state.chat_stage == "explore":
                    bot_reply = pick_response(mood_map[mood]["listening"])
                    st.session_state.chat_stage = "deeper"
                elif st.session_state.chat_stage == "deeper":
                    bot_reply = pick_response(mood_map[mood]["clarifying"])
                    st.session_state.chat_stage = "reflect"
                elif st.session_state.chat_stage == "reflect":
                    bot_reply = pick_response(mood_map[mood]["reflective"])
                    st.session_state.chat_stage = "support"
                else:
                    bot_reply = pick_response(mood_map[mood]["guidance"])
                    st.session_state.chat_stage = "explore"
            else:       
                bot_reply = pick_response(affirmation_responses)
    elif any(phrase in clean_text for phrase in negative_phrases):
        bot_reply = pick_response(negative_responses)

    else: 
        mood = detect_mood(clean_text)
        if mood:
            st.session_state.last_mood_detected = mood
            if st.session_state.chat_stage == "explore":
                bot_reply = pick_response(mood_map[mood]["listening"])
                st.session_state.chat_stage = "deeper"
            elif st.session_state.chat_stage == "deeper":
                bot_reply = pick_response(mood_map[mood]["clarifying"])
                st.session_state.chat_stage = "reflect"
            elif st.session_state.chat_stage == "reflect":
                bot_reply = pick_response(mood_map[mood]["reflective"])
                st.session_state.chat_stage = "support"
            else:
                bot_reply = pick_response(mood_map[mood]["guidance"])
                st.session_state.chat_stage = "explore"
        elif st.session_state.last_mood_detected:
            mood = st.session_state.last_mood_detected
            if st.session_state.chat_stage == "deeper":
                bot_reply = pick_response(mood_map[mood]["clarifying"])
                st.session_state.chat_stage = "reflect"
            elif st.session_state.chat_stage == "reflect":
                bot_reply = pick_response(mood_map[mood]["reflective"])
                st.session_state.chat_stage = "support"
            else:
                bot_reply = pick_response(mood_map[mood]["guidance"])
                st.session_state.chat_stage = "explore"
        else:
            bot_reply = pick_response(closing_responses)
    with st.chat_message("assistant"):
        st.write(bot_reply)
    st.session_state.messages.append({"role" : "assistant" , "content" : bot_reply})