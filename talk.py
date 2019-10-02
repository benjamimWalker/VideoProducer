from gtts import gTTS


def speech(term):
    file = gTTS(text=term, lang='en')
    file.save('/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/' + term[0:3] + '.mp3')
    return '/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/' + term[0:3] + '.mp3'
