from urllib import response
from PIL import Image, ImageDraw, ImageFont
import requests
import json
import textwrap
from pexels_api import API
from io import BytesIO
import time
import random

print("Collecting Image Data...")

PEXELS_API_KEY = '563492ad6f91700001000001ccee9913e3b94277ba5cb2b2d4b27e28'
api = API(PEXELS_API_KEY)
api.search('dark nature', page=1, results_per_page=50)
photos = api.get_entries()

image = random.randint(0, 49)

background = photos[image].original
img_data = requests.get(background)

print("Selecting a Quote...")
time.sleep(5)
result = requests.get('https://zenquotes.io/api/random')
response = json.loads(result.text)
quote = response[0]['q']
# text wrap the quote
quote = textwrap.fill(quote, width=40)
font = ImageFont.truetype('Lobster-Regular.ttf', 100)


img = Image.open(fp=BytesIO(img_data.content), mode='r')


draw = ImageDraw.Draw(img)

##x, y = 300, 300
##shadowcolor = "grey"

# thicker border
##draw.text((x-1, y-1), quote, font=font, fill=shadowcolor)
##draw.text((x+1, y-1), quote, font=font, fill=shadowcolor)
##draw.text((x-1, y+1), quote, font=font, fill=shadowcolor)
##draw.text((x+1, y+1), quote, font=font, fill=shadowcolor)


draw.text(xy=(300, 300), font=font, text=quote, fill='#FFFFFF')

title = random.randint(1, 1000)

img.save(str(title)+'.jpg')

print("Done!")
