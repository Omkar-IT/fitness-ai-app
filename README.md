# 🥗 Track It: Student AI Fitness

**Track It** is an AI-powered fitness and nutrition planner designed specifically for students. It leverages Google's **Gemini 3 Flash** model to generate personalized, budget-friendly diet plans and home workout routines based on individual body metrics.

🔗 **[Live Demo](https://fitness-ai-app-omkar-it.streamlit.app/)**

## 🚀 Features

* **🧠 AI Reasoning Engine:** Uses the latest `gemini-3-flash-preview` with "Thinking" logic to create scientifically accurate plans.
* **📊 Smart Body Metrics:** Automatically calculates BMI based on user height (cm) and weight (kg).
* **💸 Budget-First Design:** Algorithms prioritize affordable ingredients (like lentils, eggs, and oats) for student budgets.
* **🎨 Premium UI:** Features a modern dark mode with glassmorphism cards and glowing buttons.
* **🔐 Secure:** Uses Streamlit Secrets for API key management.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python)
* **AI Model:** Google Gemini 3 Flash (`google-generativeai`)
* **Deployment:** Streamlit Community Cloud
* **Version Control:** Git & GitHub

## ⚙️ How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Omkar-IT/fitness-ai-app.git](https://github.com/Omkar-IT/fitness-ai-app.git)
    cd fitness-ai-app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

```text
fitness-ai-app/
├── app.py              # Main application logic and UI
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
