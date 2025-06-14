import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Forex Wizard AI", layout="centered")

st.title("🧠 Forex Wizard - Live Chart Analyzer")

st.markdown("### 📥 Upload a Live Market Chart Screenshot")
uploaded_file = st.file_uploader("Upload chart image (JPG/PNG)", type=["jpg", "jpeg", "png"])

st.markdown("### ✍️ Enter your Strategy Prompt")
user_prompt = st.text_area("For example: Should I buy or sell using support and resistance strategy?")

run = st.button("▶️ Analyze")

if run:
    if uploaded_file is None or user_prompt.strip() == "":
        st.warning("Please upload an image and enter a prompt to analyze.")
    else:
        # Show image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Chart", use_column_width=True)

        with st.spinner("Analyzing market chart with strategy..."):
            time.sleep(2)

        # OUTPUT SECTION (Currently Hardcoded Sample)
        st.markdown("## 🧾 Market Analysis Result")

        st.markdown(f"""
        📌 Prompt: _{user_prompt}_

        📈 Trend Analysis  
        Strong bullish trend identified using recent resistance break.

        ✅ Entry Price: 3035.00  
        🎯 Take Profit (TP): 3085.00 (Approx. 5000 pips)  
        🛑 Stop Loss (SL): 3010.00

        💡 Recommendation: Buy  
        - Price broke above resistance zone with strong momentum.
        - RSI and volume confirm bullish strength.
        - Safe SL below last support. High reward opportunity.

        ⚠️ Use proper risk management. Conditions may change in live market.
        """)
