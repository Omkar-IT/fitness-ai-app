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
</style>
""", unsafe_allow_html=True)

st.title("🥗 Track It: Student AI Fitness")

with st.sidebar:
    st.header("🔑 AI Setup")
    api_key = st.text_input("Gemini API Key", type="password")
    st.header("👤 Profile")
    goal = st.selectbox("Goal", ["Lose Weight", "Build Muscle", "Healthy Maintenance"])
    diet_pref = st.selectbox("Diet", ["Vegetarian", "Non-Veg", "Vegan", "Eggitarian"])
    budget = st.select_slider("Weekly Budget", options=["Budget", "Standard", "Premium"])

if st.button("Generate My Personalized Plan 🚀"):
    if not api_key:
        st.error("Please enter your API Key!")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # --- FIXED MODEL NAME FROM YOUR SCAN ---
            # Your scan showed 'gemini-3-flash-preview' is available
            model = genai.GenerativeModel('gemini-3-flash-preview')
            
            prompt = f"Create a student {goal} plan for a {diet_pref} diet on a {budget} budget."
            
            with st.spinner("🤖 AI is thinking deeply..."):
                # --- FIXED THINKING CONFIGURATION ---
                # For Gemini 3, thinking is configured within the generation_config
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "thinking_level": "medium" # 'medium' balances reasoning and speed
                    }
                )
                
                st.markdown(f'<div class="premium-card">{response.text}</div>', unsafe_allow_html=True)
                
        except Exception as e:
            # If thinking_level still errors, your library might need a refresh
            st.error(f"Something went wrong: {e}")
            st.info("Try running: pip install --upgrade google-generativeai")