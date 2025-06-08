def build_prompt(system_prompt, history, current_input, max_turns=5):
    prompt = system_prompt + "\n\n"
    for turn in history[-max_turns:]:
        prompt += f"User: {turn['user']}\nAI: {turn['ai']}\n"
    prompt += f"User: {current_input}\nAI:"
    return prompt

def update_history(history, user_input, ai_output):
    history.append({"user": user_input, "ai": ai_output})
    return history