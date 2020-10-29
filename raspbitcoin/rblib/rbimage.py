import os
from copy import deepcopy
from enum import Enum

import pyqrcode
from PIL import Image, ImageOps

from . import epd2in13_V2

'''
rbimage.py includes all e-paper display operation functions
NOTICE: ALL ORIENTATION HAS BEEN CORRECTED BY HACKING THE LIB epd2in13_V2.py
'''

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 122

img_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

epd = epd2in13_V2.EPD()


class Coins(Enum):
    BTC = "btc"
    ETH = "eth"


def fit_screen(self: Image.Image):
    ratio_width = SCREEN_WIDTH / self.size[0]
    ratio_height = SCREEN_HEIGHT / self.size[1]
    ratio = ratio_width if ratio_width < ratio_height else ratio_height

    new_size = tuple([int(x * ratio) for x in self.size])
    new_image = ImageOps.pad(self.resize(new_size, Image.ANTIALIAS), (SCREEN_WIDTH, SCREEN_HEIGHT), color='white')
    return new_image


def display_address(address: str, coin_type=Coins.BTC):
    qrcode_addr = pyqrcode.create(address)
    qrcode_addr.png(address + '.png', scale=2, quiet_zone=0)
    qrcode_addr_img = Image.open(address + '.png')  # small enough to insert

    coin_bg_name = coin_type.value + "-bg.png"
    bg_img = Image.open(os.path.join(img_dir, coin_bg_name))
    result = insert_qr_to_bg(qrcode_addr_img, bg_img)

    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(bg_img))
    # todo: this needs to be done upon whole init, not here

    epd.init(epd.PART_UPDATE)
    epd.displayPartial(epd.getbuffer(result))
    epd.sleep()
    # exit device cannot be done here


def insert_qr_to_bg(qr: Image.Image, bg: Image.Image):
    ret = deepcopy(bg)
    qr_w, qr_h = qr.size  # qr width = height
    bg_w, bg_h = bg.size
    offset = ((bg_h - qr_w) // 2, (bg_h - qr_h) // 2)  # want to make it on left side
    ret.paste(qr, offset)
    return ret


def display_tx_info():
    pass
