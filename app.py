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
st.write("Your journey to greatness starts **right here, right now!** Every effort, every step, every lesson adds up to success. Believe in yourself and take action! 💪✨")

# Motivational Quote 
st.header("💡 Thought for the Day")
st.write("*\"Your potential is endless. Keep pushing forward, and success will chase you!\"* 🔥")
st.markdown("---")

# Challenge Section
st.header("🔥 Identify Your Challenge")
user_input = st.text_input("What obstacle will you conquer today?")

if user_input:
    st.success(f"You're taking on: **{user_input}** 💪 Stay committed and keep progressing!")
else:
    st.warning("Define your challenge and turn it into an opportunity for growth!")

# Reflection Section
st.header("🧐 Self-Reflection")
reflection = st.text_area("What valuable insights did you gain today?")

if reflection:
    st.success(f"Key takeaway: **{reflection}** 🌟 Keep evolving and learning!")
else:
    st.info("Self-awareness fuels progress. Take a moment to reflect!")

# Achievement Section
st.header("🏆 Recognize Your Wins")
achievement = st.text_area("What’s one notable accomplishment from today?")

if achievement:
    st.success(f"Great job! You achieved: **{achievement}** 🎉 Keep striving for excellence!")
else:
    st.info("Every step forward is a step closer to your dreams. Celebrate your progress!")

# Footer 
st.markdown("---")
st.write("🌟 Keep pushing, stay consistent, and embrace the journey! 🌟")
st.write("🚀 Your mindset shapes your reality—make it UNSTOPPABLE! 🚀")
st.write("© 2025 Created with passion by Sadia Tariq")
