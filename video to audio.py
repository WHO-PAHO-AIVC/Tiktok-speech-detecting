import moviepy.editor
from tkinter import filedialog as fd


input_video = fd.askopenfilename()
video = moviepy.editor.VideoFileClip(input_video)
audio = video.audio

audio.write_audiofile("test1.wav")
print("Completed")