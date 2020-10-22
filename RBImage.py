from PIL import Image, ImageDraw


def new(mode, size, color=0):
    image = Image.new(mode, size, color)
    return image.transpose(Image.ROTATE_180)
# waveshare gives us a reversed picture so we fix it here
