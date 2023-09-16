from PIL import Image, ImageDraw, ImageFont
import datetime
import qrcode
import os
import uuid
import secrets

from config import Config


class CreatePicture:
    def __init__(self, image, bus_id):
        self.image = image
        self.bus_id = bus_id

    def create_date(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M")
        return formatted_datetime
    
    def create_key(self):
        part1 = str(uuid.uuid4())
        part2 = str(uuid.uuid4())
        part3 = str(uuid.uuid4())
        part4 = str(secrets.randbelow(9999999999))
        part5 = str(secrets.randbelow(99999))       
        part6 = str(secrets.randbelow(9999999999))
        part7 = str(secrets.randbelow(9999999999))

        last_part = secrets.token_hex(64)

        generated_key = f"rsctl://{part1}:{part2}:{part3}:{part4}:{part5}:{part6}:{part7}:{self.bus_id}:{last_part}"
        return generated_key
            
    def create_qrcode(self):
        data = self.create_key()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=9, 
            border=0,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("output_qr_code.jpg")

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

    def generate_ticket(self):
        background_image = Image.open(Config.output_image_path)
        inserted_image = Image.open("output_qr_code.jpg")

        position = (32, 497)
        background_image.paste(inserted_image, position)
        background_image.save("ticket.jpg")

        self.delete_files(Config.output_image_path)
        self.delete_files(Config.output_qr_code_path)

    def delete_files(self, path):
        os.remove(path)
