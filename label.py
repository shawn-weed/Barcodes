import qrcode
from PIL import Image, ImageDraw, ImageFont
from zebrafy import ZebrafyImage

class Label:
    def __init__(self, serial_number):
        self.serial_number = serial_number

        #Create qrcode
        qr = qrcode.make(f'{self.serial_number}')

        #Create label
        resize = qr.resize((150,150))
        logo = Image.open('./assets/logo.png')

        self.label_template = Image.new("RGB", (406, 203), "white")

        self.label_template.paste(resize, (0, 0))
        self.label_template.paste(logo, (150, 50))

        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 25)

        draw = ImageDraw.Draw(self.label_template)
        draw.text((0, 170), f"S/N - {self.serial_number}", font=font, fill="black")
        
        self.zebra_image = ZebrafyImage(self.label_template, invert=True).to_zpl()