import speech_recognition as sr
import moviepy.editor
from tkinter import filedialog as fd
import os
import json


def transfer_mp4_to_wav(input_video, path_input_video, save_path_wav):
    print(path_input_video)
    video = moviepy.editor.VideoFileClip(path_input_video)
    audio = video.audio

    wav_filename = input_video.split(".mp4")[0] + ".wav"
    audio.write_audiofile(os.path.join(save_path_wav, wav_filename))

    audio.close()
    video.close()
    print("Transforming completed")



def speech_detecting_from_wav(input_audio_file, path_input_audio_file, save_path_txt):
    r = sr.Recognizer()
    audio_file = sr.AudioFile(path_input_audio_file)

    with audio_file as source:
        # r.adjust_for_ambient_noise(source)
        # use listen() instead of record()
        audio = r.listen(source)
        result = r.recognize_google(audio)
        print(result)

    filename = input_audio_file.split(".wav")[0] + ".txt"
    with open(os.path.join(save_path_txt, filename), mode="w") as file:
        file.write("Recognized text: ")
        # change /n to \n
        file.write("\n")
        file.write(result)

    print('Detecting completed')


if __name__ == '__main__':
    f = open("configs.json")
    configs = json.load(f)

    mp4_data_path = configs["mp4_data_path"]
    save_path_txt = configs["save_path_txt"]
    save_path_wav = configs["save_path_wav"]

    if not os.path.exists(save_path_wav):
        os.mkdir(save_path_wav)

    if not os.path.exists(save_path_txt):
        os.mkdir(save_path_txt)

    for input_video in os.listdir(mp4_data_path):
        if input_video.split(".mp4")[-1] == "":
            transfer_mp4_to_wav(input_video, os.path.join(mp4_data_path, input_video), save_path_wav)

    print("Wav files saved in: ", save_path_wav)

    for input_audio_file in os.listdir(save_path_wav):
        if input_audio_file.split(".wav")[-1] == "":
            speech_detecting_from_wav(input_audio_file, os.path.join(save_path_wav, input_audio_file), save_path_txt)

    print("Text files saved in: ", save_path_txt)
