from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

width, height = 400, 300
image = Image.new('RGB', (width, height), (255, 255, 255))

response = requests.get('https://www.noblenaija.com/omo.jpg')
photo_image = Image.open(BytesIO(response.content))

image.paste(photo_image, (50, 50))

draw = ImageDraw.Draw(image)
name_text = 'John Smith'
name_font = ImageFont.truetype('arial.ttf', 36)
name_width, name_height = draw.textsize(name_text, font=name_font)
draw.text((200, 50), name_text, fill=(0, 0, 0), font=name_font)

company_text = 'Acme Corporation'
company_font = ImageFont.truetype('arial.ttf', 18)
company_width, company_height = draw.textsize(company_text, font=company_font)
draw.text((200, 100), company_text, fill=(0, 0, 0), font=company_font)

id_text = 'ID: 123456'
id_font = ImageFont.truetype('arial.ttf', 18)
id_width, id_height = draw.textsize(id_text, font=id_font)
draw.text((200, 150), id_text, fill=(0, 0, 0), font=id_font)

date_text = 'Issued: January 1, 2020'
date_font = ImageFont.truetype('arial.ttf', 18)
date_width, date_height = draw.textsize(date_text, font=date_font)
draw.text((200, 200), date_text, fill=(0, 0, 0), font=date_font)

# Save the ID card image as a JPEG file
image.save('id_card.jpeg')