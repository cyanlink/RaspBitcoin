from enum import Enum

from PIL import Image, ImageOps
import qrcode
import os

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 122

imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

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

def display_address(address, coin_type: Coins):
    qrcode_addr = qrcode.make(address)
    coin_img_name = coin_type + "jpg"
    bg_img = Image.open(os.path.join(imgdir, coin_img_name))
    # merge bg_img and address image then commit it to epaper display
