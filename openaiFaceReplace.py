import os
import base64
import requests
from PIL import Image # Run pip install Pillow
from openai import OpenAI # https://github.com/openai/openai-python/discussions/742
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY'),
)
# to edit existing image
def censor(image):
  text = "remove the face in the picture, replace it with an ai generated face"
  out = client.images.edit(
  model ="gpt-image-1.5",
  image= [open(image,'rb')],
  prompt=text,
  n=1)
  return base64.b64decode(out.data[0].b64_json)

edited= censor('./imgs/random_man.jpg')
with open('./imgs/openai/random_man_openai.png','wb') as file:
	file.write(edited)
