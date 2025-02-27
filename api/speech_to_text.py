import os
import speech_recognition as sr
from pydub import AudioSegment

def extract_audio_from_video(video_file, audio_file='temp_audio.wav'):
    """Extract audio from video file and save as WAV format."""
    audio = AudioSegment.from_file(video_file)
    audio.export(audio_file, format='wav')
    return audio_file

def transcribe_audio(audio_file):
    """Transcribe audio file to text using SpeechRecognition."""
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
        try:
            # Using Google's Web Speech API
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
    
    return ""

def main(video_file):
    """Main function to process the video file and extract transcriptions."""
    # Extract audio from the video
    audio_file = extract_audio_from_video(video_file)
    
    # Transcribe the audio to text
    transcription = transcribe_audio(audio_file)

    # Clean up temporary audio file
    if os.path.exists(audio_file):
        os.remove(audio_file)

    return transcription

if __name__ == '__main__':
    # Example usage: replace 'your_video_file.mp4' with the path to your video file
    video_file = 'your_video_file.mp4'
    transcription = main(video_file)
    print("Transcription:\n", transcription)
