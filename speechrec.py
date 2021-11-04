import speech_recognition as sr
from tkinter import filedialog as fd


r = sr.Recognizer()
input_file = fd.askopenfilename()
audio_file = sr.AudioFile(input_file)

with audio_file as source:
	r.adjust_for_ambient_noise(source)
	audio = r.record(source)
	result = r.recognize_google(audio)

with open("test.txt", mode = "w")as file:
	file.write("Recognized text: ")
	file.write("/n", result)
