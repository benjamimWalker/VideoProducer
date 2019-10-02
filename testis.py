from cv2 import cv2
from PIL import Image, ImageFilter, ImageOps
from cv2 import imread, imwrite, blur
import os


def bluri(path_to_blur):
    img = imread(path_to_blur)
    dst = blur(img, (40, 40))
    imwrite(path_to_blur, dst)


def max_resolution_on_target(target, what_to_change):
    x = what_to_change[0]
    y = what_to_change[1]

    a = target[0]
    b = target[1]

    cont = 0
    while True:
        cont += 1
        if x * cont > a or y * cont > b:
            return x * (cont - 1), y * (cont - 1)


def resize(path: str, width: int, height: int, nome_para_salvar: str):
    im = Image.open(path)
    im2 = ImageOps.fit(im, (width, height), Image.ANTIALIAS)

    im2.save(path + nome_para_salvar)


def get_coordenates(img1, img2):
    shape1, shape2 = img1.shape, img2.shape
    init_h = round((shape1[1] - shape2[1]) / 2)
    init_v = round((shape1[0] - shape2[0]) / 2)
    final_h = init_h + shape2[1]
    final_v = init_v + shape2[0]
    return init_h, init_v, final_h, final_v




def enquadrar(image_path):
    original_image = Image.open(image_path)
    resize(image_path, 3480, 2160, 'resized.jpg')
    bluri(image_path + 'resized.jpg')
    for_resize_1 = cv2.imread(image_path)
    #original_image.resize(max_resolution_on_target([3480, 2160], [for_resize_1.shape[1], for_resize_1.shape[0]]), Image.ANTIALIAS)
    resize(image_path, max_resolution_on_target([3480, 2160], [for_resize_1.shape[1], for_resize_1.shape[0]])[0], max_resolution_on_target([3480, 2160], [for_resize_1.shape[1], for_resize_1.shape[0]])[1], 'Maior.jpg')
    original_image = Image.open(image_path + 'Maior.jpg')
    for_resize_1 = cv2.imread(image_path + 'Maior.jpg')
    for_resize_2 = cv2.imread(image_path + 'resized.jpg')
    resized_image = Image.open(image_path + 'resized.jpg')
    resized_image.paste(original_image, get_coordenates(for_resize_2, for_resize_1))
    os.remove(image_path)
    resized_image.save(image_path)
    os.remove(image_path + 'resized.jpg')
    os.remove(image_path + 'Maior.jpg')




