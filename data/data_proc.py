import os
from PIL import Image


def make_square(im_path, size=(28, 28), fill_color=(0,0,0,0)):
    im = Image.open(im_path)
    im.thumbnail(size, Image.ANTIALIAS)
    background = Image.new('RGB', size, (0, 0, 0))
    background.paste( im, (int((size[0] - im.size[0]) / 2), int((size[1] - im.size[1]) / 2)))
    x, y = im.size
    background.save(im_path)


for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        im_path = os.path.join(root, name)
        if im_path[-3:] == 'jpg':
            make_square(im_path)



