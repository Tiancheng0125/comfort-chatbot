from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def load_llama_pipeline():
    def generate(prompt, **kwargs):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=kwargs.get("max_new_tokens", 150),
            temperature=kwargs.get("temperature", 0.7)
        )
        return [{"generated_text": response.choices[0].message.content}]
    return generate