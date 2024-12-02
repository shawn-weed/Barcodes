import qrcode
from PIL import Image, ImageDraw, ImageFont
from zebrafy import ZebrafyImage

class Label:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def create_label(self):
        #Create qrcode
        qr = qrcode.make(f'{self.serial_number}')

        #Create label
        resize = qr.resize((150,150))
        logo = Image.open('./assets/logo.png')

        label_template = Image.new("RGBA", (406, 203), (0, 0, 0, 0))

        label_template.paste(resize, (0, 0))
        label_template.paste(logo, (150, 50))

        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 25)

        draw = ImageDraw.Draw(label_template)
        draw.text((0, 170), f"S/N - {self.serial_number}", font=font, fill="black")

        label_template.save("label.png")
        self.zpl = ZebrafyImage(label_template).to_zpl()
        return self.zpl