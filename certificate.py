from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
width, height = 400, 300
image = Image.new('RGB', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(image)
title_text = 'Certificate of Completion'
title_font = ImageFont.truetype('arial.ttf', 36)
title_width, title_height = draw.textsize(title_text, font=title_font)
draw.text(((width - title_width) / 2, 50), title_text, fill=(0, 0, 0), font=title_font)

content_text = 'This certificate is awarded to:'
content_font = ImageFont.truetype('arial.ttf', 18)
content_width, content_height = draw.textsize(content_text, font=content_font)
draw.text(((width - content_width) / 2, 100), content_text, fill=(0, 0, 0), font=content_font)

response = requests.get('https://www.example.com/signature.png')
signature_image = Image.open(BytesIO(response.content))

image.paste(signature_image, (100, 200))

# Save the certificate image as a JPEG file
image.save('certificate.jpeg')