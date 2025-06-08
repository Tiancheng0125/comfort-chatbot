import streamlit as st
from utils.model_loader import load_llama_pipeline
from utils.memory_manager import build_prompt, update_history
from utils.stt_whisper import transcribe_audio
from utils.tts_speaker import speak_text
from config import MAX_TOKENS, TEMPERATURE, HISTORY_LENGTH
import os

llm = load_llama_pipeline()

with open("prompts/system_prompt.txt", "r") as f:
    system_prompt = f.read()

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎙 Comfort Chatbot (Voice Input + Text Comfort)")

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
    response = output[0]["generated_text"].split("AI:")[-1].strip()

    st.chat_message("user").markdown(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.history = update_history(st.session_state.history, user_input, response)

    speak_text(response, output_path="audio/reply.mp3")
    st.audio("audio/reply.mp3", format="audio/mp3")