import string
from pathlib import Path
from PIL import Image
import numpy as np


def load_images(img_folder: string):
    p = Path(img_folder)
    img_path = p / 'input'
    enc_path = p / 'enc'
    images_list = []
    enc_list = []
    for i in img_path.iterdir():
        img = Image.open(i)
        images_list.append(np.array(img))
        img.close()
    for i in enc_path.iterdir():
        img = Image.open(i)
        enc_list.append(np.array(img))
        img.close()
    return np.concatenate(images_list, axis=0), np.concatenate(enc_list, axis=0)


if __name__ == "__main__":
    load_images('data/train')
