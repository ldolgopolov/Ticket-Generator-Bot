from PIL import Image, ImageDraw, ImageFont
import datetime
from config import Config


class CreatePicture:
    def __init__(self, image, bus_id):
        self.image = image
        self.bus_id = bus_id

    def create_date(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M")
        return formatted_datetime

    def write_data(self):
        date = self.create_date()
        draw = ImageDraw.Draw(self.image)

        font_size = 27
        font_color = (225, 225, 225)
        font = ImageFont.truetype(Config.font_path, font_size)

        date_position = (275, 183)
        bus_id_position = (326, 229)

        draw.text(bus_id_position, self.bus_id, font=font, fill=font_color)
        draw.text(date_position, date, font=font, fill=font_color)
        self.image.save(Config.output_image_path)



