import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Track It | AI Student Fitness", page_icon="🥗", layout="centered")

# --- PREMIUM CSS ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f172a, #1e293b); color: #f8fafc; }
    
    /* Card Styling */
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-top: 25px;
        backdrop-filter: blur(10px);
        line-height: 1.6;
    }
    
    /* Glowing Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #10b981, #3b82f6);
        color: white;
        font-weight: 800;
        border-radius: 12px;
        border: none;
        padding: 15px;
        transition: 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🥗 Track It: Student AI Fitness")
st.write("Professional diet & workout plans customized for your body and budget.")

# --- SIDEBAR (User Profile & AI Setup) ---
with st.sidebar:
    st.header("🔑 AI Setup")
    api_key = st.text_input("Gemini API Key", type="password", help="Get your key at aistudio.google.com")
    
    st.header("👤 Your Profile")
    gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)
    age = st.number_input("Age", min_value=1, max_value=120, value=20)
    
    # New Parameters: Height and Weight
    height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    weight = st.number_input("Current Weight (kg)", min_value=10, max_value=300, value=70)
    
    # Simple BMI Calculation
    bmi = round(weight / ((height/100)**2), 1)
    st.info(f"💡 Your calculated BMI: **{bmi}**")
    
    st.header("🎯 Goals & Budget")
    goal = st.selectbox("Your Main Goal", ["Lose Weight", "Build Muscle", "Healthy Maintenance"])
    diet_pref = st.selectbox("Dietary Preference", ["Vegetarian", "Non-Veg", "Vegan", "Eggitarian"])
    budget = st.select_slider("Weekly Budget", options=["Budget (Cheap)", "Standard", "Premium"])

# --- GENERATION LOGIC ---
if st.button("Generate My Personalized Plan 🚀"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar!")
    else:
        try:
            # Configure Gemini 3 Flash
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-3-flash-preview')
            
            # Integrated Prompt including ALL new parameters
            prompt = f"""
            Act as an elite Fitness and Nutrition Expert. Create a detailed 1-day plan for:
            - Profile: {age}yo {gender}, Height: {height}cm, Weight: {weight}kg (BMI: {bmi})
            - Goal: {goal}
            - Diet: {diet_pref}
            - Budget: {budget} (Focus on cheap student ingredients like lentils, rice, eggs)

            Include:
            1. 🍳 Full Diet Plan (Breakfast, Lunch, Dinner, Snack) with estimated calories/macros.
            2. 🏋️ Home-friendly Workout tailored to the goal.
            3. 💡 Money-saving student tips.
            """
            
            with st.spinner("🤖 AI Coach is reasoning through your data..."):
                # Use Gemini 3 "Thinking"
                response = model.generate_content(
                    prompt,
                    generation_config={"thinking_level": "medium"} 
                )
                
                # Display in Premium Card
                st.markdown(f"""
                <div class="premium-card">
                    {response.text}
                </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.info("If you see 'thinking_level' error, try updating the library: pip install -U google-generativeai")

# --- FOOTER ---
st.markdown("---")
st.caption("Built for students by Omkar-IT using Gemini 3 AI")