from PIL import Image, ImageOps

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 122


def fit_screen(self: Image.Image):
    ratio_width = SCREEN_WIDTH / self.size[0]
    ratio_height = SCREEN_HEIGHT / self.size[1]
    ratio = ratio_width if ratio_width < ratio_height else ratio_height

    new_size = tuple([int(x * ratio) for x in self.size])
    new_image = ImageOps.pad(self.resize(new_size, Image.ANTIALIAS), (SCREEN_WIDTH, SCREEN_HEIGHT), color='white')
    return new_image
