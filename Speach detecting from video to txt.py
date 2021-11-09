import speech_recognition as sr
import moviepy.editor
from tkinter import filedialog as fd


def transfer_mp4_to_wav(input_video):
    video = moviepy.editor.VideoFileClip(input_video)
    audio = video.audio
    audio.write_audiofile("test.wav")
    print("Transforming completed")


def speech_detecting_from_wav(input_audio_file):
    r = sr.Recognizer()
    audio_file = sr.AudioFile(input_audio_file)

    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        result = r.recognize_google(audio)

    with open("test.txt", mode="w") as file:
        file.write("Recognized text: ")
        file.write("/n")
        file.write(result)
    print('Detecting completed')


def main():
    input_video = fd.askopenfilename()
    transfer_mp4_to_wav(input_video)
    input_audio_file = fd.askopenfilename()
    speech_detecting_from_wav(input_audio_file)


main()
