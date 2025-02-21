


import streamlit as st

# Page configuration
st.set_page_config(page_title="Master Your Mindset 🚀", page_icon="🔹")
st.title("🚀 Master Your Mindset: Daily Growth Journal 🚀 ")

# Custom Styling
st.markdown("""
<style>
body {
    background-color: #e3f2fd;
}
h1 {
    color: #002855;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}
h2 {
    color: #00509e;
    font-size: 34px;
    font-weight: bold;
}
p {
    color: #222;
    font-size: 20px;
}
.stAlert {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Welcome Section
st.header("🎯 Welcome, High Achiever! 🌟")
st.write("Your path to continuous improvement begins here. Every small effort compounds over time! 🌟")

# Motivational Quote 
st.header("💡 Thought for the Day")
st.write(">>" + "Believe you can and you're halfway there." + " - Theodore Roosevelt 🔥")
st.markdown("---")

# Challenge Section
st.header("🔥 Identify Your Challenge")
user_input = st.text_input("What personal or professional challenge are you tackling today?")

if user_input:
    st.success(f"You're taking on: **{user_input}** 💪 Stay committed and keep progressing!")
else:
    st.warning("Define your challenge to take meaningful action!")

# Reflection Section
st.header("🧐 Self-Reflection")
reflection = st.text_area("What valuable insights did you gain today?")

if reflection:
    st.success(f"Key takeaway: **{reflection}** 🌟 Keep learning and evolving!")
else:
    st.info("Self-awareness fuels progress. Take a moment to reflect!")

# Achievement Section
st.header("🏆 Recognize Your Wins")
achievement = st.text_area("What’s one notable accomplishment from today?")

if achievement:
    st.success(f"Great job! You achieved: **{achievement}** 🎉 Keep striving for excellence!")
else:
    st.info("Acknowledging your progress keeps motivation high!")

# Footer 
st.markdown("---")
st.write("🌟 Keep pushing forward, stay consistent, and embrace the journey! 🌟")
st.write("🚀 Your mindset shapes your reality—make it unstoppable! 🚀")
st.write("© 2025 Created with passion by Sadia Tariq")