import os

import moviepy.editor as mp
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
from os import remove, rename
try:
    from Production.talk import speech
except ModuleNotFoundError:
    exec('from talk import speech')


def cut(tupla, audio_path):
    endTime = tupla[0] * 60 * 1000 + tupla[1] * 1000
    song = AudioSegment.from_mp3(audio_path)
    extract = song[0:endTime]
    extract.export(audio_path + 'copy.mp3', format="mp3")
    return audio_path + 'copy.mp3'


def get_len(video):
    clip = VideoFileClip(video)
    dur = int(clip.duration)
    mins, secs = dur // 60 % 60, dur % 60

    mins = "0" + str(mins) if (mins < 10) else str(mins)
    secs = "0" + str(secs) if (secs < 10) else str(secs)
    return int(mins), int(secs)


def add_song(video_path, audio_path):
    path_for_delete = cut(get_len(video_path), audio_path)
    video = mp.VideoFileClip(video_path)
    video.write_videofile(video_path + '.audio.mp4',
                          audio=path_for_delete)
    remove(video_path)
    rename(video_path + '.audio.mp4', video_path)
    remove(path_for_delete)


def add_voice(video_path, term):
    videoclip = VideoFileClip(video_path)
    audioclip = AudioFileClip(speech(term))
    new_audioclip = CompositeAudioClip([videoclip.audio, audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(video_path)
    os.remove('/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/' + term[0:3] + '.mp3')


def pega_audio(path):
    videoclip = VideoFileClip(path)
    audioclip = videoclip.audio
    audioclip.write_audiofile(path + '.mp3')
    return path + '.mp3'



