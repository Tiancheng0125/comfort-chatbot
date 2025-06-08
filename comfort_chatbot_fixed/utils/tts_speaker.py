import pyttsx3

def speak_text(text, output_path="audio/reply.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()