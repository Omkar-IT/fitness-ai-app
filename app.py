import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Track It | AI Student Fitness", page_icon="🥗", layout="centered")

# --- PREMIUM CSS ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f172a, #1e293b); color: #f8fafc; }
    
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-top: 25px;
        backdrop-filter: blur(10px);
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #10b981, #3b82f6);
        color: white;
        font-weight: 800;
        border-radius: 12px;
        border: none;
        padding: 15px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🥗 Track It: Student AI Fitness")
st.write("Customized diet and workout plans using Gemini 3 Reasoning.")

# --- SIDEBAR (Parameters) ---
with st.sidebar:
    st.header("🔑 AI Setup")
    api_key = st.text_input("Gemini API Key", type="password")
    
    st.header("👤 Your Profile")
    gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)
    age = st.number_input("Age", 15, 100, 20)
    height = st.number_input("Height (cm)", 50, 250, 170)
    weight = st.number_input("Weight (kg)", 10, 300, 70)
    
    # BMI logic
    bmi = round(weight / ((height/100)**2), 1)
    st.info(f"💡 Your BMI: **{bmi}**")
    
    st.header("🎯 Goals")
    goal = st.selectbox("Goal", ["Lose Weight", "Build Muscle", "Stay Healthy"])
    diet_pref = st.selectbox("Diet", ["Vegetarian", "Non-Veg", "Vegan", "Eggitarian"])
    budget = st.select_slider("Budget", options=["Cheap", "Standard", "Premium"])

# --- GENERATION LOGIC ---
if st.button("Generate My Personalized Plan 🚀"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    else:
        try:
            # 1. Setup Model
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-3-flash-preview')
            
            prompt = f"""
            Act as an elite Fitness Expert. Create a 1-day plan for:
            - Profile: {age}yo {gender}, {height}cm, {weight}kg (BMI: {bmi})
            - Goal: {goal}, Diet: {diet_pref}, Budget: {budget}
            
            Provide a meal plan and a home workout. Use simple student-friendly ingredients.
            """
            
            with st.spinner("🤖 AI Coach is reasoning..."):
                # 2. Use the correct "Thinking" configuration
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "thinking_level": "medium" 
                    }
                )
                
                # 3. Display Result
                st.markdown(f'<div class="premium-card">{response.text}</div>', unsafe_allow_html=True)
                
        except Exception as e:
            # Error handling for quota or model name issues
            st.error(f"Something went wrong: {e}")
            if "thinking_level" in str(e):
                st.info("Tip: Update your library using 'pip install --upgrade google-generativeai'")

# --- FOOTER ---
st.markdown("---")
st.caption("Built for students by Omkar-IT")