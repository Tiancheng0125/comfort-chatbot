
import streamlit as st
import os

# 设置网页标题与标签
st.set_page_config(
    page_title="Smart Heating Chatbot",
    layout="centered",
)

st.title("Smart Heating Chatbot")
st.subheader("Providing Emotional Value and Physical Comfort (Voice Input + Text Comfort)")

# 🔧 功能 1: 侧边栏介绍
with st.sidebar:
    st.header("📘 About This Project")
    st.markdown(
        "**Smart Heating Chatbot** offers both emotional support and physical comfort.\n\n"
        "- 🎤 Voice Input\n"
        "- 💬 Empathetic Chat\n"
        "- 🔊 Optional Voice Response (TTS)\n\n"
        "Ideal for **menstrual discomfort**, **neck pain**, or **emotional stress**."
    )

# 🔧 功能 2: 设置按钮 - 控制 TTS 开关
with st.sidebar:
    tts_enabled = st.checkbox("🔊 Enable Voice Feedback", value=True)

st.title("Smart Heating Chatbot")

audio_file = st.file_uploader("🎤 Upload your voice (WAV only)", type=["wav"])
if audio_file:
    with open("audio/record.wav", "wb") as f:
        f.write(audio_file.read())
    user_input = transcribe_audio("audio/record.wav")
    st.success(f"🗣 You said: {user_input}")
else:
    user_input = st.chat_input("📝 Or type how you're feeling...")

if user_input:
    full_prompt = build_prompt(system_prompt, st.session_state.history, user_input)
    output = llm(full_prompt, max_new_tokens=MAX_TOKENS, do_sample=True, temperature=TEMPERATURE)
    response = output[0]["generated_text"].strip()

    st.chat_message("user").markdown(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.history = update_history(st.session_state.history, user_input, response)

    speak_text(response, output_path="audio/reply.mp3")
    st.audio("audio/reply.mp3", format="audio/mp3")