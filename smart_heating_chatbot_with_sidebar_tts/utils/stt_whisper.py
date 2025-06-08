from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")

def transcribe_audio(audio_file_path):
    segments, info = model.transcribe(audio_file_path)
    return " ".join([segment.text for segment in segments])