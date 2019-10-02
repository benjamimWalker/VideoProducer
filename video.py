import shutil
import cv2
import glob
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance
try:
    from Production.text import text_wiki
except ModuleNotFoundError:
    exec('from text import text_wiki')
try:
    from Production.image import get_images, enquadrar
except ModuleNotFoundError:
    exec('from image import get_images, enquadrar')
from random import uniform, randint, choice
try:
    from Production.audio import add_song, add_voice, pega_audio
except ModuleNotFoundError:
    exec('from audio import add_song, add_voice, pega_audio')
import os
import webbrowser
try:
    from Production.gettags import get_tags
except ModuleNotFoundError:
    exec('from gettags import get_tags')


descricao = ''

oq = input('Um video sobre o que? Senhor:  ')
comple = input('Complemento: ')
get_images(oq)


def anti_jpg_uppercase(path: str):
    if path.endswith('.JPG'):
        listadepath = list(path)
        for c in range(-1, -4, -1):
            listadepath[c] = listadepath[c].lower()
        os.rename(path, ''.join(listadepath))
    else:
        pass


def darken(path):
    peak = Image.open(path)
    enhancer = ImageEnhance.Brightness(peak)
    bright = enhancer.enhance(0.38)
    os.remove(path)
    bright.save(path)


def add_after_terme(total):
    lista = list()
    for letra in total:
        lista.append(letra)
    lista.insert(-4, 'coisa aleatoria que nao aparece em todo lugar')
    return ''.join(lista)


fnt = ImageFont.truetype('/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/Champagne & Limousines Bold.ttf', randint(131, 144))
fnt_title = ImageFont.truetype('/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/Champagne & Limousines Bold Italic.ttf', randint(290, 381))


# def resize(path, width, height):
#     im = Image.open(path)
#     im2 = ImageOps.fit(im, (width, height), Image.ANTIALIAS)
#     os.remove(path)
#     im2.save(path)


pathiss = glob.glob(f'/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/{oq}/*')
for pathinho in pathiss:
    anti_jpg_uppercase(pathinho)

images = glob.glob(f'/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/{oq}/*.jpg')
sounds = glob.glob(f'/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/*.mp3')

for filenames in images:
    enquadrar(filenames)

images.sort()
for filename in images:
    if 'coisa aleatoria que nao aparece em todo lugar' in filename:
        continue
    shutil.copy(filename, add_after_terme(filename))



def write_the_info(listfrase):
    j: int = 0
    pictures = glob.glob(f'/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/{oq}/*.jpg')
    pictures.sort()
    for namefile in pictures:
        if 'coisa aleatoria que nao aparece em todo lugar' not in namefile:
            if j == 0:
                darken(namefile)
                im = Image.open(namefile)
                im2 = ImageDraw.Draw(im)
                im2.text((randint(190, 230), randint(520, 560)), oq.title(), fill=(255, 255, 255), font=fnt_title)
                os.remove(namefile)
                im.save(namefile)
                os.remove(add_after_terme(namefile))
            continue
        if j == 1:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            im2.text((63, choice((220, 980, 1080))), listfrase[0], fill=(255, 255, 255), font=fnt)
            os.remove(namefile)
            im.save(namefile)
        if j == 2:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            im2.text((63, choice((220, 980, 1080))), listfrase[1], fill=(255, 255, 255), font=fnt)
            os.remove(namefile)
            im.save(namefile)
        if j == 3:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            im2.text((63, choice((220, 980, 1080))), listfrase[2], fill=(255, 255, 255), font=fnt)
            os.remove(namefile)
            im.save(namefile)
        if j == 4:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            im2.text((63, choice((220, 980, 1080))), listfrase[3], fill=(255, 255, 255), font=fnt)
            os.remove(namefile)
            im.save(namefile)
        if j == 5:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            im2.text((63, choice((220, 980, 1080))), listfrase[4], fill=(255, 255, 255), font=fnt)
            os.remove(namefile)
            im.save(namefile)
        if j == 6:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            try:
                im2.text((63, choice((220, 980, 1080))), listfrase[5], fill=(255, 255, 255), font=fnt)
            except:
                pass
            os.remove(namefile)
            im.save(namefile)
        if j == 7:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            try:
                im2.text((63, choice((220, 980, 1080))), listfrase[6], fill=(255, 255, 255), font=fnt)
            except:
                pass
            os.remove(namefile)
            im.save(namefile)
        if j == 8:
            darken(namefile)
            im = Image.open(namefile)
            im2 = ImageDraw.Draw(im)
            try:
                im2.text((63, choice((220, 980, 1080))), listfrase[7], fill=(255, 255, 255), font=fnt)
            except:
                pass
            os.remove(namefile)
            im.save(namefile)
        j += 1


images = glob.glob(f'/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/{oq}/*.jpg')
images.sort()


lista = text_wiki(oq, complement=comple)
write_the_info(lista)


img_array = []
images = glob.glob(f'/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/{oq}/*.jpg')
images.sort()
for filename in images:
    img = cv2.imread(filename)
    height, width, layers = img.shape

    size = width, height
    print(size)
    img_array.append(img)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), uniform(0.11, 0.21), (3480, 2160))
for i in range(len(img_array)):
    out.write(img_array[i])


img = cv2.imread('/home/benjamim/PycharmProjects/Nyte/ImagesAndSounds/finalscreen.jpg')
out.write(img)
out.release()

os.rename('project.avi', f'{oq.title()}.mp4')
# shutil.copy(f'{oq}.mp4', f'{oq}.mp4'+'1.mp4')

for items in lista:
    descricao += items + '\n'

add_song(f'{oq.title()}.mp4', choice(sounds))
#add_voice(f'{oq}.mp4', descricao)
# add_song(f'{oq}.mp4' + '1.mp4', pega_audio(f'{oq}.mp4'))
# os.remove(f'{oq}.mp4')
# os.remove(f'{oq}.mp4' + '.mp3')
# os.rename(f'{oq}.mp4' + '1.mp4', f'{oq}.mp4')

for image in images:
    os.remove(image)

print('\n' + '-' * 20 + '\n')
print(f'DESCRIÇAO:\n\033[34mHey there!\nHere is my script: {descricao}\n')
print('\n' + '_' * 20 + '\n')
webbrowser.open('https://www.youtube.com/upload')
get_tags(oq)
