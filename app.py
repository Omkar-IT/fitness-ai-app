import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Fitness Planner", page_icon="💪", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .result-card {
        background-color: #1f2937;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00ff88;
        margin-top: 20px;
        line-height: 1.6;
    }
    .stButton>button { width: 100%; background-color: #00ff88; color: black; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("💪 AI Student Personal Trainer")
st.write("Personalized plans based on your culture, budget, and needs.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", 15, 60, 20)
    goal = st.selectbox("Goal", ["Lose Weight", "Build Muscle", "Stay Healthy"])
    diet = st.selectbox("Diet", ["Vegetarian", "Non-Veg", "Vegan", "Halal"])
    budget = st.select_slider("Weekly Budget", ["Student Low", "Medium", "High"])

if st.button("Generate My Plan 🚀"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    else:
        try:
            genai.configure(api_key=api_key)
            # USING THE MODEL NAME FROM YOUR SCANNER
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            prompt = f"Act as a student fitness coach. Create a 1-day {goal} plan for a {age}yo {gender}. Diet: {diet}. Budget: {budget}. Include a workout and cheap meals."
            
            with st.spinner("🤖 AI Coach is drafting your plan..."):
                response = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Something went wrong: {e}")