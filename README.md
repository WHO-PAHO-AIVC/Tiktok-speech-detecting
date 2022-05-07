# Tiktok-speech-detecting
## Code Documentation - Bug Fixes

1. Clone the bug fixes branch of this repository

Command: `git clone --branch bug_fixes https://github.com/WHO-PAHO-AIVC/Tiktok-speech-detecting.git`

### Folder Structure

```
| Desktop
  | project
    | mp4_videos
      | video1.mp4
      | video2.mp4
      ...
    | text_files
      | video1.txt
      | video2.txt
    | wav_files
      | video1.wav
      | video2.wav
    | configs.json
    | Speach detecting from video to txt.py
```
Make sure the repo is cloned in the folder where the mp4 videos are stored. In the above case it is cloned into `.\Desktop\project`

Change your working directory in Command Line/Terminal to `Cd .\Desktop\project` before cloning the repository.

### Files

`configs.json`: before running the code on YOUR Mac/PC, change the directories in this file

**Directories to be changed**:

- `mp4_data_path`: path to the folder that has the mp4 files that need conversion to audio
- `save_path_wav`: path to folder that will store the converted mp4 audio files
- `save_path_txt`: path to the folder that will store the transcripts txt files

**Example**:

```
{
  "mp4_data_path": "C:\Users\John\Desktop\project\mp4_videos",
  "save_path_wav": "C:\Users\John\Desktop\project\wav_files",
  "save_path_txt": "C:\Users\John\Desktop\project\text_files"
}
```

Once changes have been made in `configs.json`, you can run the python script

Command: `python3 Speach detecting from video to txt.py`
