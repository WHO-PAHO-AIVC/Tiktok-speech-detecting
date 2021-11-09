import moviepy.editor
from tkinter import filedialog as fd


def transfer_mp4_to_wav(input_video):
    video = moviepy.editor.VideoFileClip(input_video)
    audio = video.audio
    audio.write_audiofile(r"ouput.mp3")
    print("Transforming completed")


def main():
    input_video = fd.askopenfilename()
    transfer_mp4_to_wav(input_video)


main()
